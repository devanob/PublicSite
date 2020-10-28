from wagtail.core import blocks
from wagtail.snippets.blocks import (SnippetChooserBlock)
from wagtail.core.blocks import (IntegerBlock)
from django.contrib.auth import get_user_model
#DeFine Block Dislaying Project 


class ProjectListing(blocks.StructBlock):
    users = SnippetChooserBlock( get_user_model(), required=True )
    page_numer = IntegerBlock(min_value=3,max_value=9 )

    class Meta:
        template = 'Projects/blocks/project_listing.html'