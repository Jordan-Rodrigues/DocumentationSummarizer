import PyPDF2
import re
pdf_file = open('test.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
for i in range(0,number_of_pages):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    words = page_content
    re.sub("\n","", words)
    print(words) 