from django.shortcuts import render
from django.http import HttpResponse
from . import models
from random import randint
import random

import io
import re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from .models import DBMS



# # Create your views here.
def home(request):
    return render(request, 'home.html')
    return HttpResponse('hello')

def scan_pdf(request):
    # miner_text_generator.py
# import io
# import re
# from pdfminer.converter import TextConverter
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfpage import PDFPage
# from .models import DBMS







# def generate_view(request):
#     qn_4 = 2
#     qn_2 = 1
#     questions = models.Question.objects.all()

    
#     for i in questions:
#         print(i)
#     q = [i for i in questions]
#     print(q)
#     random.shuffle(q)


#     #print(q)

    
#     fin = []
#     for i in q:
#         if int(i.mark) == 4 & qn_4 > 0 :
#             fin.append(i)
#             qn_4 -= 1
#         elif int(i.mark) == 2 & qn_2 > 0 :
#             fin.append(i)
#             qn_2 -= 1
#         else:
#             pass

    

#     #print(fin)
    

#     context = {
#         'questions': q
#     }
#     return render(request, "aqpgapp/generated.html" , context = context)