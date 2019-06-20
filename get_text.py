import PyPDF2

file_name = 'example.pdf'
all_words = [] # List to hold strings from all pages in a PDF

def get_text():

    pdf_file = open(file_name, 'rb') # Opens PDF file
    read_pdf = PyPDF2.PdfFileReader(pdf_file) # Reads in PDF
    number_of_pages = read_pdf.getNumPages() # Gets number of pages

    for pages in range(number_of_pages): # loops through all pages in PDF
        page = read_pdf.getPage(pages)
        page_content = page.extractText() # Extracts text from current page
        all_words.append(page_content.encode('utf-8')) # Adds string of text from current page to list

    return number_of_pages, all_words


number_of_pages, all_words = get_text()
