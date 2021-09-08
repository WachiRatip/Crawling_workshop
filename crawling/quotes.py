import asyncio

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

URL = "https://quotes.toscrape.com/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL)
        print(await page.title())
        html_content = await page.content()
        sup = BeautifulSoup(markup=html_content, features='lxml')
        data = sup.find(class_='text')
        print(data.contents)
        await browser.close()

if __name__=="__main__":
    asyncio.run(main())