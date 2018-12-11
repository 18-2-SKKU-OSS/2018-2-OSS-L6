from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os


def save_card_image(card_image_src):
	print("Save \"" + card_image_src + "\"")
	image_name = card_image_src.split("/")[-1]
	image_data = requests.get(card_image_src, stream=True)
	with open(image_name, "wb") as img_file:
		img_file.write(image_data.content)


def collect_cards_list(url):
	driver = webdriver.PhantomJS("../phantomjs")
	driver.get(url)
	html = driver.page_source
	source = BeautifulSoup(html, "html.parser")

	cards_section = source.find("div", {"id": "RevealedCards"})
	cards_image = cards_section.find_all("img")

	for card_image in cards_image:
		card_image_src = card_image.get("data-src")
		save_card_image(card_image_src)


print("Card list URL: ", end='')
url = input()
url = url.replace(" ", "")
if not os.path.exists("./" + "card_image" + "/"):
	os.mkdir("card_image")
os.chdir("card_image")
collect_cards_list(url)
