from django.apps import AppConfig
from django.urls import path,include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f'User',UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


# Using DefaultRouter, don’t need to manually define each URL for CRUD operations. It automatically creates standard RESTful endpoints like:

# GET /courses/ (list all  courses)
# POST /courses/ (create new courses)
# GET / courses/{id}/ (retrieve a single courses)
# PUT / courses/{id}/ (update a courses)
# DELETE / courses/{id}/ (delete a courses)