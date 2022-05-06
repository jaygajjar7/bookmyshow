from django.urls import path
from .views import AboutView, HomeListView

app_name = "core"

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
]
