import asyncio
from os import fsync
import pytest
import store.db.mongo 
import db_client 


@pytest.fixture(scope="session")
def event_loop():
    """Force the pytest loop to be the main one."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mongo_client():
    return db_client.get()

@pytest.fixture(autouse=True)
async def clear_collection():
    yield
    collection_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue
        await mongo_client.get_database()[collection_name].delete_many()
    