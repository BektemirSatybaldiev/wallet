from django.urls import path, include
from .views import CustomerViewSet, UserViewSet, TransferViewSet
from rest_framework.routers import SimpleRouter

app_name = 'payment'
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('customers', CustomerViewSet, basename='customers')


urlpatterns = [
    path('', include(router.urls)),
    path('transfer/', TransferViewSet.as_view({'post': 'create'}), name='transfer'),
]

