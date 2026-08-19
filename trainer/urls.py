from django.urls import path
from . import views

app_name = "trainer"

urlpatterns = [
    path("", views.home, name="home"),
    path("estudiar/", views.study, name="study"),
    path("sobre-el-mazo/", views.about, name="about"),
    path("api/cards/", views.cards_api, name="cards_api"),
    path("api/meta/", views.meta_api, name="meta_api"),
]
