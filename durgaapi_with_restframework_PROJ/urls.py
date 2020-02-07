
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from durgaapi_with_restframework_APP import views
from rest_framework_swagger.views import get_swagger_view


#from django.urls import path
#____________________________________________________________________________________________________________________

schema_view = get_swagger_view(title="RAW API Documentation")


router = routers.DefaultRouter()

# NOTE: If we use ModelViewSet, then this below code line is optional.
#router.register('api', views.EmployeeCRUDCBV, basename='api')
# router is only applicable, when we are using viewsets

router.register('api', views.EmployeeCRUDCBV)

# When we routers, we need to import include as (from django.conf.urls import include) and use it as show below in
# urlpatterns:




urlpatterns = [
    url(r'^swaggerdoc/', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),

]
