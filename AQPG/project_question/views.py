from django.shortcuts import render
from django.http import HttpResponse
from . import models




from fpdf import FPDF

import random
from random import randint

from django.core.files import File

import io
import re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from .models import dbms

import questionpattern



# # Create your views here.           
def home(request):
    return render(request, 'home.html')
   # return HttpResponse('hello')

'''def scan_pdf(request):
    # miner_text_generator.py
# import io
# import re
# from pdfminer.converter import TextConverter
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfpage import PDFPage
# from .models import DBMS
    def extract_text_by_page(pdf_path):
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh, 
                                        caching=True,
                                        check_extractable=True):
                resource_manager = PDFResourceManager()
                fake_file_handle = io.StringIO()
                converter = TextConverter(resource_manager, fake_file_handle)
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(page)
            
                text = fake_file_handle.getvalue()
                yield text
    
            # close open handles
                converter.close()
                fake_file_handle.close()

    def extract_text(pdf_path):
        for page in extract_text_by_page(pdf_path):
            print(page)
    
        split_text=page.split("]")
    # print(split_text)
        x = len(split_text)
        for i in range(0,x):
            mlist = split_text[i]
            pattern = re.compile(r'(\d{1,3})\)\s+([A-Za-z0-9.,;\"\s?]+)\s+\[(\d{1,2})\s*')
            matches = pattern.finditer(mlist)
            for match in matches:
            #print(match.group(3))
                qn = match.group(2)
                marks= match.group(3)

                if (marks==2):
                    object=DBMS(questions=qn)
           # Question.objects.create(qn = Ques, mark = marking)
        
        
        with open('test.txt','w') as f:
            f.write(page)
        #print()
        

    text=extract_text("test.pdf")


    # context = {
    #     'questions': q
    #  }
    # return render(request, "aqpgapp/generated.html" , context = context)

'''

# def getdata(request):
#     questionss=models.dbms.objects.all()
#     q=[i for i in questionss]
#     qn_4 = 2
#     qn_2 = 2
#     global grpA=[]
#     global grpB=[]
#     qn=random.shuffle(q)
#     for i in q:
#         if i.marks==2 and qn_2>0:
#             grpA.append(i.questions)
#             qn_2 -=1
#         if i.marks==4 and qn_4>0:
#             grpB.append(i.questions)
#             qn_4 -=1
        

#     context = {
#             'questionShort': grpA,
#             'questionLong': grpB
#         }
#     return render(request, "generated.html",context)



def data(grpA,grpB):
    questionss=models.dbms.objects.all()
    q=[i for i in questionss]
    qn_4 = 2
    qn_2 = 2
    grpA=[]
    grpB=[]
    qn=random.shuffle(q)
    for i in q:
        if i.marks==2 and qn_2>0:
            grpA.append(i.questions)
            qn_2 -=1
        if i.marks==4 and qn_4>0:
            grpB.append(i.questions)
            qn_4 -=1
    return (grpA,grpB) 








def generate_view(request):
    qn_4 = 2
    qn_2 = 1
    questions = models.dbms.objects.all()

    
    # for i in questions:
    #     print(i)
    q = [i for i in questions]
    print(q)
    random.shuffle(q)

    # for qs in q:
    #     print(qs.questions)


    #print(q)

    
    
    # for i in q:
    #     if int(i.marks) == 4 & qn_4 > 0 :
    #         fin.append(i)
    #         qn_4 -= 1
    #     elif int(i.marks) == 2 & qn_2 > 0 :
    #         fin.append(i)
    #         qn_2 -= 1
    #     else:
    #         pass
    for qs in q:
        if int(qs.marks)==4 & qn_4 > 0 :
            with open('paper.txt','a') as f:
                f.write(qs.questions)
                qn_4 -= 1
        elif int(qs.marks)==2 & qn_2 > 0 :
            with open('paper.txt','a') as f:
                f.write(qs.questions)
                qn_2 -= 1
        else:
            pass
        

    

    #print(fin)
    

    context = {
        'questions': qs.objects.all()
    }
    return render(request, "generated.html" , context)

def text_pdf(request):
    text=models.dbms.objects.all()
    context = {
        'text': text} 

    with open("questions.txt",'w') as q:
        q.write(text)
    
    
    
    
    
    # pdf=FPDF()
    # pdf.add_page()
    # pdf.set_font("Times",size=20)
    # file=open("C:\\Users\\KISHOR\\Desktop\\operating_sys_question.txt",'r')
    # for i in file:
    #     pdf.cell(100,10,txt=i,ln=1,align='c')

    # pdf.output("sample.pdf")
    # return render(request, context)

    

def pdf_text(request):
    def extract_text_by_page(pdf_path):
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh, 
                                        caching=True,
                                        check_extractable=True):
                resource_manager = PDFResourceManager()
                fake_file_handle = io.StringIO()
                converter = TextConverter(resource_manager, fake_file_handle)
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(page)
                
                text = fake_file_handle.getvalue()
                yield text
        
                # close open handles
                converter.close()
                fake_file_handle.close()

    def extract_text(pdf_path):
        for page in extract_text_by_page(pdf_path):
            print(page)
        
        split_text=page.split("]")
        # print(split_text)
        x = len(split_text)
        for i in range(0,x):
            mlist = split_text[i]
            pattern = re.compile(r'(\d{1,3})\)\s+([A-Za-z0-9.,;\"\s?]+)\s+\[(\d{1,2})\s*')
            matches = pattern.finditer(mlist)
            for match in matches:
                #print(match.group(3))
                qn = match.group(2)
                marks= match.group(3)
                if (marks==2):
                    obj=dbms(questions=qn)
            # Question.objects.create(qn = Ques, mark = marking)
            
            
        with open('test.txt','w') as f:
            f.write(page)
            #print()
            

    text=extract_text("test.pdf")

    return render(request,"scan.html")


    
