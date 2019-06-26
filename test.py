from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import requests
import io
import nltk
import re



all_urls = ['https://literature.rockwellautomation.com/idc/groups/literature/documents/rn/1441-rn002_-en-p.pdf',
        'https://literature.rockwellautomation.com/idc/groups/literature/documents/in/800mr-in001_-en-e.pdf',
        'https://literature.rockwellautomation.com/idc/groups/literature/documents/td/1500-td220_-en-e.pdf']

url = 'https://literature.rockwellautomation.com/idc/groups/literature/documents/rn/1441-rn002_-en-p.pdf'
all_content = [] # List to hold strings from all pages in a PDF


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
    words = str(words)
    print(type(words))
    #Line 41: this will split the string even further into single words
    wordList = re.sub("[^\w]", " ", words).split() #This line of code was created by Username: Bryan; Founded on stackoverflow.com.
    return wordList


number_of_pages, all_words = get_text(url)

#Use a new list to hold all of the split words so we can later count how many words are actually there.
split_words = []
for i in range(0, len(all_words)):
    split_words += convert_to_string(all_words[i])


#Counts number of words are in the pdf
count = 0
for i in range(0, len(split_words)):
    count += 1
#prints the count at the end of iteration
print(count)
