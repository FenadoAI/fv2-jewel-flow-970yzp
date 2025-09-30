# Jewellery Store Management System — API Contract

## Conventions
- Base URL: `/api`
- Auth: `Authorization: Bearer <JWT>` (required for all endpoints except public catalog and order placement)
- IDs: string UUID; Time: ISO 8601; Money: integer cents (USD)
- Errors: `{ "error": { "code": "STRING", "message": "STRING" } }`
- Pagination: `?page=1&limit=20`
- Role Hierarchy: `owner > manager > staff`

---

## Client Types (TypeScript)

```ts
export type UserRole = "staff" | "manager" | "owner";
export type ItemStatus = "available" | "sold" | "reserved";
export type OrderStatus = "pending" | "confirmed" | "delivered" | "cancelled";

export type User = {
  id: string;
  username: string;
  email: string;
  role: UserRole;
  created_at: string;
};

export type JewelleryItem = {
  id: string;
  item_code: string;        // Unique, mandatory
  name: string;
  description: string;
  category: string;         // e.g., "ring", "necklace", "bracelet"
  price: number;            // cents
  weight: number;           // grams
  material: string;         // e.g., "gold", "silver", "diamond"
  images: string[];         // Array of image URLs
  status: ItemStatus;
  created_at: string;
  updated_at: string;
};

export type OrderItem = {
  item_id: string;
  item_code: string;
  name: string;
  price: number;
  quantity: number;
  subtotal: number;
};

export type Order = {
  id: string;
  customer_name: string;
  customer_phone: string;
  customer_address: string;
  items: OrderItem[];
  total_amount: number;
  status: OrderStatus;
  payment_method: "COD";
  order_date: string;
  delivery_date?: string;
};

export type InventoryReport = {
  total_items: number;
  available_items: number;
  sold_items: number;
  reserved_items: number;
  total_value: number;       // cents
  by_category: Record<string, number>;
  by_material: Record<string, number>;
};

export type SalesReport = {
  total_orders: number;
  completed_orders: number;
  pending_orders: number;
  total_revenue: number;     // cents
  date_range: { start: string; end: string };
  top_selling_items: Array<{ item_code: string; name: string; quantity: number }>;
};
```

---

## 10 Core Endpoints (MVP)

### Authentication (2 endpoints)

**1. POST /auth/login** → 200
Req: `{ email: string, password: string }`
Res: `{ token: string, user: User }`
Notes: Returns JWT token valid for 24 hours

**2. GET /auth/me** → 200
Auth: Required
Res: `User`
Notes: Get current authenticated user details

---

### Inventory Management (3 endpoints)

**3. GET /inventory/items** → 200
Auth: Optional (public for catalog view, authenticated for full access)
Query: `?page=1&limit=20&category=string&material=string&status=available&search=string`
Res: `{ items: JewelleryItem[], page: number, total: number, has_more: boolean }`
Notes: Public users only see available items; authenticated users see all

**4. POST /inventory/items** → 201
Auth: Required (staff+)
Req: `{ item_code: string, name: string, description: string, category: string, price: number, weight: number, material: string, images?: string[] }`
Res: `JewelleryItem`
Validation: item_code must be unique

**5. PATCH /inventory/items/{id}** → 200
Auth: Required (staff+)
Req: Partial JewelleryItem (any field except id, created_at)
Res: `JewelleryItem`
Notes: Updates updated_at automatically

---

### Order Management (3 endpoints)

**6. POST /orders** → 201
Auth: Not required (public endpoint)
Req: `{ customer_name: string, customer_phone: string, customer_address: string, items: Array<{ item_id: string, quantity: number }> }`
Res: `Order`
Notes: Automatically sets payment_method to COD, validates item availability

**7. GET /orders** → 200
Auth: Required (staff+)
Query: `?page=1&limit=20&status=pending&customer_phone=string`
Res: `{ orders: Order[], page: number, total: number }`
Notes: Sorted by order_date descending

**8. PATCH /orders/{id}/status** → 200
Auth: Required (staff+)
Req: `{ status: OrderStatus, delivery_date?: string }`
Res: `Order`
Notes: Sets delivery_date when status changes to "delivered"

---

### Reporting (2 endpoints)

**9. GET /reports/inventory** → 200
Auth: Required (manager+)
Query: `?category=string&material=string`
Res: `InventoryReport`
Notes: Real-time inventory statistics

**10. GET /reports/sales** → 200
Auth: Required (manager+)
Query: `?start_date=ISO8601&end_date=ISO8601`
Res: `SalesReport`
Notes: Defaults to last 30 days if dates not provided

---

## User Flow

### Public Customer Flow
1. Browse catalog (GET /inventory/items?status=available)
2. View item details (GET /inventory/items with filter)
3. Place COD order (POST /orders)

### Staff Flow
1. Login (POST /auth/login)
2. View all orders (GET /orders)
3. Add new jewellery items (POST /inventory/items)
4. Update inventory (PATCH /inventory/items/{id})
5. Update order status (PATCH /orders/{id}/status)

