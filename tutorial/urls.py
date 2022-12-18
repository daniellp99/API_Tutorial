from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from tutorial.quickstart import views
from snippets.views import SnippetViewSet_v2, UserViewSet

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', SnippetViewSet_v2,basename="snippet")
router.register(r'users', UserViewSet,basename="user")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    #useful if your API requires authentication and you want to use the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('', include('snippets.urls')),
    path('', include(router.urls)),
    
    
]