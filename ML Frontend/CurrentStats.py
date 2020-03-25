# This Program gives Current stats of conoravirus cases and death by fetching it from government website

from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def getData(url):
    r = requests.get(url)  # gives the html data
    return r.text  # returns in text format


def currentStatus():
    myHtmlData = getData("https://www.mohfw.gov.in/")

#     print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, "html.parser")
#     print(soup.prettify())

    # gets only the table from whole html page
    myDataStr = ""
    for tr in soup.find_all("tbody")[7].find_all("tr"):
        myDataStr += tr.get_text()

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n")

    # print(itemList)
    tempList = int(itemList[-11]) + int(itemList[-9]
                                        ), int(itemList[-6]), int(itemList[-3])
    # print(tempList)

    return tempList


if __name__ == '__main__':
    # currentStatus()
    pass
