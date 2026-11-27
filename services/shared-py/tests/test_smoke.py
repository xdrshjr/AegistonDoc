import asyncio

import shared_py


def test_shared_py_import() -> None:
    assert shared_py.hello() == "Hello from shared-py!"


async def test_asyncio_auto_mode() -> None:
    assert await asyncio.sleep(0, result=True)
