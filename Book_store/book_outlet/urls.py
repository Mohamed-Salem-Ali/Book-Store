from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name='book_list'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail')
]
 