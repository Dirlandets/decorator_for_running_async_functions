# Decorator for running async functions
This decorator runs async function like sync function by running it in event loop. I created it when I start to use asyncio and aiohttp. And tryed to test it by unittest...

Examples:

```python
@with_loop
async def go_async(n: int) -> None:
    print(n)
    await asyncio.sleep(n)

go_async(10)
```

OR practical example:

```python
class TestFetcher(TestCase):
    @with_loop
    async def test_post(self):
        fetcher = await Fetch().post(BASE_URL)
        self.assertEqual(fetcher.method, 'POST')
```
