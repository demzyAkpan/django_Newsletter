from django.urls import path
from . import views

urlpatterns = [
    path('subscriber/', views.SubcriptionPage.as_view(), name='subscriber_page'),
    path('newsletter/', views.CreateNewsletter.as_view(),name='send'),
]