from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from administrador.models import ensaladas
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, ID_ensalada, precio_base, tamaño):
    cart = Cart(request)
    ensalada = get_object_or_404(ensaladas, ID_ensalada = ID_ensalada)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(ensalada=ensalada,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'],
                 precio_base = precio_base,
                 tamaño = tamaño)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, ID_ensalada):
    cart = Cart(request)
    product = get_object_or_404(ensaladas, ID_ensalada = ID_ensalada)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'carrito.html', {'cart': cart})