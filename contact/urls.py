from site import venv
from django.urls import path
from . import views
from django.core.paginator import Paginator
app_name='contact'
urlpatterns = [
    path('',views.send_massege,name='contact'),
]
