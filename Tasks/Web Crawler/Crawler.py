import sys
import re
import urllib.request
import json
from bs4 import BeautifulSoup


URL_RESULT_COUNT = "http://www.shopping.com/products?KW={0}"
URL_RESULTS = "http://www.shopping.com/products~PG-{1}?KW={0}"


# returns total number of results for a given keyword
def result_count(keyword):
    response = __query(URL_RESULT_COUNT.format(keyword))
    count = re.search('NumItemsReturned:(\d+)', response).group(1)
    return count


# returns all found results for a given keywords on a specified page
def find_results(keyword, page_number):
    response = __query(URL_RESULTS.format(keyword, page_number))

    soup = BeautifulSoup(response, 'html.parser')

    # gets the result container in html DOM
    searchResultsContainer = soup.find('div', {"id": "searchResultsContainer"})

    # gets all the <a> tags which contains the result
    tagNames = searchResultsContainer.find_all('a', {"class": "productName"})

    # iterates all the tagNames and gets the product name
    result = []
    for tagName in tagNames:
        try:
            strName = (tagName['title'])
        except Exception as e:
            try:
                strName = (tagName.find('span')['title'])
                result.append(strName)
            except Exception as e:
                pass
            pass
    return result


# returns the response from a url
def __query(url):
    return urllib.request.urlopen(url).read().decode('utf-8')
