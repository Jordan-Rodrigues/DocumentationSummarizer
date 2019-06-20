from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import io
import requests

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
        page_content = page.extractText().replace('\n', '') # Extracts text from current page & cleans up newlines
        all_content.append(page_content.encode('utf-8')) # Adds string of text from current page to list

    return number_of_pages, all_content


number_of_pages, all_words = get_text(url)
