import PyPDF2

pdfFileObj = open('antican.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(2)
print(pageObj.extractText())