from django.db import models
from BaseSectionPage.models import BaseSection as Page
#from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
#Page To Represent A Collection Of  Projects 
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.search.backends import get_search_backend
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms
##Project Model
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.models import ClusterableModel
from modelcluster.tags import ClusterTaggableManager
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class Project(index.Indexed,ClusterableModel):
    
    # Fields
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255,verbose_name='name')
    tags = ClusterTaggableManager(through='Projects.ProjectTag', blank=True)
    created = models.DateTimeField(verbose_name='Date Created')
    last_updated = models.DateTimeField(verbose_name='Date Updated')
    description = models.TextField(max_length=1000)
    project_link = models.CharField(max_length=100)
    projectHandlier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="projectUserHandlier",)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+', blank=True)
    categories = ParentalManyToManyField('Projects.ProjectCategory',related_name='related_categories', blank=True)
    def __str__(self):
        return "{} created on {} last updated {} ".format(
            self.project_name,
            self.created.strftime('%m-%d-%Y, %H:%M:%S'),
            self.last_updated.strftime('%m-%d-%Y, %H:%M:%S'),
            )
    #search Fields
    panels = [
        FieldPanel('project_name'),
        ImageChooserPanel('image'),
        FieldPanel('tags'),
        FieldPanel('categories',widget=forms.CheckboxSelectMultiple),
        FieldPanel('project_link'),
        FieldPanel('description'),
      
    ]

    search_fields = [
        index.SearchField('project_name', partial_match=True),
        index.SearchField('description', partial_match=True),
    ]
    ##
    
class ProjectPageIndex(Page):
    parent_page_types = ['home.HomePage']
    model = Project
    get_search_param = "search-key"
    template = 'Projects/project_index.html'
    # get search query set
    def getQuerySet(self, searchText=""):
        search_back_end = get_search_backend()
        if self.getModel ==None:
            return None
        serach_results  = search_back_end.search(searchText, self.getModel().objects.all())
        return serach_results
from wagtail.snippets.models import register_snippet

@register_snippet
class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    
    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"



class ProjectTag(TaggedItemBase):
    content_object = ParentalKey(Project, related_name='project_tags')
    verbose_name = "Project Tag"
    class Meta:
        verbose_name_plural = "Project Tags"
        verbose_name = "Project Tag"

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
        verbose_name_plural = "Project Tags"
        verbose_name = "Project Tag"