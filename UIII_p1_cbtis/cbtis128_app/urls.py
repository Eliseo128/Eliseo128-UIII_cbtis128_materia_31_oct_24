from django.urls import path
from cbtis128_app import views
urlpatterns = [
    path('',views.inicio_vista,name='inicio_vista')
]
