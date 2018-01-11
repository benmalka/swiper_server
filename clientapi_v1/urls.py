from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^users/$', views.users_list, name='users_list'),
        url(r'^category/$', views.category_list, name='category_list'),
        url(r'^items/$', views.items_list, name='items_list'),
        url(r'^like_items/$', views.items_list, name='items_list'),
]
