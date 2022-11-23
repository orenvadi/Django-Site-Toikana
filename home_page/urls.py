from django.urls import path

from . import views
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu/", views.show_menu, name="menu"),
    path("dish_detail/<int:id>/", views.find_by_id, name="dish"),
    path("news/", views.show_news, name="news"),
    path("contact/", views.show_contacts, name="contacts"),
]
