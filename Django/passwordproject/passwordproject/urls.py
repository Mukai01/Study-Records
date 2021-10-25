from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# authアプリケーションを呼び出す
# change-passwordが入っている場合、auth_viewsで定義されているPasswordChangeViewクラスを呼び出す
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'),),
]