from django.urls import path
from . import views
# from blog.views import blog, list_detail

urlpatterns = [
    path('', views.Home, name="HomePage"),
    path('BlogPage/', views.blog, name="BlogPage"),
    path('list_detail/', views.list_detail,name='list_detail'),
    path('Add_CreateArticle' , views.create_article, name = "Add-CreateArticle"), 
]
