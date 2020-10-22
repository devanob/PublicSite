# Create your models here.
from django.db import models
from BaseSectionPage.models import BaseSection as Page
#from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
#Page To Represent A Collection Of  Projects 
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
#from django.xtensions.db.fields import AutoSlugField
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from wagtail.search.backends import get_search_backend
from wagtail.core.fields import StreamField,BlockField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from CustomBlock import blocks as custom_blocks
#from . import  blocks as AboutBlocks
from wagtail_svgmap.blocks import ImageMapBlock
from wagtail.core.blocks import StreamBlock
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList

#Generic Page For Generald Use
class CustomPage(Page):
    is_creatable  = True
    parent_page_types = ['home.HomePage','CustomPage.CustomPage']
    subpage_types = ['CustomPage.CustomPage']
    template = "About/about_page.html"
    section_template_name = "About/about_snippet.html" #default empty 
    body = StreamField([
        ('content', custom_blocks.ColumnBlocks(required=False)),
    
    ],blank=True, null=True)
    #Page Body Content
    page_body = StreamField([
        ('content', custom_blocks.ColumnBlocks(required=False)),
    
    ],blank=True, null=True)
    #body content Sections
    content_panels =  Page.content_panels + [
        StreamFieldPanel('body',classname='wagtailuiplus__panel--collapsed'),
    ]

    #body content page
    main_content_panels =  Page.main_content_panels + [
        StreamFieldPanel('page_body',classname='wagtailuiplus__panel--collapsed'),
    ]