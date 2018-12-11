from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os


def collect_cards_list(url):
	driver = webdriver.PhantomJS("../phantomjs")
	driver.get(url)
	html = driver.page_source
	source = BeautifulSoup(html, "html.parser")

	cards_section = source.find("div", {"id": "RevealedCards"})
	cards_image = cards_section.find_all("img")

	for card_image in cards_image:
		card_image_src = card_image.get("data-src")
		print(card_image_src)


print("Card list URL: ", end='')
url = input()
url = url.replace(" ", "")
if not os.path.exists("./" + "card_image" + "/"):
	os.mkdir("card_image")
os.chdir("card_image")
collect_cards_list(url)
