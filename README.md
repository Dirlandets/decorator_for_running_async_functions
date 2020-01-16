# Decorator for ruuning async functions
This decorator runs async def like simple def by running it in loop. 
I created it when I start to use asyncio and aiohttp.

It's nice for simple tests like:

```python
@with_loop
async def go_async(arg):
    print(arg)
    await asyncio.sleep(arg)

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
