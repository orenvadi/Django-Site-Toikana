from django.urls import path

from . import views
from .views import (AddBooking, AddReview, BranchCreateView, BranchDeleteView,
                    BranchUpdateView, ChefDeleteView, ChefUpdateView,
                    HomePageView, MenuCreateView, MenuDeleteView,
                    MenuUpdateView, NewsCreateView, NewsDeleteView,
                    NewsUpdateView,ReviewView,BookingView,GalleryView)

# app_name='home_page'
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu/", views.show_menu, name="menu"),
    path("dish_detail/<int:id>/", views.find_by_id, name="dish"),
    path("news/", views.show_news, name="news"),
    path("contact/", views.show_contacts, name="contacts"),
    path("delete/<int:pk>", BranchDeleteView.as_view(), name="delete"),
    path("deletedish/<int:pk>", MenuDeleteView.as_view(), name="deletedish"),
    path("deletechef/<int:pk>", ChefDeleteView.as_view(), name="deletechef"),
    path("deletenews/<int:pk>", NewsDeleteView.as_view(), name="deletenews"),
    path("update/<int:pk>", views.BranchUpdateView.as_view(), name="update"),
    path("updatedish/<int:pk>", views.MenuUpdateView.as_view(), name="updatedish"),
    path("updatechef/<int:pk>", views.ChefUpdateView.as_view(), name="updatechef"),
    path("updatenews/<int:pk>", views.NewsUpdateView.as_view(), name="updatenews"),
    path("addchef", views.ChefCreateView.as_view(), name="addchef"),
    path("addbranch", views.BranchCreateView.as_view(), name="addbranch"),
    path("addmenu", views.MenuCreateView.as_view(), name="addmenu"),
    path("addnews", views.NewsCreateView.as_view(), name="addnews"),
    path("leave_review/", AddReview.as_view(), name="review"),
    path("leave_booking/", AddBooking.as_view(), name="booking"),
    path("first/", views.first_course, name="first"),
    path("second/", views.second_course, name="second"),
    path("desserts/", views.desserts, name="desserts"),
    path("wine/", views.wine, name="wine"),
    path("drinks/", views.drinks, name="drinks"),
    path("review_view/",ReviewView.as_view(),name="viewreview"),
    path("booking_view/",BookingView.as_view(),name="viewbooking"),
    path("gallery_view/",GalleryView.as_view(),name="gallery"),


]
