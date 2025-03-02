from django.urls import path
from myapp import (views)

app_name = 'myapp'
urlpatterns = [
    # URL pattern for the index view (e.g., http://localhost:8000/myapp/)
    path(r'', views.index, name='index'),
    # URL pattern for the about view (e.g., http://localhost:8000/myapp/about/)
    path('about/', views.about, name='about'),
    # URL pattern for the detail view using a named group for the category number
    # (e.g., http://localhost:8000/myapp/3/ for category with id=3)
    path('<int:cat_no>/', views.detail, name='detail'),
]