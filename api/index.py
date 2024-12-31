from flask import Flask
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By



app = Flask(__name__)

@app.route('/')
def home():
    t = "0000000"
    t = run_parsing()

    return 'Hello, World!' + t

@app.route('/about')
def about():
    return 'About'



def run_parsing():

    text = "00000"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)
    try:
        browser.get("https://www.google.com")
        text = ("Page title was '{}'".format(browser.title))
    finally:
        browser.quit()

    return text