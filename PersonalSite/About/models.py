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
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from CustomBlock import blocks as custom_blocks
from . import  blocks as AboutBlocks
class AboutPageIndex(Page):
    parent_page_types = ['home.HomePage']
    template = "About/about_page.html"
    section_template_name = "About/about_snippet.html" #default empty 
    body = StreamField([
        ('column_about_block', AboutBlocks.AboutGenericColumnBlocks(required=False)),
    
    ],blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    