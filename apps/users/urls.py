from django.urls import path, include
from . import views

urlpatterns = [
    path('me/', views.UserView.as_view()),
    path('register/', views.newUserView.as_view()),
    path('sign_in/', views.signUserView.as_view()),

]
