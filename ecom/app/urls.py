from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('category/<slug:value>',views.CategoryView.as_view(),name="category"),
    path('productdetail/<int:pk>',views.ProductDetails.as_view(),name="productdetail"),

    path('reg',views.createuser),
    path('log',views.loginpanel),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
