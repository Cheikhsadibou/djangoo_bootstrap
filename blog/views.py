from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import UserInput
from .forms import InputForm
from blog.models import DetailCar
from django.core.paginator import Paginator

def about_us(request):
   return render(request, 'contact_about/about_me.html', {})

def contact_us(request):
   return render(request, 'contact_about/contact.html', {})

def update_car(request, article_id):
   articl = UserInput.objects.get(pk=article_id)
   form = InputForm(request.POST or None, instance=articl)
   if form.is_valid():
      form.save()
      return redirect('liste-article')
   
   return render(request, 'create_update/change_article.html', {'articl': articl, 'form':form})

def show_article(request, article_id):
   articl = UserInput.objects.get(pk=article_id)
   return render(request, 'create_update/show_article.html', {'articl': articl})

def liste_article(request):
   InputListe = UserInput.objects.all()
   context = {
      "InputListe": InputListe,
   }
   return render(request, 'create_update/update_Article.html', context)

def create_article(request):
   entry= False
   if request.method == "POST":
      form = InputForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/Create_article?entry=true')
   else:
      form = InputForm
      if 'entry' in request.GET:
         entry = True
   return render(request, 'create_update/Create_Article.html', {'form':form, 'entry':entry})


def handler404(request, exeption):
   return render(request, "404.html", status=404)


def Home(request):
   return render(request, 'home.html', {})
  

def blog(request):

   blog = DetailCar.objects.all()
   p = Paginator(DetailCar.objects.all(), 6)
   page = request.GET.get('page')
   page_obj = p.get_page(page)
   nbr = "a" * page_obj.paginator.num_pages
   context = {
      "blog": blog,
      "page_obj" : page_obj,
      "nbr" : nbr
   }
   return render(request, 'Blogs/blog.html',context )

def list_detail(request):
   Detail = DetailCar.objects.all()
   pg = Paginator(DetailCar.objects.all(), 2)
   page = request.GET.get('page')
   page_detail = pg.get_page(page)
   nbrs = "n" * page_detail.paginator.num_pages
   context = {
      "Detail": Detail,
      "page_detail": page_detail,
      "nbrs": nbrs      
   }
   return render(request, 'Blogs/list_detail.html', context)
