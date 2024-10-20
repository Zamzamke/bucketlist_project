from rest_framework import generics,permissions
from .models import BucketList
from .serializers import BucketListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

class BucketListCreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Save the owner as the authenticated user

    def get_queryset(self):
        return BucketList.objects.filter(owner=self.request.user)  # Return only the user's bucket lists

class BucketListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BucketList.objects.filter(owner=self.request.user)  # Only allow access to the user's bucket list

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
