from django.contrib import admin
# includeを追加
from django.urls import path, include

# reviewprojectのurls.pyからアプリのurls.pyを呼び出す
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewpost.urls'),)
]
