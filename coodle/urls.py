from django.contrib import admin
from django.urls import path, include
from coodle import views

urlpatterns = [
    path('', views.index),
    path('user/', include('users.urls')),
    path('discuss/', include('discuss.urls')),
    path('problem/', include('problem.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
