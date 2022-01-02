from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from Order.models import testOrder
from .forms import OrderFoodForm

# Food menu view
def food_menu(request):
    food = Food.objects.all().filter(category=1)
    drink = Food.objects.all().filter(category=2)
    side = Food.objects.all().filter(category=3)
    
    context = {
        'foods': food,
        'drinks': drink,
        'sides' : side,
    }
    return render(request, 'food/food_menu.html', context)

# Food detail view
def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    form = OrderFoodForm()
    if request.method == 'POST':
        form = OrderFoodForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.food = food
            order.price = food.food_price * order.count
            order.save()
            return redirect('order_complete', pk=order.pk)
    
    context = {
        'food': food,
        'form': form
    }
    return render(request, 'food/food_detail.html', context)

# Order Complete view
def order_complete(request, pk):
    order = get_object_or_404(testOrder, pk=pk)
    total_price = order.count * order.food.food_price
    
    context = {
        'order' : order,
        'total_price' : total_price
    }
    return render(request, 'food/order_complete.html', context)

