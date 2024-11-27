from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main.views import home, catalog, buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('buying/', buy, name='buying')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)