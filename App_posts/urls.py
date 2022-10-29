# from django.urls import path
# from .views import PostsPIView


from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostsViewSet

router = DefaultRouter()

router.register('posts', PostsViewSet, basename='posts')

urlpatterns = [
    # path('posts/', PostsPIView.as_view()),
    path('', include(router.urls))
]
