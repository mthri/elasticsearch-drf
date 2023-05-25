from django.urls import path

from shop.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
]
