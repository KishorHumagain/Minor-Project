
from .import models
from .models import dbms

def gererate(request):
    qn_4=2
    qn_2=1
    question=models.dbms.objects.all()
    for i in question :
        print(i)
