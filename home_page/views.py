from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import TemplateView,ListView

from . import models


# def homePageView(request):
#     return HttpResponse("hello mr Putin")
def show_all(request):
    menu = models.Menu.objects.all()
    return render(request, "menu.html", {"menu": menu})


def show_home_page(request):
    news = models.News.objects.all()
    menu= models.Menu.objects.all()
    print(news)    # context={'news':news}
    return render(request, "index.html", {"news": news,"menu":menu})


def show_news(request):
    news=models.News.objects.all()
    return render(request, "news.html",{ "news":news })
# получение одного блюда
def find_by_id(request, id):
    dish = get_object_or_404(models.Menu, id=id)
    return render(request, "dish_detail.html", {"dish": dish})


def show_contacts(request):
    contacts = models.Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


class HomePageView(ListView):  # просмотр начальной страницы
    model = models.News
    context_object_name = 'news_list'
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            'menu_list': models.Menu.objects.order_by('title'),
        })
        return context


class AboutPageView(TemplateView):  # просмотр страницы о проекте
    template_name = "about.html"
