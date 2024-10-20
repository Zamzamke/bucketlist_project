from django.urls import path
from .views import BucketListCreateView, BucketListDetailView,RegisterUser

urlpatterns = [
    path('bucketlists/', BucketListCreateView.as_view(), name='bucketlist-create'),
    path('bucketlists/<int:pk>/', BucketListDetailView.as_view(), name='bucketlist-detail'),
    path('register/', RegisterUser.as_view(), name='register'),  
]
