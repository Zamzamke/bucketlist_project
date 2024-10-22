from django.urls import path
from .views import (BucketListCreateView, BucketListDetailView, AddItemToBucketList,UpdateBucketListItem,DeleteBucketListItem, GetItemsFromBucketList,)

urlpatterns = [
    path('bucketlists/', BucketListCreateView.as_view(), name='bucketlist-create'),
    path('bucketlists/<int:pk>/', BucketListDetailView.as_view(), name='bucketlist-detail'),
    path('bucketlists/<int:id>/items/', AddItemToBucketList.as_view(), name='add-item'),
    path('bucketlists/<int:id>/items/<int:item_id>/', UpdateBucketListItem.as_view(), name='update-item'),
    path('bucketlists/<int:id>/items/<int:item_id>/delete/', DeleteBucketListItem.as_view(), name='delete-item'),
    path('bucketlists/<int:id>/items/', GetItemsFromBucketList.as_view(), name='get-items'),
]
