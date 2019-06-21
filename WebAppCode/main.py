from flask import Flask, render_template, request, redirect, url_for
import requests
import time
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
app = Flask(__name__)

#Creating global variables that can be passed from page to page
global fulLURL
global PDFs
PDFs = []
fullURL = None


#Route for the main page, renders the home template
@app.route('/')
def home():
   return render_template("home.html")

@app.route('/',  methods=["POST", "GET"])
def searchGenerator():
    global fullURL
    global PDFs
    #used here for testing purposes, will be pulled from page in reality
    filterDictionary = {"service_ss": "Asset Management Services"}
    keyword = "voltage"
    
    fullURL = urlCreator(keyword, filterDictionary)
    #Delay before running the function to give the javascript of the page time to load in 
    time.sleep(3)
    
    #Creates an invisible browser (headless) to load the page manually (allows JS to render) and then pulls in all the relevant links
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome()
    browser.get(fullURL)
    tags = browser.find_elements_by_css_selector("div.literature.ra a")
    
    #for each tag pulled from the website, add the URL of that tag to the PDF list if it isn't none
    for tag in tags:
        if (tag.get_attribute("href") != None):
            PDFs.append(tag.get_attribute("href"))
    return redirect(url_for("results"))

@app.route('/Results')
def results():
    global PDFs
    
    #Limits the PDFs to the first 5 for readability purposes
    if len(PDFs) > 5:
        PDFs = PDFs[0:5]
    return render_template("result.html", PDFs=PDFs)


#-----------------------------------------FUNCTIONS--------------------------------
def urlCreator(keyword, filterDictionary):
    #First part of the URL
    urlStart = "https://www.rockwellautomation.com/search/ra_en_NA;keyword="
    #Browser automatically handles the rendering of keyword input
    #I want to be given a dictionary for the filters where the filter category is the key and all the entered filter types are the values
    filterSection = ""
    numCategories = len(filterDictionary)
    dictPosCounter = 0
    for filterCategory, filterTypeList in filterDictionary.items():
        #Creating a filter chucnk for each filter category, add them all together at end
        filterBody = ""
        counter = 0
        numFilters = len(filterTypeList)
        for filter in filterTypeList:
            #applying custom url codes derived from pattern analysis
            filter.replace(" ", "%2520")
            filter.replace("/", "%252F")
            #if you're on the last one, end it
            if (counter == numFilters - 1):
                filterBody += (filter + "%2552%2529")
                counter += 1
            #add an or statement and go on to the next
            else:
                filterBody += (filter + "%2522%2520OR%2520%2522")
                counter += 1
        if (dictPosCounter == 0):
            filterHeader = filterCategory + "%253A%2528%2522"
        else:
            filterHeader = "%253B" + filterCategory + "%253A%2528%2522"
        filterSection += (filterHeader + filterBody)
        dictPosCounter += 1
    finalURL = urlStart + keyword + ";activeTab=Literature;" + filterSection
    print(finalURL)
    return finalURL
        
        




