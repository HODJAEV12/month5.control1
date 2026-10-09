from django.urls import path
from .views import ChecksListView, ChecksDetailView

urlpatterns = [
    path('checks/', ChecksListView.as_view(), name='categories'),
    path('checks/<int:pk>/', ChecksDetailView.as_view(), name='category-detail'),
]