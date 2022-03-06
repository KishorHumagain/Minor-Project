
from django.urls import path
from . import views 
from django.contrib import admin



admin.site.site_header=' College Admin Page'
admin.site.site_title='Welcome to Admin Panel'
urlpatterns = [

path ('',views.home,name='home'),
#path('scan_pdf',views.scan_pdf,name='scan')
path('generate_view' , views.generate_view, name="genetated"),
path('text_to_pdf',views.text_pdf,name="pdf"),
path('getdata',views.getdata,name="getdata"),
path('scan',views.pdf_text,name='pdf_text'),

]