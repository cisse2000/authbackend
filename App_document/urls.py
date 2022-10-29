from django.urls import path
from .views import DocumentAPIView

urlpatterns = [
    path('crud/', DocumentAPIView.as_view(), name='file')
]