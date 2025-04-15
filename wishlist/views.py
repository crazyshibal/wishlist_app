from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Wishlist, WishlistItem
from .forms import WishlistForm, WishlistItemForm
from django.contrib import messages

class WishlistListView(ListView):
    model = Wishlist
    template_name = 'wishlist/home.html'
    context_object_name = 'wishlists'
    ordering = ['-created_at']
    paginate_by = 5

class WishlistDetailView(DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist_detail.html'

class WishlistCreateView(CreateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'

class WishlistUpdateView(UpdateView):
    model = Wishlist
    form_class = WishlistForm
    template_name = 'wishlist/wishlist_form.html'

class WishlistDeleteView(DeleteView):
    model = Wishlist
    template_name = 'wishlist/wishlist_confirm_delete.html'
    success_url = '/'

def wishlist_item_create(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)
    if request.method == 'POST':
        form = WishlistItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.wishlist = wishlist
            item.save()
            messages.success(request, 'Item added to your wishlist!')
            return redirect('wishlist-detail', pk=wishlist.pk)
    else:
        form = WishlistItemForm()
    return render(request, 'wishlist/wishlistitem_form.html', {'form': form, 'wishlist': wishlist})

def wishlist_item_update(request, pk, item_pk):
    item = get_object_or_404(WishlistItem, pk=item_pk)
    if request.method == 'POST':
        form = WishlistItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('wishlist-detail', pk=item.wishlist.pk)
    else:
        form = WishlistItemForm(instance=item)
    return render(request, 'wishlist/wishlistitem_form.html', {'form': form, 'wishlist': item.wishlist})

def wishlist_item_delete(request, pk, item_pk):
    item = get_object_or_404(WishlistItem, pk=item_pk)
    if request.method == 'POST':
        wishlist_pk = item.wishlist.pk
        item.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('wishlist-detail', pk=wishlist_pk)
    return render(request, 'wishlist/wishlistitem_confirm_delete.html', {'item': item})