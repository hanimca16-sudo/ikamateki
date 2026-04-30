from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/social/', include('allauth.socialaccount.urls')),
    path('accounts/google/', include('allauth.socialaccount.providers.google.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)