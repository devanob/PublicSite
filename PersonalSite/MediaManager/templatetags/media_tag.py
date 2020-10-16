from django.template import Library, Node
from ..middleware.media_middleware import GlobalMediaMiddleware
from django.forms.widgets import Media
from functools import reduce
import threading
register = Library()

MEDIA_KEY = '_media'


@register.simple_tag(takes_context=True)
def add_media(context, *args):
    print(threading.get_ident())
    #print(args)
    medias = filter(lambda m: isinstance(m, Media), args)
    print(medias)
    if not bool(medias):
        return ''
    media_container = GlobalMediaMiddleware.get_current_media_container()
    media_container.add_media(reduce(lambda acc, m: acc + m, medias))

    return ''


@register.simple_tag(takes_context=True)
def add_js(context,media, *js):
    #print(js)
    add_media(context, Media(js=js))
    return ''


@register.simple_tag(takes_context=True)
def add_css(context, media, *css):

    add_media(context, Media(css={"all": css}))
    media_container = GlobalMediaMiddleware.get_current_media_container()
   
    return ''


@register.simple_tag(takes_context=True)
def print_media(context, media_type=None):
    media_container = GlobalMediaMiddleware.get_current_media_container()
    media = media_container.media

    #print(media)
    
    if media_type is None:
        return media
    return media[media_type]


class MediaNode(Node):
    TAG_NAME = 'media'

    def __init__(self, nodelist):
        super(MediaNode, self).__init__()
        self.nodelist = nodelist

    def render(self, context):
        media_container = GlobalMediaMiddleware.get_current_media_container()
        with media_container.media_block():
            # Run for its side effects, discard output.
            self.nodelist.render(context)

        return ''


@register.tag(MediaNode.TAG_NAME)
def media(parser, token):
    nodelist = parser.parse(('end' + MediaNode.TAG_NAME,))
    parser.delete_first_token()
    return MediaNode(nodelist)


    