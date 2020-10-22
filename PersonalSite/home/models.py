from django.db import models
from MediaManager.middleware.media_middleware import GlobalMediaMiddleware
from wagtail.core.models import Page
from BaseSectionPage.models import BaseSection 
from About.models import AboutPageIndex
class HomePage(Page):
   #section_list = [AboutPageIndex]
   
   def get_context(self, request):
      context = super(HomePage, self).get_context(request)
      context['sections']= self.getSections()
      for i in context['sections']:
         print(i.section_template_name )
      return context
   def getSections(self):
      #loop through  set of legal section children of the homepage
      return self.get_children().type(BaseSection).specific()
