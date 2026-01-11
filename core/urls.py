from django.urls import path
from .views import test_prompt

urlpatterns = [
    path("", test_prompt, name="test_prompt"),
]
