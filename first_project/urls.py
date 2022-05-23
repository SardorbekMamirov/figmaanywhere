
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib.auth.views import LogoutView
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Swagger')


urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('', include('basic_app.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)