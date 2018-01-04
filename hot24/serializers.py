from rest_framework import serializers

from models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Users
        # fields = ('user_id', 'user_name', 'user_email', 'user_creation_dt','user_modify_dt','user_token')
        fields = ('user_id','user_name', 'user_email')
        #read_only_fields = ('date_created', 'date_modified')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Items
        fields = ('item_id','item_category', 'item_details', 'item_creation_dt','item_update_dt','item_priority','item_url','item_price')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category_id','category_name')


class LikedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedItems
        fields = ('user_id', 'item_id','creation_dt')



