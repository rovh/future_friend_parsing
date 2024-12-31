from flask import Flask
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


app = Flask(__name__)

@app.route('/')
def home():
    t = "0000000"
    t = run_parsing()

    return t

@app.route('/about')
def about():
    return 'About'



def run_parsing():


    text = "00000"

    try:
        serv=ChromeService(ChromeDriverManager().install())
        
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        browser = webdriver.Chrome(service=serv, options=chrome_options)
        # browser = webdriver.Chrome(service=Service())
        # browser.implicitly_wait(5)


        browser.get("https://www.google.com")
        text = ("Page title was '{}'".format(browser.title))
    finally:
        browser.quit()
        return text

