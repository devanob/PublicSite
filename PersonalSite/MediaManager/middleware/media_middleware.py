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
        response.render()
        current_thread_media_container = self.get_current_media_container()
        print( current_thread_media_container.media)
        render_files = render(request, 'MediaManager/media_manager.html', {}, '')
        response.content  = response.content + render_files.content
        return response

    def process_response(self, request, response):
        #response.content = response.rendered_content
        try:
            del self.thread_media_map[threading.get_ident()]
        except KeyError:
            return response
        return response