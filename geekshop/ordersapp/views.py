from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from ordersapp.models import Order


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderCreate(CreateView):
    pass

class OrderUpdate(UpdateView):
    pass

class OrderDelete(DeleteView):
    pass

class OrderDetail(DetailView):
    pass

def order_forming_complete(request,pk):
    pass