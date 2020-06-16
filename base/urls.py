from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="base-home"),
    path("about/", views.about, name="base-about"),
    path("contact/", views.contact, name="base-contact"),
    path("login/", views.login, name="base-login"),
    path("blogs/", views.blog, name="blog-all_blogs"),
]
