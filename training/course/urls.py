from .views import CourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', CourseViewSet)

urlpatterns = router.urls

# Check all the urls in the router
# for url in router.urls:
#     print(url, '\n')