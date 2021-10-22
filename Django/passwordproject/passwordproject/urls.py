from django.contrib import admin
from django.urls import path, include

# authアプリケーションを呼び出す
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('django.contrib.auth.urls')),
]