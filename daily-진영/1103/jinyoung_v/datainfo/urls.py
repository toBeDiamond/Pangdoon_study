from django.urls import path
from . import views


urlpatterns = [
    path('function_a/', views.function_A),
    path('function_b/', views.function_B),
    path('function_c/', views.function_C),
    path('function_c/test/normal_sort/', views.function_C),
]
