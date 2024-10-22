from rest_framework import generics,permissions, status
from .models import BucketList, BucketListItem
from .serializers import BucketListSerializer,BucketListItemSerializer ,#UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

#To create a new bucketlist and list all bucketlists
class BucketListCreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Save the owner as the authenticated user

    def get_queryset(self):
        return BucketList.objects.filter(owner=self.request.user)  # Return only the user's bucket lists

#to retrieve, update, or delete a specific bucket list.
class BucketListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BucketList.objects.filter(owner=self.request.user)  # Only allow access to the user's bucket list

#Handle user registration
#class RegisterUser(APIView):
    #def post(self, request, *args, **kwargs):
       # serializer = UserSerializer(data=request.data)
       # if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add an item to a specific bucket list
class AddItemToBucketList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            bucketlist = BucketList.objects.get(id=id, owner=request.user)
        except BucketList.DoesNotExist:
            return Response({'error': 'BucketList not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BucketListItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(bucketlist=bucketlist)  # Save the item with the related bucket list
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update an item in the bucket list
class UpdateBucketListItem(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id, item_id):
        try:
            bucketlist = BucketList.objects.get(id=id, owner=request.user)
            item = BucketListItem.objects.get(id=item_id, bucketlist=bucketlist)
        except (BucketList.DoesNotExist, BucketListItem.DoesNotExist):
            return Response({'error': 'Item or BucketList not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BucketListItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete an item from the bucket list
class DeleteBucketListItem(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, id, item_id):
        try:
            bucketlist = BucketList.objects.get(id=id, owner=request.user)
            item = BucketListItem.objects.get(id=item_id, bucketlist=bucketlist)
        except (BucketList.DoesNotExist, BucketListItem.DoesNotExist):
            return Response({'error': 'Item or BucketList not found'}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Get all items from a specific bucket list (with filters)
class GetItemsFromBucketList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        try:
            bucketlist = BucketList.objects.get(id=id, owner=request.user)
        except BucketList.DoesNotExist:
            return Response({'error': 'BucketList not found'}, status=status.HTTP_404_NOT_FOUND)

        items = bucketlist.bucketlistitem_set.all()  # Get all items related to the bucket list

        # Filtering based on query parameters
        category = request.query_params.get('category')
        priority = request.query_params.get('priority')
        status = request.query_params.get('status')

        if category:
            items = items.filter(category=category)
        if priority:
            items = items.filter(priority=priority)
        if status:
            items = items.filter(status=status)

        serializer = BucketListItemSerializer(items, many=True)
        return Response(serializer.data)