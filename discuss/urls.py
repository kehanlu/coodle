from django.urls import path
from discuss import views

urlpatterns = [
    path('', views.list),
    path('<int:pid>', views.discuss),
    path('post', views.post),
    path('api/post', views.api_post),
    path('api/comment/<int:pid>', views.api_comment)
]
