from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os


def collect_cards_list(url):
	driver = webdriver.PhantomJS("./phantomjs")
	driver.get(url)
	html = driver.page_source
	source = BeautifulSoup(html, "html.parser")
	print(source)


print("URL: ", end='')
url = input()
url = url.replace(" ", "")
collect_cards_list(url)
