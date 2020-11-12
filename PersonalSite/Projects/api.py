from .models import Project
from django.shortcuts import get_object_or_404
from  .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api import APIField
from .pagination import CustomPaginator
from django.contrib.auth import get_user_model
# created = models.DateTimeField(verbose_name='Date Created')
#     last_updated = models.DateTimeField(verbose_name='Date Updated')
#     description = models.TextField(max_length=1000)
#     project_link = models.CharField(max_length=100)
#     projectHandlier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="projectUserHandlier",)
class ProjectViewSet(viewsets.ViewSet,CustomPaginator):
    """
    A simple ViewSet for listing or retrieving projects.
    """
    def list(self, request, user=None):
        category = request.query_params.get('category',"")
        print("chicken\n")
        print(category)
        queryset= None
        if (user == None):
            queryset = Project.objects.get_queryset()

        else:
             userModel = get_user_model()
             user = userModel.objects.get(username=user)
             queryset = user.projectUserHandlier
        ##
        if category.isnumeric():
            cat = int(category)
            queryset= queryset.filter(project_categories__project_category__in=[cat])
        ##
        queryset = queryset.filter(show_case=True)
        #Ordeer by last updated 
        queryset.order_by('-last_updated')
        ##
        queryset_paginated= self.paginate_queryset(queryset,request)
        serializedProject = ProjectSerializer(queryset_paginated, many=True, context={'request': request})
        return self.get_paginated_response(serializedProject.data)
    def listWithUser(self, request, portal_pk=None):
        return ""