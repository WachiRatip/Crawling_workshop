import asyncio
from playwright.async_api import async_playwright

URL = "http://www.aws-observation.tmd.go.th/web/main/index.asp"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL)
        print(await page.title())
        page_content = await page.query_selector('#main_cityweather')
        res = await page.evaluate('(element) => element.textContent', page_content)
        print(res, type(res))
        await browser.close()

if __name__=="__main__":
    asyncio.run(main())