import aiohttp
import asyncio
import async_timeout
class Async_con:
    def __init__(self):
        self.loop=asyncio.get_event_loop()
    @classmethod
    async def fetch_page(cls,url, session):
    # gets the url
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                # get url content after it loads
                return await response.text()
    async def get_multiple_pages(self, *urls):
        tasks = []
        async with aiohttp.ClientSession(loop=self.loop) as session:
            for url in urls:
                tasks.append(Async_con.fetch_page(url, session))
            grouped_tasks = asyncio.gather(*tasks)
            return await grouped_tasks