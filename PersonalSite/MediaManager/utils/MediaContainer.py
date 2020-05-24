from contextlib import contextmanager
from django.forms.widgets import Media

class MediaContainer(object):
    media=None
    def __init__(self):
        self.media = Media()
        self.block_media = None
        self.in_media_block = False
    # @property
    # def media(self):
    #     return self.media_
    def start_media_block(self):
        """
        Starts ``{% media %}`` block mode.
        """
        self.in_media_block = True
        self.block_media = Media()

    def end_media_block(self):
        """
        Exits ``{% media %}`` block mode, and prepends the accumulated media
        to the page media
        """
        self.in_media_block = False
        self.add_media(self.block_media)
        self.block_media = None

    def add_media(self, media):
        """
        Add the `media` to the current page media. If the page is currently in
        ``{% media %}`` block, the media is appended to the block media,
        otherwise the media is prepended to the site media.
        """
        if media is None:
            return

        if self.in_media_block:
            self.block_media = self.block_media + media
        else:
            self.media = self.media + media

    @contextmanager
    def media_block(self):
        self.start_media_block()
        yield()
        self.end_media_block()

    @classmethod
    def from_context(cls, context):
        if MEDIA_KEY not in context:
            context[MEDIA_KEY] = MediaContainer()

        return context[MEDIA_KEY]



