#!/usr/bin/env python3
import aiosqlite
import asyncio

# ✅ Asynchronous function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        print("All Users:", users)
        return users

# ✅ Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        users = await cursor.fetchall()
        await cursor.close()
        print("Users older than 40:", users)
        return users

# ✅ Main coroutine to run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# ✅ Run the concurrent function
asyncio.run(fetch_concurrently())
