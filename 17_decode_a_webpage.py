import requests
import lxml
from bs4 import BeautifulSoup as bsp

web_page_html = requests.get('https://www.nytimes.com/').text
web_page = bsp(web_page_html,'html5lib')
print(web_page[100])


print(web_page.find_all(class_ = 'balancedHeadline'))