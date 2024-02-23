
from django.urls import path
from . import views


urlpatterns = [
   
   path ('',views.registration, name='registration'),
   path ('userlogin/',views.user_login, name='userlogin'),
   path ('profile/',views.profile, name='profile'),
   path ('userlogout/',views.user_logout, name='userlogout'),
   path ('passchange/',views.change_password, name='passchange'),
]