from .api import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects/user/(?P<user>\D+)', ProjectViewSet, 'project-user')
#router.register(r'projects', ProjectViewSet , basename='project')