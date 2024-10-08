# from playwright.sync_api import sync_playwright
# from selectolax.parser import HTMLParser

from util.extractHtml import getHtml
from util.extractRating import getRating
import re

if __name__ == '__main__':
    flipUrl = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    
    flipHtml = getHtml(pageUrl=flipUrl)
    allLp = flipHtml.css('div.tUxRFH > a > div.row')
    
    i= 0
    
    for lp in allLp:
        i = i + 1
        title = lp.css_first('div.KzDlHZ').text()
        rating = getRating(lp.css_first('div.XQDdHH'))
        offerPrice = lp.css_first('div.Nx9bqj').text()
        
        new_offerPrice = float(re.sub(r'[₹,]', '',offerPrice ))
        
        currentPrice = lp.css_first('div.yRaY8j').text()
        
        new_currentPrice = float(re.sub(r'[₹,]', '',currentPrice ))
        
        discount_percent = lp.css_first('div.UkUFwK').text()
        
        
        lpInfo = [info.text() for info in lp.css('ul.G4BRas > li') ]
        
        lpDetails = {
            'title': title,
            'rating': rating,
            'lpInfo': lpInfo,
            'offerPrice': new_offerPrice,
            'currentPrice': new_currentPrice,
            'discount_percent': discount_percent
            
        }
        print(f'{i}. lpDetails {lpDetails}')
        print('------------------------------------------------------------------------------------------------')

        


# if __name__ == '__main__':
#     with sync_playwright() as p:
#         browser= p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
#         page.wait_for_timeout(5000)
#         page.screenshot(path="flip.png" , full_page= True)
#         htmlContent = page.inner_html('body')
        
#         flipHtml = HTMLParser(htmlContent)
        
#         lp1 = flipHtml.css_first('div.KzDlHZ').text()
        
#         print('lp1 = ' , lp1)