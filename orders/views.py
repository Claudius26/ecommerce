from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cart.cart import Cart
from orders.models import Order, OrderItem


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )

    cart.clear()
    return render(request, 'orders/order_created.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created-at')
    return render(request, 'orders/order_history.html', {'orders': orders})
# Create your views here.
