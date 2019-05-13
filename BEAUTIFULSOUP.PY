import requests
import  parse
import urllib.error
from bs4 import BeautifulSoup
import json


url = 'https://www.jumia.com.ng/oud-touch-for-men-100ml-frank-olivier-mpg73251.html#ratingReviews'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


product_json = {}
# This block of code will help extract the Brand of the item
for article in soup.findAll('article', attrs={'class': 'card-desktop -ratingReview'}):
    try:
        product_json['brand'] = article['data-brand']
        
        break
    except:
        pass
# This block of code will help extract the Prodcut Title of the item
for div1 in soup.findAll('div', attrs={'class': 'title'}):
    name_of_product = div1.text.strip()
    product_json['name'] = name_of_product
    break

# This block of code will help extract the average star rating of the product
for div2 in soup.findAll('div', attrs={'class': 'rating-stars'}):
    for div3 in div2.findAll('div', attrs={'class': 'stars-container'}):
        product_json['star-rating'] = div3.text.strip()
        break
# This block of code will help extract the number of customer reviews of the product
for div4 in soup.findAll('div', attrs={'class': 'detail truncate-txt'}):
    if div4.text:
        review_count = div4.text.strip()
        product_json['customer-reviews-count'] = review_count
        break


# Saving the scraped data in json format
with open('product.json', 'w') as outfile:
    json.dump(product_json, outfile, indent=4)
print('----------Extraction of data is complete. Check json file.----------')


		
	
