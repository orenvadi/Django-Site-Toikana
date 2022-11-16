from django.urls import path

from .views import AboutPageView, HomePageView
from . import views


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('menu/', views.show_all, name='menu'),
    path('dish_detail/<int:id>/', views.find_by_id, name='dish'),
    path('news/',views.show_news, name='news'),
    path('contact/',views.show_contacts,name='contacts'),
]
