from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from questionnaire import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tests', views.TestViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = router.urls + [
]

urlpatterns = format_suffix_patterns(urlpatterns)
