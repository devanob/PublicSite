from .models import Project
from django.shortcuts import get_object_or_404
from  .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api import APIField
from .pagination import CustomPaginator

# created = models.DateTimeField(verbose_name='Date Created')
#     last_updated = models.DateTimeField(verbose_name='Date Updated')
#     description = models.TextField(max_length=1000)
#     project_link = models.CharField(max_length=100)
#     projectHandlier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="projectUserHandlier",)
class ProjectViewSet(viewsets.ViewSet,CustomPaginator):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Project.objects.get_queryset().order_by('id')
        queryset_paginated= self.paginate_queryset(queryset,request)
        serializedProject = ProjectSerializer(queryset_paginated, many=True, context={'request': request})
        return self.get_paginated_response(serializedProject.data)
   