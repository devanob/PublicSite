from django import template
register = template.Library()


@register.simple_tag()
def get_template_name(page_object):
    #try to return the hash link of the \
    # current page if it inherits from the base section page
    try:
        return page_object.getSectionLinkWithHash()
    except:
        return None