### Manager/Owner Flow
1. Login (POST /auth/login)
2. All staff permissions
3. View inventory reports (GET /reports/inventory)
4. View sales reports (GET /reports/sales)

---

## Role-Based Access Control

| Endpoint | Owner | Manager | Staff | Public |
|----------|-------|---------|-------|--------|
| GET /inventory/items | Full | Full | Full | Available only |
| POST /inventory/items | ✓ | ✓ | ✓ | ✗ |
| PATCH /inventory/items/{id} | ✓ | ✓ | ✓ | ✗ |
| POST /orders | ✓ | ✓ | ✓ | ✓ |
| GET /orders | ✓ | ✓ | ✓ | ✗ |
| PATCH /orders/{id}/status | ✓ | ✓ | ✓ | ✗ |
| GET /reports/inventory | ✓ | ✓ | ✗ | ✗ |
| GET /reports/sales | ✓ | ✓ | ✗ | ✗ |

---

## Validation Rules

### JewelleryItem
- `item_code`: required, unique, alphanumeric, max 50 chars
- `name`: required, min 3 chars, max 200 chars
- `price`: required, integer >= 0
- `weight`: required, float > 0
- `category`: required, one of predefined categories
- `material`: required, string, max 100 chars
- `images`: optional, array of valid URLs
- `status`: required, one of: available, sold, reserved

### Order
- `customer_name`: required, min 2 chars, max 100 chars
- `customer_phone`: required, valid phone format
- `customer_address`: required, min 10 chars
- `items`: required, non-empty array
- `items[].quantity`: required, integer > 0
- Validation: All item_ids must exist and be available

### Reports
- `start_date`, `end_date`: valid ISO 8601 dates
- `end_date` must be after `start_date`
- Date range cannot exceed 1 year

---

## Error Codes

- `INVALID_CREDENTIALS` - Login failed
- `UNAUTHORIZED` - Missing or invalid token
- `FORBIDDEN` - Insufficient permissions
- `ITEM_CODE_EXISTS` - Duplicate item_code
- `ITEM_NOT_FOUND` - Item does not exist
- `ITEM_UNAVAILABLE` - Item not available for order
- `ORDER_NOT_FOUND` - Order does not exist
- `INVALID_STATUS_TRANSITION` - Invalid order status change
- `VALIDATION_ERROR` - Request validation failed

---

## Implementation Priority

### Phase 1 (MVP - Week 1)
1. Authentication endpoints (login, get current user)
2. Public catalog view (GET /inventory/items)
3. Add inventory (POST /inventory/items)
4. Place order (POST /orders)

### Phase 2 (Core Operations - Week 2)
5. Update inventory (PATCH /inventory/items/{id})
6. View orders (GET /orders)
7. Update order status (PATCH /orders/{id}/status)

### Phase 3 (Management - Week 3)
8. Inventory reports (GET /reports/inventory)
9. Sales reports (GET /reports/sales)
10. Advanced filtering and search

---

## Database Collections

### users
```json
{
  "_id": "uuid",
  "username": "string",
  "email": "string",
  "password_hash": "string",
  "role": "staff|manager|owner",
  "created_at": "ISO8601"
}
```
Index: `email` (unique)

### jewellery_items
```json
{
  "_id": "uuid",
  "item_code": "string",
  "name": "string",
  "description": "string",
  "category": "string",
  "price": 0,
  "weight": 0.0,
  "material": "string",
  "images": [],
  "status": "available",
  "created_at": "ISO8601",
  "updated_at": "ISO8601"
}
```
Indexes: `item_code` (unique), `status`, `category`, `material`

### orders
```json
{
  "_id": "uuid",
  "customer_name": "string",
  "customer_phone": "string",
  "customer_address": "string",
  "items": [
    {
      "item_id": "uuid",
      "item_code": "string",
      "name": "string",
      "price": 0,
      "quantity": 1,
      "subtotal": 0
    }
  ],
  "total_amount": 0,
  "status": "pending",
  "payment_method": "COD",
  "order_date": "ISO8601",
  "delivery_date": "ISO8601|null"
}
```
Indexes: `status`, `customer_phone`, `order_date`

---

## Non-Functional Requirements

- Response time: < 200ms for read operations, < 500ms for write operations
- Authentication: JWT tokens expire after 24 hours
- Pagination: Default 20 items per page, max 100
- Image uploads: Support via separate endpoint (future enhancement)
- Backup: Daily database backups
- Logging: Log all inventory and order changes with user attribution

---

## Future Enhancements (Not in MVP)

- User management endpoints (POST /users, PATCH /users/{id})
- Delete inventory items (soft delete)
- Order cancellation by customers
- Image upload endpoint (POST /inventory/items/{id}/images)
- Customer accounts and order history
- Payment gateway integration
- Inventory low-stock alerts
- Advanced search with full-text search
- Export reports as PDF/Excel