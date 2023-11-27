from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.forms import LoginForm
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home),
    path('category/<slug:value>',views.CategoryView.as_view(),name="category"),
    path('productdetail/<int:pk>',views.ProductDetails.as_view(),name="productdetail"),
    
    path('registration',views.CustomerRegistrationView.as_view(),name='custreg'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('logout',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('addcart',views.addcart,name='addcart'),
    path('cart',views.showcart,name='cart'),
    path('plus_cart',views.plus_cart),
    path('minus_cart',views.minus_cart),
    path('remove_cart',views.remove_cart),
    path('add_cart',views.add_cart),
    
    path('search',views.search,name='search'),

    # path('reg',views.createuser),
    # path('log',views.loginpanel),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
