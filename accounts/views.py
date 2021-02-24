from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .form import OrderForm
from .form import ProductForm
from .form import CustomerForm
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_order = orders.count()
    total_customer = customers.count()
    pending = orders.filter(status="Pending").count()
    delivered = orders.filter(status="Delivered").count()
    contex = {"customers":customers,'orders':orders,'total_order':total_order,'pending':pending,'delivered':delivered}
    return render(request,'accounts/dashboard.html',contex)

def products(request):
    products = Product.objects.all()    
    return render(request,"accounts/product.html",{'products':products})    


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')    
    contex={'form':form}    
    return render(request,"accounts/product_form.html",contex)

def updateProduct(request):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customer/' + str(order.customer.id))

    context =  {'action':action, 'form':form}    
    return render(request,"accounts/product_form.html",contex)


def deleteProduct(request):
    return render(request,"accounts/product_form.html")    


def customer(request):
    customers = Customer.objects.all()    
    contex={'customers':customers}
    return render(request,"accounts/customer.html",contex)  

def customerDetail(request,pk_test):
    customerDetail = Customer.objects.get(id=pk_test)
    orders = customerDetail.order_set.all()
    total_order = orders.count()
    contex= {'customerDetail':customerDetail,'orders':orders,'total_order':total_order}
    return render(request,"accounts/single_customer.html",contex)

def createCustomer(request):
    form=CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers')
    contex={'form':form}        
    return render(request,'accounts/customer_form.html',contex)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form =  CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/customers/')

    context =  {'form':form}
    return render(request, 'accounts/customer_form.html', context)



def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    contex={'form':form}
    return render(request,'accounts/order_form.html',contex)




#-------------------(UPDATE VIEWS) -------------------

def updateOrder(request, pk):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customers/' + str(order.customer.id))

    context =  {'action':action, 'form':form}
    return render(request, 'accounts/order_form.html', context)

#-------------------(DELETE VIEWS) -------------------

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        customer_id = order.customer.id
        customer_url = '/customer/' + str(order.customer.id)
        order.delete()
        return redirect(customer_url)
        
    return render(request, 'accounts/delete_item.html', {'item':order})    