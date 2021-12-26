from django.contrib import admin
# includeを追加
from django.urls import path, include

# blogpost.urlsを追加
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogpost.urls')),
]
