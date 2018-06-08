from django.urls import path
from . import views
from ShortLinks.Views.Auth import Login, Register
from ShortLinks.Views.Statistics import Statistics
from django.contrib.auth import views as auth_views

app_name = 'ShortLinks'


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('<str:urlId>', views.RedirectUrl.as_view(), name='redirect'),
    path('home/statistics', Statistics.Statistics.as_view(), name='statistics'),
    path('home/create', views.CreateShortLink.as_view(), name='create'),

    path('login/', Login.Login.as_view(), name='login'),
    path('register/', Register.Register.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),

    #Some Functions
    path('logout/', Login.logout_view, name='logout'),

    # path('home/', views.home, name='home'),
    # path('login/', auth_views.login, name='login'),
]