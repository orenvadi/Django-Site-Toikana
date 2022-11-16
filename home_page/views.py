from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import TemplateView

from . import models


# def homePageView(request):
#     return HttpResponse("hello mr Putin")
def show_all(request):
    menu = models.Menu.objects.all()
    return render(request, "menu.html", {"menu": menu})


def show_home_page(request):
    news = models.News.objects.all()
    # context={'news':news}
    return render(request, "index.html", {"news": news})


# def show_news(request):
#     news=models.News.objects.all().values()
#     template=loader.get_template('index.html')
#     context={
#         'news':news,
#     }
#     return HttpResponse(template.render(context,request))
# получение одного блюда
def find_by_id(request, id):
    dish = get_object_or_404(models.Menu, id=id)
    return render(request, "dish_detail.html", {"dish": dish})


def show_contacts(request):
    contacts = models.Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


class HomePageView(TemplateView):  # просмотр начальной страницы
    model = models.News
    template_name = "index.html"


class AboutPageView(TemplateView):  # просмотр страницы о проекте
    template_name = "about.html"
