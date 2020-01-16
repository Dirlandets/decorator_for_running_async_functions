import asyncio
from functools import wraps

def with_loop(f):
    @wraps(f)
    def inner(*args, **kwargs):
        wrapped_coro = f(*args, **kwargs)
        if wraped_coro is not None:
            loop = asyncio.get_event_loop()
            task = asyncio.ensure_future(wraped_coro)
            try:
                loop.run_until_complete(task)
            except BaseException:
                if task.done() and not task.cancelled():
                    task.exception()
                raise
            finally:
                # extra loop iteration for actual closing.
                loop.run_until_complete(asyncio.sleep(0))
    return inner
