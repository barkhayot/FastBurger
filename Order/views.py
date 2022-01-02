from django.shortcuts import render, redirect, get_object_or_404
from .models import testOrder, testOrderType
from .forms import OrderCompleteForm
from Meal.models import Food
from django.contrib.auth.decorators import login_required

def staff_board(request):
    return render(request, 'orders/staff_board.html')


@login_required(login_url='stuff_board')
def order_board(request):
    order = testOrder.objects.all().filter(status=0).order_by('-created_at')

    context = {
        'orders': order,
    }
    return render(request, 'orders/order_board.html', context)

@login_required(login_url='stuff_board')
def complete_order(request, pk):
    orderObj = get_object_or_404(testOrder, pk=pk)
    form = OrderCompleteForm()
    if request.method == 'POST':
        form = OrderCompleteForm(request.POST or None, instance=orderObj)
        if form.is_valid():
            form.save()
            return redirect('order_board')
    
    context = {
        'order': orderObj,
        'form': form
    }
    return render(request, 'orders/order_detail.html', context)

@login_required(login_url='stuff_board')
def completed_order_view(request):
    order = testOrder.objects.all().filter(status=1).order_by('-created_at')
    context = {
        'orders': order
    }
    return render(request, 'orders/completed_orders.html', context)

@login_required(login_url='stuff_board')
def order_list_view(request):
    order = testOrder.objects.all().order_by('-created_at')
    context = {
        'orders': order
    }
    return render(request, 'orders/list_view.html', context)