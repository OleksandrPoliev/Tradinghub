"""
    for next project in django i study web Scraping
    day 1(30.01.2022) install BS, read doc , write smale parser for job offer in nofluffjobs
    day 2 task : write for all main web page , understand how collect (data in model or sessions?) , CRUD
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def parser(datalist):
    req = Request(datalist[0], headers={'User-Agent': 'Mozilla/5.0 '})
    webpage = urlopen(req)
    html = webpage.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find_all(datalist[1])
    parserlist = [f'data from {datalist[3]}', ]
    for i in div:
        if datalist[3] == 'nofluffjobs':
            if "PYTHON" in str(i.text).upper():
                i = i.find_parent().find_parent().find_parent().find_parent()
                parserlist.append(f'{i.text}-{"https://nofluffjobs.com" + i.get("href")}')
        else:
            if "PYTHON" in str(i.text).upper():  # need any werbs to found
                parserlist.append(f'{i.text} - {f"""{datalist[2]}{i.get("href")}"""}')
    return parserlist


if __name__ == "__main__":

    data_for_pars = [
        ['https://www.glassdoor.com/Job/warsaw-junior-python-developer-jobs-SRCH_IL.0,6_IC3094484_KO7,30.htm?fromAge=3',
         'a', "https://www.glassdoor.com/", 'glassdoor'],
        ['https://pl.indeed.com/jobs?q=Python%20Developer&l=Warszawa%2C%20mazowieckie&fromage=1&vjk=02daaa34b78ba8e6',
         'a', "https://pl.indeed.com", 'indeed'],
        ['https://pl.jobsora.com/praca/warszawa/q-python-junior?interval=1', 'a', '', 'jobsora'],
        [
            'https://nofluffjobs.com/pl/praca-it/praca-zdalna/python?criteria=city%3Dwarszawa%20seniority%3Dtrainee,junior&page=1',
            'h3', 'https://nofluffjobs.com', 'nofluffjobs'],
        ["https://www.pracuj.pl/praca/junior%20python%20developer;kw", 'a', ' ', 'pracujpl'],
        ['https://pl.jooble.org/SearchResult?date=2&rgns=Warszawa&ukw=junior%20python', 'a', ' ', 'jooble']]
    for i in data_for_pars:
        print(parser(i))





# linkedin and  just join problem
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)
#
# url = "https://www.linkedin.com/jobs/search/?currentJobId=2896000776&f_TPR=r86400&geoId=91000002&keywords=junior%20python&location=%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%20%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B7%D0%BE%D0%BD%D0%B0&originalSubdomain=pl"
# driver.get(url)
# time.sleep(2)
# elements = driver.find_elements_by_class_name("result-card__full-card-link")
# print(elements)
# job_links = [e.get_attribute("href") for e in elements]
#
# for job_link in job_links:
#     print(job_link)

# req = Request(
#     'https://www.linkedin.com/jobs/search/?f_TPR=r86400&geoId=91000002&keywords=junior%20python&location=%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%20%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B7%D0%BE%D0%BD%D0%B0&originalSubdomain=pl',headers={'User-Agent':'Mozilla/5.0 '})
# webpage = urlopen(req)
# html = webpage.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# div = soup.find_all('div',class_="job-card-container relative job-card-list job-card-container--clickable job-card-list--underline-title-on-hover jobs-search-results-list__list-item--active jobs-search-two-pane__job-card-container--viewport-tracking-1")
# print(div)
# for i in div:
#     if True:# need any werbs to found
#         print(f'{i.text} - {i.get("href")}')
#
# req = Request(
#     'https://justjoin.it/all/python/junior',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 '})
# webpage = urlopen(req)
# html = webpage.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# div = soup.find_all()
# print(div)
