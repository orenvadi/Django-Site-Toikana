from django.urls import path

from . import views
from .views import BranchDeleteView, BranchUpdateView, HomePageView

# app_name='home_page'
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu/", views.show_menu, name="menu"),
    path("dish_detail/<int:id>/", views.find_by_id, name="dish"),
    path("news/", views.show_news, name="news"),
    path("contact/", views.show_contacts, name="contacts"),
    path("delete/<int:pk>", BranchDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", views.BranchUpdateView.as_view(), name="update"),
    path("signupp/", views.show_signup, name="signupp"),
]
