"""Seed database with test users for jewellery store."""

import asyncio
import os
import sys
from datetime import datetime, timezone

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

sys.path.insert(0, os.path.dirname(__file__))
from auth import hash_password

load_dotenv()


async def seed_users():
    """Seed database with test users."""
    mongo_url = os.getenv("MONGO_URL")
    db_name = os.getenv("DB_NAME")

    if not mongo_url or not db_name:
        print("Error: MONGO_URL and DB_NAME must be set in .env")
        return

    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]

    # Test users
    users = [
        {
            "_id": "owner-001",
            "username": "owner",
            "email": "owner@test.com",
            "password_hash": hash_password("test123"),
            "role": "owner",
            "created_at": datetime.now(timezone.utc),
        },
        {
            "_id": "manager-001",
            "username": "manager",
            "email": "manager@test.com",
            "password_hash": hash_password("test123"),
            "role": "manager",
            "created_at": datetime.now(timezone.utc),
        },
        {
            "_id": "staff-001",
            "username": "staff",
            "email": "staff@test.com",
            "password_hash": hash_password("test123"),
            "role": "staff",
            "created_at": datetime.now(timezone.utc),
        },
    ]

    # Insert users (replace if exists)
    for user in users:
        await db.users.replace_one({"_id": user["_id"]}, user, upsert=True)
        print(f"Created user: {user['email']} (role: {user['role']})")

    # Create indexes
    await db.users.create_index("email", unique=True)
    await db.jewellery_items.create_index("item_code", unique=True)
    await db.jewellery_items.create_index("status")
    await db.jewellery_items.create_index("category")
    await db.jewellery_items.create_index("material")
    await db.orders.create_index("status")
    await db.orders.create_index("customer_phone")
    await db.orders.create_index("order_date")

    print("\nDatabase seeded successfully!")
    print("\nTest credentials:")
    print("  Owner:   owner@test.com / test123")
    print("  Manager: manager@test.com / test123")
    print("  Staff:   staff@test.com / test123")

    client.close()


if __name__ == "__main__":
    asyncio.run(seed_users())