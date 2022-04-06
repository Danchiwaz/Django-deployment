from django.urls import path
from . import views

urlpatterns = [
    path('',views.successPage, name="home_page"),
    path('registration/',views.registration, name="registration"),
    path('login/',views.login_user, name="login_page"),
    path('logout/',views.logout_user, name="logout_page"),
]