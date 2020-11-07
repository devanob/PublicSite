from wagtail.core import blocks
from wagtail.snippets.blocks import (SnippetChooserBlock)
from wagtail.core.blocks import (IntegerBlock)
from django.contrib.auth import get_user_model
from .models import ProjectCategory
from rest_framework.reverse import reverse,reverse_lazy
#DeFine Block Dislaying Project 


class ProjectListing(blocks.StructBlock):
    users = SnippetChooserBlock( get_user_model(), required=True )
    page_numer = IntegerBlock(min_value=3,max_value=9 )

    #context injector
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['project_categories'] = ProjectCategory.objects.all()
        user = value['users'].username
        print(value)
        context['api_url'] = reverse_lazy('project-user-list', args=[user], request=None)
        return context

    class Meta:
        template = 'Projects/blocks/project_listing.html'