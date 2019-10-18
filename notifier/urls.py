from django.contrib import admin
from django.urls import path

from notifier.views import NotifierBaseView

urlpatterns = [
    path('', NotifierBaseView.as_view()),
]