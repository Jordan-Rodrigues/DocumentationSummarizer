from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import requests
import io
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


all_urls = ['https://literature.rockwellautomation.com/idc/groups/literature/documents/rn/1441-rn002_-en-p.pdf',
        'https://literature.rockwellautomation.com/idc/groups/literature/documents/in/800mr-in001_-en-e.pdf',
        'https://literature.rockwellautomation.com/idc/groups/literature/documents/td/1500-td220_-en-e.pdf']

url = 'https://literature.rockwellautomation.com/idc/groups/literature/documents/rn/1441-rn002_-en-p.pdf'
all_content = [] # List to hold strings from all pages in a PDF

##################FUNCTIONS####################################################
def get_text(url):

    r = requests.get(url) # Grab URL
    pdf_file = io.BytesIO(r.content) # Downloads PDF file as a byte stream (only in memory never saved locally)
    #pdf_file = open(file_name, 'rb') # Opens PDF file from directory
    read_pdf = PdfFileReader(pdf_file) # Reads in PDF
    number_of_pages = read_pdf.getNumPages() # Gets number of pages

    for pages in range(number_of_pages): # loops through all pages in PDF
        page = read_pdf.getPage(pages)
        page_content = page.extractText().replace('\n', " ") # Extracts text from current page & cleans up newlines
        all_content.append(page_content.encode('utf-8')) # Adds string of text from current page to list
    return number_of_pages, all_content

#This function will take in the word bytes from the PDF and convert it to a string and then split it off into a list of words
def convert_to_string(words):
    count = 0
    #Need to convert variable words from bytes to a string
    words = str(words)
    #Line 41: this will split the string even further into single words
    wordList = re.sub("[^\w]", " ", words).split() #This line of code was created by Username: Bryan; Founded on stackoverflow.com.
    return wordList

#Counts number of words are in the pdf
def size_of(words):
    count = 0
    for i in range(0, len(split_words)):
        count += 1
    return count

#A helper function that will be called upon when we want to remove specific stop words
#Parameters: Takes in list_words to take out all of the stop words needed
def word_stop(list_words):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(str(list_words))
    filtered_sentence = []
    removed_words = []
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
        else:
            removed_words.append(w)
    return filtered_sentence

#This function will take in words and print them to the console for testing purposes
#mostly
def to_string(printed_words):
    for i in range(0, len(printed_words)):
        print(printed_words[i]),


###############DRIVER###################
number_of_pages, all_words = get_text(url)
#Use a new list to hold all of the split words so we can later count how many words are actually there.
split_words = []
for i in range(0, len(all_words)):
    split_words += convert_to_string(all_words[i])

stopped_words = []
for i in range(0, len(all_words)):
    stopped_words.append(word_stop(all_words[i]))

to_string(stopped_words)
#print(all_words)
#prints the count at the end of iteration
#print(size_of(split_words))
