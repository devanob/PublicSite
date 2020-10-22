from django.db import models
from wagtail.core.models import Page
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import  ImageChooserPanel
from wagtail_svgmap.blocks import ImageMapBlock
from wagtail.core.blocks import StreamBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.utils.decorators import cached_classmethod

# Create your models here.
class BaseSection(Page):
    """
    BaseSection abstract base class. All sections should inherit
    from this class.This Will Also Serve As A Regular Page As Well. 
    """
    page_icon = StreamField(
    StreamBlock([
        ('icon_page', ImageMapBlock())
    ], min_num=0, max_num=1))
    parent_page_types = [] #empty by default 
    subpage_types = []
    section_template_name = "" #default empty 
    section_slug = AutoSlugField(populate_from=['title'], editable=True)
    int_order = models.IntegerField(default=170)
    banner_image = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+', blank=True)
    ##
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Page Configuration Base-Section"),
    ]
    ##
    page_panel_options= [
        StreamFieldPanel('page_icon'),
        FieldPanel('section_slug'),
        ImageChooserPanel('banner_image'),
    ]
    content_panels = Page.content_panels + [
       
       
    ]

    main_content_panels = []
    para_list = []
    
    @cached_classmethod
    def get_edit_handler(cls):
        edit_handler = TabbedInterface([
            ObjectList(cls.content_panels, heading='Snippet Content'),
            ObjectList(cls.main_content_panels, heading='Main Content'),
            ObjectList(cls.page_panel_options, heading='Page Options'),
            ObjectList(cls.promote_panels, heading='Promote'),
            ObjectList(cls.settings_panels, heading='Settings', classname="settings"),
        ])
        return edit_handler.bind_to(cls)
    

    class Meta:
        abstract = True

    def getSectionLinkWithHash(self):
        return "#{}".format(self.section_slug)

    def getSectionLink(self):
        return "{}".format(self.section_slug)

    def getSectionHTML(self):
        if self.section_template_name:
            return 1
        else:
            return 2
    # def get_url_parts(self,  request=None, *args, **kwargs):
    #     """
    #     Customising URL patterns for a page model
    #     http://docs.wagtail.io/en/latest/topics/pages.html#customising-url-patterns-for-a-page-model
    #     Rewrite page path to corresponding anchor of this section on the 
    #     containing page.
    #     """
    #     url_parts = super().get_url_parts(request=request)

    #     if url_parts is None:
    #         return None
    #     else:
    #         site_id, root_url, page_path = url_parts
    #         _cust_page_path = '#section-{}'.format(page_path.replace('/', ''))
    #         return (site_id, root_url, _cust_page_path)



from django.db import models
#from BaseSectionPage.models import BaseSection as Page
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

