from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>",views.page, name="pages"),
    path("search", views.search, name="search"),
]
