import PyPDF2
pdf = PyPDF2.PdfFileReader("David.pdf")
#print(pdf.documentInfo)
#print(pdf.getNumPages())
str = " "
for i in range(1,41):
    str += pdf.getPage(i).extractText()
with open("pdf.txt" , "w" , encoding="utf-8") as f:
    f.write(str)