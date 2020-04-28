from django.contrib import admin
from django.urls import path, include
from .views import DonateCreateView, Index, DonateListView, DonateDetailView, VerificationView, ValidView

app_name = "donate"
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('list/<str:category>/<str:search>',
         DonateListView.as_view(), name="list"),
    path('list/<slug:category>',
         DonateListView.as_view(), name="list"),
    path('detail/<slug:slug>', DonateDetailView.as_view(), name="detail"),
    path('verify/', VerificationView.as_view(), name="verify"),
    path('valid/', ValidView.as_view(), name="valid"),
    path('create/<int:pk>', DonateCreateView.as_view(), name="create"),
]
