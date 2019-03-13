from django.urls import path, include
from users import views

urlpatterns = [
    path('submission', views.submission),
]
