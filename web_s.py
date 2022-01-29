"""
    for next project in django i study web Scraping
    day 1(30.01.2022) install BS, read doc , write smale parser for job offer in nofluffjobs
    day 2 task : write for all main web page , understand how collect (data in model or sessions?) , CRUD
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request(
    'https://nofluffjobs.com/pl/praca-it/praca-zdalna/python?criteria=city%3Dwarszawa%20seniority%3Dtrainee,junior&page=1')
webpage = urlopen(req)
html = webpage.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
div = soup.find_all('h3')
for i in div:
    if "PYTHON" in str(i.text).upper():# need any werbs to found
        i = i.find_parent().find_parent().find_parent().find_parent()
        print(f'{i.text}-{"https://nofluffjobs.com" + i.get("href")}')






