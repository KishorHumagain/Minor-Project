

from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Times",size=20)
file=open("E:\Minor Project\Output.txt",'r')
for i in file:
    pdf.cell(100,10,txt=i,ln=1,align='c')

pdf.output("sample.pdf")