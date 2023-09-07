from django.urls import path
from . import views


urlpatterns = [
    path('',views.CartList.as_view(),name='cart_list'),
    path('add/',views.CartAdd.as_view(),name='cart_add'),
    path('update/<int:id>/',views.CartUpdate.as_view(),name='cart_update'),
]