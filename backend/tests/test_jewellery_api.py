"""Tests for jewellery store management API."""

import os
import sys
from datetime import datetime

import pytest
import requests
from dotenv import load_dotenv

# Load environment variables
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
load_dotenv()

API_BASE = os.getenv("TEST_API_URL", "http://localhost:8001/api")


def test_server_is_running():
    """Test that the server is running."""
    response = requests.get(f"{API_BASE}/", timeout=5)
    assert response.status_code == 200, "Server is not running"


class TestAuthentication:
    """Test authentication endpoints."""

    def setup_method(self):
        """Setup test data."""
        self.test_user = {
            "email": "owner@test.com",
            "password": "test123",
        }

    def test_login_with_valid_credentials(self):
        """Test login with valid credentials."""
        response = requests.post(f"{API_BASE}/auth/login", json=self.test_user, timeout=5)
        assert response.status_code == 200, f"Login failed: {response.text}"

        data = response.json()
        assert "token" in data, "Token not in response"
        assert "user" in data, "User not in response"
        assert data["user"]["email"] == self.test_user["email"]

    def test_login_with_invalid_credentials(self):
        """Test login with invalid credentials should fail."""
        invalid_user = {"email": "owner@test.com", "password": "wrongpassword"}
        response = requests.post(f"{API_BASE}/auth/login", json=invalid_user, timeout=5)
        assert response.status_code == 401, "Should return 401 for invalid credentials"

    def test_get_me_without_token(self):
        """Test /auth/me without token should fail."""
        response = requests.get(f"{API_BASE}/auth/me", timeout=5)
        assert response.status_code == 403, "Should return 403 without token"

    def test_get_me_with_valid_token(self):
        """Test /auth/me with valid token."""
        # Login first
        login_resp = requests.post(f"{API_BASE}/auth/login", json=self.test_user, timeout=5)
        assert login_resp.status_code == 200
        token = login_resp.json()["token"]

        # Get current user
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{API_BASE}/auth/me", headers=headers, timeout=5)
        assert response.status_code == 200, f"Failed to get user: {response.text}"

        data = response.json()
        assert data["email"] == self.test_user["email"]


