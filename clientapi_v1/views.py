from django.shortcuts import render

# Create your views here.
from pip._vendor.cachecontrol import serialize

from rest_framework import generics
import hashlib

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Categories, Items, Admins, Users, LikedItems
from serializers import CategorySerializer, ItemSerializer, UsersSerializer, LikedItemsSerializer

PAGINATION = 10
EMPTY_DICT = {}


def isUserExist(uname):
    return Users.objects.get(user_name=uname) != None


@api_view(['GET', 'POST'])
def users_list(request):
    """
    List all users, or create a new task.
    """
    if request.method == 'GET':
        if 'user_name' in request.GET.keys():
            user = Users.objects.get(user_name=request.GET['user_name'])
            serializer = UsersSerializer(user, many=False)
            res = Response(serializer.data)
        else:
            res = Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)

        # users = Users.objects.all()
        #
        # serializer = UsersSerializer(users, many=True)
        return res

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_user(request):
    # TODO:
    return Response(EMPTY_DICT, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def items_list(request):
    if request.method == 'Post' and 'user_name' in request.data.keys():
        if Users.object.get(user_name=request.data['user_name']):
            data = request.data['data']
            cObj = Categories.objects.get(category_name=data['item_category'])
            if cObj:
                data['item_category'] = cObj.id
                serializer = ItemSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # neet to eliminate this GET request
    if request.method == 'GET':
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_items(request):
    if request == 'POST' and 'user_name' in request.data.keys() and 'data' in request.data.keys() and 'maxPrice' in \
            request.data['data'].keys():
        if Users.object.get(user_name=request.data['user_name']):
            # partion_index
            data = request.data['data']
            PI = data['page'] if 'page' in data.keys() else 0
            # TODO: check page validation
            items = Items.objects.filter(item_price__lte=data['maxPrice']).order_by('-item_update_dt')[
                    PI * PAGINATION:(PI + 1) * PAGINATION]
            serializer = ItemSerializer(data=items, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
    return Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def category_list(request):
    """
    :GET get all main categories
    :POST add new category
    :param request:
    :return: Response obj
    """
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST' and 'user_name' in request.data.keys() and 'data' in request.data.keys():
        user = Users.objects.get(user_name=request.data['user_name'])
        data = request.data['data']
        if user and 'category_name' in data.keys():
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
def like_item(request):
    if request.method == 'POST' and 'user_name' in request.data.keys() and 'data' in request.data.keys():
        user = Users.objects.get(user_name=request.data['user_name'])
        item = Items.objects.get(item_id=request.data['data'])
        if user and item:
            # if isUserExist(user_name=request.data['user_name']):
            data = {}
            data['user_id'] = user.user_id
            data['item_id'] = item.item_id
            serializer = LikedItemsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE' and 'user_name' in request.data.keys() and 'data' in request.data.keys():
        user = Users.objects.get(user_name=request.data['user_name'])
        item = Items.objects.get(item_id=request.data['data'])
        if user and item:
            try:
                LikedItems.objects.get(user_id=user.user_id, item_id=item.item_id).delete()
                return Response(EMPTY_DICT, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                print e
                pass
    return Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_liked_items(request):
    if request.method == 'POST' and 'user_name' in request.data.keys() and 'data' in request.data.keys():
        user = Users.objects.get(user_name=request.data['user_name'])
        if user:
            PI = request.data['page'] if 'page' in request.data.keys() else 0
            likeditems = LikedItems.objects.filter(user.id).order_by('-creation_dt')[
                         PI * PAGINATION:(PI + 1) * PAGINATION]
            data = {'items': []}
            for item in likeditems:
                data['items'].append(Items.objects.get(item_id=item.item_id))
            return Response(data, status=status.HTTP_200_OK)
    return Response(EMPTY_DICT, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_liked_item(request):
    # TODO:
    return Response(EMPTY_DICT, status=status.HTTP_200_OK)