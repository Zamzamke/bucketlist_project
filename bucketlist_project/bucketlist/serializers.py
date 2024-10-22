from rest_framework import serializers
from .models import BucketList,BucketListItem
from django.contrib.auth.models import User


# Handle serialization for the user
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
#To handle serialization for bucket list Items
class BucketListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketListItem
        fields = ['id', 'title', 'description', 'category', 'priority', 'status', 'bucketlist']

 #Handle serialization for bucket lists
class BucketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    items = BucketListItemSerializer(many=True, read_only=True)

    class Meta:
        model = BucketList
        fields = ['id', 'name', 'owner', 'items']