class TestInventory:
    """Test inventory management endpoints."""

    def setup_method(self):
        """Setup test data."""
        # Login to get token
        login_resp = requests.post(
            f"{API_BASE}/auth/login",
            json={"email": "staff@test.com", "password": "test123"},
            timeout=5,
        )
        assert login_resp.status_code == 200
        self.token = login_resp.json()["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def test_get_items_public(self):
        """Test public catalog access without authentication."""
        response = requests.get(f"{API_BASE}/inventory/items", timeout=5)
        assert response.status_code == 200, f"Failed to get items: {response.text}"

        data = response.json()
        assert "items" in data
        assert "page" in data
        assert "total" in data
        assert "has_more" in data

    def test_get_items_authenticated(self):
        """Test inventory access with authentication."""
        response = requests.get(
            f"{API_BASE}/inventory/items", headers=self.headers, timeout=5
        )
        assert response.status_code == 200, f"Failed to get items: {response.text}"

        data = response.json()
        assert isinstance(data["items"], list)

    def test_create_item_success(self):
        """Test creating a jewellery item."""
        item_code = f"TEST-{datetime.now().timestamp()}"
        new_item = {
            "item_code": item_code,
            "name": "Test Diamond Ring",
            "description": "Beautiful diamond ring for testing",
            "category": "ring",
            "price": 50000,
            "weight": 5.5,
            "material": "gold",
            "images": [],
        }

        response = requests.post(
            f"{API_BASE}/inventory/items",
            json=new_item,
            headers=self.headers,
            timeout=5,
        )
        assert response.status_code == 201, f"Failed to create item: {response.text}"

        data = response.json()
        assert data["item_code"] == item_code
        assert data["name"] == new_item["name"]
        assert data["status"] == "available"

    def test_create_item_duplicate_code(self):
        """Test creating item with duplicate code should fail."""
        item_code = f"DUP-{datetime.now().timestamp()}"
        new_item = {
            "item_code": item_code,
            "name": "First Item",
            "description": "First item",
            "category": "ring",
            "price": 10000,
            "weight": 2.0,
            "material": "silver",
        }

        # Create first item
        response1 = requests.post(
            f"{API_BASE}/inventory/items",
            json=new_item,
            headers=self.headers,
            timeout=5,
        )
        assert response1.status_code == 201

        # Try to create duplicate
        response2 = requests.post(
            f"{API_BASE}/inventory/items",
            json=new_item,
            headers=self.headers,
            timeout=5,
        )
        assert response2.status_code == 400, "Should fail with duplicate item_code"

    def test_create_item_without_auth(self):
        """Test creating item without authentication should fail."""
        new_item = {
            "item_code": "NOAUTH",
            "name": "No Auth Item",
            "description": "Should fail",
            "category": "ring",
            "price": 10000,
            "weight": 2.0,
            "material": "silver",
        }

        response = requests.post(f"{API_BASE}/inventory/items", json=new_item, timeout=5)
        assert response.status_code in [401, 403], "Should require authentication"

    def test_update_item(self):
        """Test updating an item."""
        # First create an item
        item_code = f"UPD-{datetime.now().timestamp()}"
        new_item = {
            "item_code": item_code,
            "name": "Original Name",
            "description": "Original description",
            "category": "ring",
            "price": 10000,
            "weight": 2.0,
            "material": "silver",
        }

        create_resp = requests.post(
            f"{API_BASE}/inventory/items",
            json=new_item,
            headers=self.headers,
            timeout=5,
        )
        assert create_resp.status_code == 201
        item_id = create_resp.json()["id"]

        # Update the item
        update_data = {"name": "Updated Name", "price": 15000}
        update_resp = requests.patch(
            f"{API_BASE}/inventory/items/{item_id}",
            json=update_data,
            headers=self.headers,
            timeout=5,
        )
        assert update_resp.status_code == 200, f"Failed to update: {update_resp.text}"

        data = update_resp.json()
        assert data["name"] == "Updated Name"
        assert data["price"] == 15000


class TestOrders:
    """Test order management endpoints."""

    def setup_method(self):
        """Setup test data."""
        # Login as staff
        login_resp = requests.post(
            f"{API_BASE}/auth/login",
            json={"email": "staff@test.com", "password": "test123"},
            timeout=5,
        )
        assert login_resp.status_code == 200
        self.token = login_resp.json()["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

        # Create a test item for orders
        item_code = f"ORD-ITEM-{datetime.now().timestamp()}"
        new_item = {
            "item_code": item_code,
            "name": "Order Test Item",
            "description": "Item for order testing",
            "category": "ring",
            "price": 20000,
            "weight": 3.0,
            "material": "gold",
        }
        create_resp = requests.post(
            f"{API_BASE}/inventory/items",
            json=new_item,
            headers=self.headers,
            timeout=5,
        )
        assert create_resp.status_code == 201
        self.test_item_id = create_resp.json()["id"]

    def test_create_order_public(self):
        """Test creating an order without authentication (public endpoint)."""
        order_data = {
            "customer_name": "John Doe",
            "customer_phone": "+1234567890",
            "customer_address": "123 Test Street, Test City, 12345",
            "items": [{"item_id": self.test_item_id, "quantity": 1}],
        }

        response = requests.post(f"{API_BASE}/orders", json=order_data, timeout=5)
        assert response.status_code == 201, f"Failed to create order: {response.text}"

        data = response.json()
        assert data["customer_name"] == order_data["customer_name"]
        assert data["payment_method"] == "COD"
        assert data["status"] == "pending"
        assert len(data["items"]) == 1

    def test_create_order_with_invalid_item(self):
        """Test creating order with non-existent item should fail."""
        order_data = {
            "customer_name": "Jane Doe",
            "customer_phone": "+1234567890",
            "customer_address": "456 Test Avenue, Test City, 12345",
            "items": [{"item_id": "invalid-item-id", "quantity": 1}],
        }

        response = requests.post(f"{API_BASE}/orders", json=order_data, timeout=5)
        assert response.status_code == 404, "Should fail with invalid item"

    def test_get_orders_requires_auth(self):
        """Test getting orders without authentication should fail."""
        response = requests.get(f"{API_BASE}/orders", timeout=5)
        assert response.status_code in [401, 403], "Should require authentication"

    def test_get_orders_with_auth(self):
        """Test getting orders with authentication."""
        response = requests.get(f"{API_BASE}/orders", headers=self.headers, timeout=5)
        assert response.status_code == 200, f"Failed to get orders: {response.text}"

        data = response.json()
        assert "orders" in data
        assert "page" in data
        assert "total" in data

    def test_update_order_status(self):
        """Test updating order status."""
        # First create an order
        order_data = {
            "customer_name": "Status Test",
            "customer_phone": "+1234567890",
            "customer_address": "789 Test Boulevard, Test City, 12345",
            "items": [{"item_id": self.test_item_id, "quantity": 1}],
        }

        create_resp = requests.post(f"{API_BASE}/orders", json=order_data, timeout=5)
        assert create_resp.status_code == 201
        order_id = create_resp.json()["id"]

        # Update status
        update_data = {"status": "confirmed"}
        update_resp = requests.patch(
            f"{API_BASE}/orders/{order_id}/status",
            json=update_data,
            headers=self.headers,
            timeout=5,
        )
        assert update_resp.status_code == 200, f"Failed to update: {update_resp.text}"

        data = update_resp.json()
        assert data["status"] == "confirmed"


class TestReports:
    """Test reporting endpoints."""

    def setup_method(self):
        """Setup test data."""
        # Login as manager
        login_resp = requests.post(
            f"{API_BASE}/auth/login",
            json={"email": "manager@test.com", "password": "test123"},
            timeout=5,
        )
        assert login_resp.status_code == 200
        self.token = login_resp.json()["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def test_inventory_report_requires_manager(self):
        """Test inventory report requires manager+ role."""
        # Try with staff credentials
        staff_login = requests.post(
            f"{API_BASE}/auth/login",
            json={"email": "staff@test.com", "password": "test123"},
            timeout=5,
        )
        staff_token = staff_login.json()["token"]
        staff_headers = {"Authorization": f"Bearer {staff_token}"}

        response = requests.get(
            f"{API_BASE}/reports/inventory", headers=staff_headers, timeout=5
        )
        assert response.status_code == 403, "Staff should not access reports"

    def test_inventory_report_with_manager(self):
        """Test inventory report with manager credentials."""
        response = requests.get(
            f"{API_BASE}/reports/inventory", headers=self.headers, timeout=5
        )
        assert response.status_code == 200, f"Failed to get report: {response.text}"

        data = response.json()
        assert "total_items" in data
        assert "available_items" in data
        assert "sold_items" in data
        assert "reserved_items" in data
        assert "total_value" in data
        assert "by_category" in data
        assert "by_material" in data

    def test_sales_report_with_manager(self):
        """Test sales report with manager credentials."""
        response = requests.get(
            f"{API_BASE}/reports/sales", headers=self.headers, timeout=5
        )
        assert response.status_code == 200, f"Failed to get report: {response.text}"

        data = response.json()
        assert "total_orders" in data
        assert "completed_orders" in data
        assert "pending_orders" in data
        assert "total_revenue" in data
        assert "date_range" in data
        assert "top_selling_items" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])