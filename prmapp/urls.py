from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('admins',views.admins,name="admin"),
    path('products',views.products,name="products"),
    path('vilakku',views.vilakku,name="vilakku"),
    path('arathi',views.arathi,name="arathi"),
    path('statue',views.statue,name="statue"),
    path('para',views.para,name="para"),
    path('chain',views.chain,name="chain"),
    path('gift',views.gift,name="gift"),
    path('house',views.house,name="house"),
    path('medal',views.medal,name="medal"),
    path('bell',views.bell,name="bell"),
    path('music',views.music,name="music"),
    path('photo',views.photo,name="photo"),
    path('all',views.all,name="all"),
    path('plate',views.plate,name="plate"),
    path('polish',views.polish,name="polish"),
    path('vasthu',views.vasthu,name="vasthu"),
    path('pooja',views.pooja,name="pooja"),
    path('stand',views.stand,name="stand"),
    path('temple',views.temple,name="temple"),
    path('utensils',views.utensils,name="utensils"),
    path('shop',views.shop,name="shop"),
    path('login',views.login,name="login"),
    path('reg',views.reg,name="reg"),

    path('^update(?P<idd>\w+)',views.update,name="update"),
    path('delete(?P<idd>\w+)',views.delete,name="delete"),

]
