from django.contrib import admin
# includeを追加
from django.urls import path, include
from django.conf import settings
# staticを追加
from django.conf.urls.static import static

# reviewprojectのurls.pyからアプリのurls.pyを呼び出す
# requestがMEDIA_URLと一致した時に、MEDIA＿ROOTで定義した画像を呼び出す
# CSSも同様に設定する
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewpost.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
