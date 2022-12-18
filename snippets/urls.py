from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('users/v2/', views.UserList.as_view(), name='user-list'),
    path('users/v2/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    #Function based views
    #   Using JsonResponse for return json format respond
    path('snippets/v1/', views.snippet_list_v1, name='snippet-list'),
    path('snippets/v1/<int:pk>/', views.snippet_detail_v1, name='snippet-detail'),
    path('snippets/v1/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #   Using Response for return html format response
    path('snippets/v2/', views.snippet_list_v2, name='snippet-list'),
    path('snippets/v2/<int:pk>/', views.snippet_detail_v2, name='snippet-detail'),
    path('snippets/v2/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #Class based views
    #   Using APIView class
    path('snippets/v3/', views.SnippetList_v1.as_view(), name='snippet-list'),
    path('snippets/v3/<int:pk>/', views.SnippetDetail_v1.as_view(), name='snippet-detail'),
    path('snippets/v3/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #   Using GenericAPIView with mixins classes
    path('snippets/v4/', views.SnippetList_v2.as_view(), name='snippet-list'),
    path('snippets/v4/<int:pk>/', views.SnippetDetail_v2.as_view(), name='snippet-detail'),
    path('snippets/v4/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    #   Using generic class-based views
    path('snippets/v5/', views.SnippetList_v3.as_view(), name='snippet-list'),
    path('snippets/v5/<int:pk>/', views.SnippetDetail_v3.as_view(), name='snippet-detail'),
    path('snippets/v5/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),    
]
#To append a set of format suffix patterns to the existing URLs
urlpatterns = format_suffix_patterns(urlpatterns)