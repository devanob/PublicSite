from django.db import models
from wagtail.core.models import Page
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import  ImageChooserPanel



# Create your models here.
class BaseSection(Page):
    """
    BaseSection abstract base class. All sections should inherit
    from this class.This Will Also Serve As A Regular Page As Well. 
    """

    parent_page_types = [] #empty by default 
    subpage_types = []
    section_template_name = "" #default empty 
    section_slug = AutoSlugField(populate_from=['title'], editable=True)
    int_order = models.IntegerField(default=170)
    banner_image = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+', blank=True)
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Page Configuration Base-Section"),
    ]
    content_panels = Page.content_panels + [
       FieldPanel('section_slug'),
       ImageChooserPanel('banner_image'),
    ]

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