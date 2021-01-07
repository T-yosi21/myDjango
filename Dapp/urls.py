from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'Dapp'

urlpatterns = [
    path('index/', views.ProductList, name='ProductList'),
    path('product/', views.ProductCreate, name='ProductCreate'),
    path('<int:pk>/update/', views.ProductUpdate.as_view(), name='ProductUpdate'),
    path('<int:pk>/delete/', views.ProductDelete, name='ProductDelete'),
    path('<int:pk>/Detail/', views.ProductDetail, name='ProductDetail'),
    path('', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="Dapp:ProductList"), name='logout'),
]
