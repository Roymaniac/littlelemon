from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'),
    re_path(r'^bookings_api/(?P<date>\d{4}-\d{2}-\d{2})/$',
            views.bookings_query, name="bookings_query"),
]
