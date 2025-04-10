from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import SecureHelloView

router = DefaultRouter()
router.register('todos', views.TodoViewSet)  


urlpatterns = [
    path('api/', include(router.urls)),  
    path('secure-hello/', SecureHelloView.as_view()),
]
