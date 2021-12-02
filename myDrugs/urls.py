from django.urls import path
from .views import indexPageView, searchPageView, detailsPageView

urlpatterns = [
    path("search/", searchPageView, name="search"),
    path("details/", detailsPageView, name="details"),
    path("", indexPageView, name="index"),
]