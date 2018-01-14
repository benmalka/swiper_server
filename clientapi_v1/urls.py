from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^users$', views.users_list, name='users_list'),
        url(r'^add_user$', views.add_user, name='add_user'),
        url(r'^category$', views.category_list, name='category_list'),
        url(r'^items$', views.items_list, name='items_list'),
        url(r'^get_items$', views.get_items, name='get_items'),
        url(r'^like_item$', views.like_item, name='like_item'),
        url(r'^get_liked_items$', views.get_liked_items, name='get_liked_items'),
        url(r'^delete_liked_item$', views.delete_liked_item, name='delete_liked_item'),
]
