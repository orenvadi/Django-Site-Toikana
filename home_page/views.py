from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from . import models
from .forms import AddBooking, AddReview
from .models import Branch, Chef, Menu, News,Review,Booking


# Output of menu
def show_menu(request):
    menu = models.Menu.objects.all()
    return render(request, "menu.html", {"menu": menu})


# Filtering the menu by first courses
def first_course(request):
    dish = Menu.objects.filter(menu="First courses")
    return render(request, "menu_type.html", {"dish": dish})


# Filtering the menu by second courses
def second_course(request):
    dish = Menu.objects.filter(menu="Second courses")
    return render(request, "menu_type.html", {"dish": dish})


# Filtering the menu by desserts
def desserts(request):
    dish = Menu.objects.filter(menu="Desserts")
    return render(request, "menu_type.html", {"dish": dish})


# Filtering the menu by wine
def wine(request):
    dish = Menu.objects.filter(menu="Wine Map")
    return render(request, "menu_type.html", {"dish": dish})


# Filtering the menu by drinks
def drinks(request):
    dish = Menu.objects.filter(menu="Drinks")
    return render(request, "menu_type.html", {"dish": dish})


# Output of news
def show_news(request):
    news = models.News.objects.all()
    return render(request, "about.html", {"news": news})


# Get one dish by id
def find_by_id(request, id):
    dish = get_object_or_404(models.Menu, id=id)
    return render(request, "dish_detail.html", {"dish": dish})


# Output of contacts
def show_contacts(request):
    contacts = models.Contact.objects.all()
    return render(request, "contact.html", {"contacts": contacts})


# Output of all information listed on the main page
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


# Leave review
class AddBooking(CreateView):
    form_class = AddBooking
    template_name = "booking.html"
    success_url = "/"


# Add branches
class BranchCreateView(CreateView):  # new
    model = Branch
    template_name = "add_new.html"
    success_url = "/"
    fields = ["name", "description", "image"]


# Update branch by id
class BranchUpdateView(UpdateView):
    model = models.Branch
    template_name = "update.html"
    fields = "__all__"
    success_url = "/"


# Delete branch by id
class BranchDeleteView(DeleteView):  # new
    model = models.Branch
    template_name = "confirm_delete.html"
    success_url = "/"


# Leave review
class AddReview(CreateView):
    form_class = AddReview
    template_name = "about.html"
    success_url = "/"


# Add dish
class MenuCreateView(CreateView):  # new
    model = Menu
    template_name = "add_new.html"
    success_url = "/"
    fields = "__all__"


# Update dish by id method
class MenuUpdateView(UpdateView):
    model = models.Menu
    template_name = "update.html"
    fields = "__all__"
    success_url = "/"


# Delete dish by id method
class MenuDeleteView(DeleteView):  # new
    model = models.Menu
    template_name = "confirm_delete.html"
    success_url = "/"


# Update chef by id method
class ChefUpdateView(UpdateView):
    model = models.Chef
    template_name = "update.html"
    fields = "__all__"
    success_url = "/"


# Delete chef by id method
class ChefDeleteView(DeleteView):  # new
    model = models.Chef
    template_name = "confirm_delete.html"
    success_url = "/"


# Add chefs
class ChefCreateView(CreateView):  # new
    model = Chef
    template_name = "add_new.html"
    success_url = "/"
    fields = ["name", "description", "image"]


# Update news by id method
class NewsUpdateView(UpdateView):
    model = models.News
    template_name = "update.html"
    fields = "__all__"
    success_url = "/"


# Delete news by id method
class NewsDeleteView(DeleteView):  # new
    model = models.News
    template_name = "confirm_delete.html"
    success_url = "/"


# Add news
class NewsCreateView(CreateView):  # new
    model = News
    template_name = "add_new.html"
    success_url = "/"
    fields = "__all__"

class ReviewView(ListView): 
    model = Review
    context_object_name = "review_list"
    template_name = "view_reviews.html"

class BookingView(ListView): 
    model = Booking
    context_object_name = "booking_list"
    template_name = "view_booking.html"