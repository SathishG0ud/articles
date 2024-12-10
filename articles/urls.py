from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('articles_full_details/<int:pk>',views.gen_article,name='gen_article'),
    path('about',views.about,name='about'),
]