from ..middleware.media_middleware import GlobalMediaMiddleware as global_media_middleware
from django.forms.widgets import Media as media_form


def add_media(*args):
    medias = filter(lambda m: isinstance(m, media_form), args)

    if not bool(medias):
        return ''

    media_container = global_media_middleware.get_current_media_container()
    media_container.add_media(reduce(lambda acc, m: acc + m, medias))
    return ''

def add_css_util(media, *css):
    add_media(context, media_form(css={media: css}))
    return ''

def add_js(*js):
    add_media(context, media_form(js=js))
   