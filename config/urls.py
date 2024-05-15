from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.general.urls')),
    path('users/', include('apps.users.urls')),
    path('product_list/', include('apps.products.urls')),
    path('contact/', include('apps.contacts.urls')),
    path('wishlist/', include('apps.wishlists.urls')),
    path('comment/', include('apps.comments.urls')),
    path('carts/', include('apps.carts.urls')),
    path('orders/', include('apps.orders.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
