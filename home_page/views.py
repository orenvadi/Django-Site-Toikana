from django.shortcuts import render
from django.views.generic import TemplateView

# def homePageView(request):
#     return HttpResponse("hello mr Putin")


class HomePageView(TemplateView):  # просмотр начальной страницы
    template_name = "index.html"


class AboutPageView(TemplateView):  # просмотр страницы о проекте
    template_name = "about.html"
