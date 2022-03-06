from django.contrib import admin
from django.urls import path
from . import views, ocrinsingleline
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns =[

    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout,name = 'logout'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('scan',ocrinsingleline.extract_text_by_page,name='extract_text_by_page'),
    path('downloadfromhere',views.downloadfromhere, name = 'downloadfromhere')

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)