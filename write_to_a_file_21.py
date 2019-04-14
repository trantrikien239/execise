import requests
from bs4 import BeautifulSoup as bsp

web_page_html = requests.get('https://www.worldstandards.eu/other/tlds/').text
web_page = bsp(web_page_html,'lxml')


# print(web_page.find_all(class_ = 'table table-striped'))
table = web_page.find_all(class_ = 'table table-striped')[0]
print(type(table))
print(len(web_page.find_all(class_ = 'table table-striped')))
list_data = table.find_all('td')
with open('./data/country_domain.csv',mode='w+') as file:
    for index, item in enumerate(list_data):
        if index % 2 == 0:
            file.write(item.text + ', ')
        else:
            file.write(item.text + '\n')

web_page_eu_countries = bsp(requests.get('https://www.countries-ofthe-world.com/countries-of-europe.html').text,'lxml')
data_area = web_page_eu_countries.find(class_ = 'container list-container')
data_list = data_area.find_all('li')
with open('./data/eu_countries.csv', mode = 'w+') as file_eu_countries:
    for item in data_list:
        if item.text not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            file_eu_countries.write(item.text + '\n')