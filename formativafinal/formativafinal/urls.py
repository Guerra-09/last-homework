from django.contrib import admin
from django.urls import path, include
from resenas import views
from resenas.views import ResenaCreateView, ResenaListView, ResenaDeleteView, ResenaUpdateView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form', ResenaCreateView.as_view(), name='form'),
    path('list', ResenaListView.as_view(), name='list'),
    path('success_delete/<int:pk>', ResenaDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', ResenaUpdateView.as_view(), name='update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
