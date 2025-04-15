from django.urls import path
from . import views
from .views import (
    WishlistListView,
    WishlistDetailView,
    WishlistCreateView,
    WishlistUpdateView,
    WishlistDeleteView,
)

urlpatterns = [
    path('', WishlistListView.as_view(), name='wishlist-home'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/new/', WishlistCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:pk>/update/', WishlistUpdateView.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', WishlistDeleteView.as_view(), name='wishlist-delete'),
    path('wishlist/<int:pk>/item/new/', views.wishlist_item_create, name='wishlist-item-create'),
    path('wishlist/<int:pk>/item/<int:item_pk>/update/', views.wishlist_item_update, name='wishlist-item-update'),
    path('wishlist/<int:pk>/item/<int:item_pk>/delete/', views.wishlist_item_delete, name='wishlist-item-delete'),
]