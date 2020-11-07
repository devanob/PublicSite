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
from wagtail_color_panel.fields import ColorField
##Project Model
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.models import ClusterableModel
from modelcluster.tags import ClusterTaggableManager
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail_svgmap.models import ImageMap
from django.contrib.auth import get_user_model
from wagtail_color_panel.edit_handlers import NativeColorPanel
from wagtail.core.models import Orderable

@register_snippet
class Project(index.Indexed,ClusterableModel):
    
    # Fields
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='project_name', blank=True,editable=True)
    project_name = models.CharField(max_length=255,verbose_name='name')
    tags = ClusterTaggableManager(through='Projects.ProjectTag', blank=True)
    created = models.DateTimeField(verbose_name='Date Created')
    last_updated = models.DateTimeField(verbose_name='Date Updated')
    description = models.TextField(max_length=1000, blank=True, null=True)
    project_link = models.CharField(max_length=100)
    show_case= models.BooleanField(blank=False,default=True)
    projectHandlier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="projectUserHandlier",)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+', blank=True)
    _categories = models.ManyToManyField('Projects.ProjectCategory',through = 'ProjectCategoryOrderable', blank=True)
    def __str__(self):
        return "{} created on {} last updated {} ".format(
            self.project_name,
            self.created.strftime('%m-%d-%Y, %H:%M:%S'),
            self.last_updated.strftime('%m-%d-%Y, %H:%M:%S'),
            )
    #search Fields
    panels = [
        FieldPanel('project_name'),
        FieldPanel('description'),
        FieldPanel('show_case'),
        ImageChooserPanel('image'),
         MultiFieldPanel(
            [
                InlinePanel("project_categories", label="Categories")
            ],
            heading="Categorie(s)"
        ),
        FieldPanel("projectHandlier"),
        FieldPanel('tags'),
        FieldPanel('project_link'),
        FieldPanel('slug'),
        
      
    ]

    search_fields = [
        index.SearchField('project_name', partial_match=True),
        index.SearchField('description', partial_match=True),
    ]
    def snippet_html(self):
        return "this works"
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


@register_snippet
class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True, editable=True,unique=True)
    icon = models.ForeignKey(ImageMap, on_delete=models.SET_NULL,null=True, related_name='+', blank=True)
    color = ColorField(default="coral", blank=True, null=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        SnippetChooserPanel('icon'),
        NativeColorPanel('color')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"



@register_snippet
class ProjectTag(TaggedItemBase):
    content_object = ParentalKey(Project, related_name='project_tags')
    verbose_name = "Project Tag"
    class Meta:
        verbose_name_plural = "Project Tags"
        verbose_name = "Project Tag"
    

class ProjectCategoryOrderable(Orderable):

    """This allows us to select one or more categories from Snippets."""
    project = ParentalKey("Projects.Project", related_name="project_categories")
    project_category = models.ForeignKey(
        "Projects.ProjectCategory",
        on_delete=models.CASCADE,
    )
    
    panels = [
    	# Use a SnippetChooserPanel because Of Foreign Key 
        SnippetChooserPanel("project_category"),
    ]