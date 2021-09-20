from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('todo_details',views.detail,name="detail"),
]
