from django.urls import path


from . import views

urlpatterns=[
    path('',views.home,name='home'),
    
    path('create_customer/',views.createCustomer,name='create_customer'),
    path('customers/',views.customer,name='customer'),
    path('update_customer/<str:pk>/',views.updateCustomer,name='update_customer'),
    path('customer_details/<str:pk_test>',views.customerDetail,name='customerDetail'),

    #-------------- products--------------------
    path('products/',views.products,name='products'),
    path('create_product/',views.createProduct,name='create_product'),
    path('update_product/<str:pk>/',views.updateProduct,name='update_product'),
    path('delete_product/<str:pk>/',views.deleteProduct,name='delete_product'),
    

    path('create_order/',views.createOrder,name='create_order'),

    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),    
]

