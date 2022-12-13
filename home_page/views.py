from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from . import models
from .forms import AddReview


def show_signup(request):
    return render(request, "signUp.html")


def show_menu(request):
    menu = models.Menu.objects.all()
    return render(request, "menu.html", {"menu": menu})


def show_news(request):
    news = models.News.objects.all()
    return render(request, "about.html", {"news": news})


# получение одного блюда
def find_by_id(request, id):
    dish = get_object_or_404(models.Menu, id=id)
    return render(request, "dish_detail.html", {"dish": dish})


def show_contacts(request):
    contacts = models.Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


class HomePageView(ListView):  # просмотр начальной страницы
    model = models.News
    context_object_name = "news_list"
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context["review_list"] = models.Review.objects.all()
        context["menu_list"] = models.Menu.objects.all()
        context["branch_list"] = models.Branch.objects.all()
        context["chef_list"] = models.Chef.objects.all()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context.update(
    #         {
    #             "menu_list": models.Menu.objects.order_by("title"),
    #             "branch_list": models.Branch.objects.all(),
    #             "chef_list": models.Chef.objects.all(),
    #             "review_list": models.Review.objects.all(),
    #         }
    #     )
    #     return context


# Update method
class BranchUpdateView(UpdateView):
    model = models.Branch
    template_name = "update.html"
    fields = "__all__"
    success_url = "/"


class BranchDeleteView(DeleteView):  # new
    model = models.Branch
    template_name = "confirm_delete.html"
    success_url = "index.html"


# Leave review
class AddReview(CreateView):
    form_class = AddReview
    template_name = "contact.html"
    success_url = "/"
