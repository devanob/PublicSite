import threading
from ..utils.MediaContainer import MediaContainer
from django.shortcuts import render

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10
    # Works perfectly for everyone using MIDDLEWARE_CLASSES
    MiddlewareMixin = object

class GlobalMediaMiddleware(MiddlewareMixin):
    #where we store per thread media center
    thread_media_map = {}

    @classmethod
    def get_current_media_container(cls):
        try:
            return cls.thread_media_map[threading.get_ident()]
        except KeyError:
            return MediaContainer()

    def process_request(self, request):
        self.thread_media_map[threading.get_ident()] = MediaContainer()

    def process_exception(self, request, exception):
        try:
            del self.thread_media_map[threading.get_ident()]
        except KeyError:
            pass
    def process_template_response(self, request, response):
        current_thread_media_container = self.get_current_media_container()
        render_files = render(request, 'MediaManager/media_manager.html', {}, '')
        media_content = render_files.content
        response.add_post_render_callback(self.callback_add_media)
        return response

    def callback_add_media(self,response):
        current_thread_media_container = self.get_current_media_container()
        render_files = render(None, 'MediaManager/media_manager.html', {}, '')
        media_content = render_files.content
        response.content  = media_content + response.content

    def process_response(self, request, response):
        return response
        response.content = response.rendered_content
        try:
            del self.thread_media_map[threading.get_ident()]
        except KeyError:
            return response
        return response#response.content = response.rendered_content
        try:
            del self.thread_media_map[threading.get_ident()]
        except KeyError:
            return response
        return response