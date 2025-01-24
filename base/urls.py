from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path("", views.home, name="home"),
    path('register_customer/',views.registerCustomer,name = 'register_customer'),
    path('register_owner/',views.registerOwner,name = 'register_owner'),
    path('register_deliverer/',views.registerDeliverer,name = 'register_deliverer'),
    path('role/',views.selectRole, name='role'),
    path("order/<str:pk>", views.order, name="order"),
    path("delete_order/<str:pk>/",views.deleteOrder, name = 'delete-order'),
    path("stats/", views.stats , name ='stats'),
    path("create-item/",views.createItem, name = 'create_item'),
    path('restaurants/',views.displayRestaurants, name='restaurant-list'),
    path('update_item/<str:pk>/', views.updateItem, name = 'update-item'),
    path('delete_item/<str:pk>/', views.deleteItem, name = 'delete-item'),
    path('order_view/<str:pk>/', views.viewOrder, name='order-view'),
    path('order_history/', views.orderHistory, name='order-history'),
    path('rating/<str:pk>/',views.rating, name='rating')
]
