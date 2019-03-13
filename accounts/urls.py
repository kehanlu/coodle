from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('allauth.socialaccount.providers.google.urls')),
    path('login/', views.login_view, name='account_login'),
    path('logout/', views.logout_view, name='account_logout'),
]
