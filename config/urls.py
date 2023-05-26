from django.urls import path, include

from shop.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('api/', include('apis.urls'))
]
