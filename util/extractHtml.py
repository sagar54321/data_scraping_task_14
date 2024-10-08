from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


def getHtml(pageUrl):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(pageUrl)
        
        page.wait_for_timeout(5000)
        page.screenshot(path='flip1.png',full_page=True)
        
        pageContent = page.inner_html('body')
        
        pageHtml = HTMLParser(pageContent)
        
        return pageHtml