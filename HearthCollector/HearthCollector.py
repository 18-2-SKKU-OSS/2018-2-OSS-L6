from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os


def collect_cards_list(url):
	print(url)


print("URL: ", end='')
url = input()
url = url.replace(" ", "")
collect_cards_list(url)
