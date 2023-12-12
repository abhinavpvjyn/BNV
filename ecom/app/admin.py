from django.contrib import admin
from . models import Cart, Product,Customer, Wishlist

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_img']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','state','zipcode']
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
    
@admin.register(Wishlist)
class WhislistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']