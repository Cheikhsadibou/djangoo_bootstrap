"""bootstrap_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from DataUsers.views import Creer_Article, Suprimer_Article, contact, A_propos
# from django.contrib.auth.views import Create_article
from blog.views import create_article, liste_article, show_article, update_car, contact_us, about_us
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'blog.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('DataUsers.urls')), 
    # path('blog/', blog,name='Page_blog'),
    # path('Détail article/', list_detail,name='Page_Detail'), 
    # path('blog/', include("blog.urls")),
    path('', include("blog.urls")),
    path('Create_article/',create_article , name='Creer_Article'),
    path('liste_article/',liste_article , name='liste-article'),
    path('show_article/<article_id>',show_article , name='show-article'),
    path('contact/',contact_us , name='contact-us'),
    path('about/',about_us , name='about-us'),
    # path('show_article/edit/<article_id>',update_car , name='update-car'),
    path('update_car/<article_id>',update_car , name='update-car')
    # path('Creer_Article/', Creer_Article,name='Creer_Article'),
    # path('Suprimer_Article/', Suprimer_Article,name='Suprimer_Article'),
    # path('contact/', contact,name='Page_contact'), 
    # path('A_propos/', A_propos,name='Page_propos'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
