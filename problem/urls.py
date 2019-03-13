from django.urls import path, include
from problem import views

urlpatterns = [
    path('', views.problem_list),
    path('<int:pid>', views.problem),
    path('submission/<int:pid>', views.submission),
    path('api/submit/<int:pid>', views.api_submit),
    path('api/submission/<int:sid>', views.api_submission),
]
