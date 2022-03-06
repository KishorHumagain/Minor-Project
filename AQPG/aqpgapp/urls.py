
from django.urls import path
from . import views 




urlpatterns = [

path ('',views.home,name='home'),
#path('generated' , views.generate_view, name="genetated")


]