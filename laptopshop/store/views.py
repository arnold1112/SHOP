from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Laptop
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect




def home(request):
    laptops = Laptop.objects.all()
    return render(request, 'store/home.html', {'laptops': laptops})


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'store/laptop_detail.html', {'laptop': laptop})

def home(request):
    category_id = request.GET.get('category')
    if category_id:
        laptops = Laptop.objects.filter(category_id=category_id)
    else:
        laptops = Laptop.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'laptops': laptops, 'categories': categories})


@login_required
def add_to_cart(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)
    item, created = CartItem.objects.get_or_create(user=request.user, laptop=laptop)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    related_laptops = Laptop.objects.filter(category=laptop.category).exclude(id=laptop.id)[:4]
    return render(request, 'store/laptop_detail.html', {
        'laptop': laptop,
        'related_laptops': related_laptops
    })



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def call_center(request):
    return render(request, 'store/call_center.html')

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def cart(request, laptop_id):
    laptop = get_object_or_404(Laptop, pk=laptop_id)
    return render(request, 'store/cart.html', {'laptop': laptop})