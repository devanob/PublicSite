from .models import Project,ProjectCategory,ProjectCategoryOrderable
from rest_framework import serializers
from rest_framework.fields import Field
from collections import OrderedDict

from rest_framework.fields import Field

class SourceImageIOError(IOError):
    """
    Custom exception to distinguish IOErrors that were thrown while opening the source image
    """
    pass

class ImageRenditionField(Field):
    """
    A field that generates a rendition with the specified filter spec, and serialises
    details of that rendition.
    Example:
    "thumbnail": {
        "url": "/media/images/myimage.max-165x165.jpg",
        "width": 165,
        "height": 100
    }
    If there is an error with the source image. The dict will only contain a single
    key, "error", indicating this error:
    "thumbnail": {
        "error": "SourceImageIOError"
    }
    """
    def __init__(self, filter_spec, *args, **kwargs):
        self.filter_spec = filter_spec
        super().__init__(*args, **kwargs)

    def to_representation(self, image):
        # print(self.context)
        try:
            thumbnail = image.get_rendition(self.filter_spec)

            return OrderedDict([
                ('url', thumbnail.url),
                ('width', thumbnail.width),
                ('height', thumbnail.height),
                ('alt', thumbnail.alt),
            ])

        except SourceImageIOError:
            return OrderedDict([
                ('error', 'SourceImageIOError'),
            
            ])


##SVG
class SourceImageIOError(IOError):
    """
    Custom exception to distinguish IOErrors that were thrown while opening the source image
    """
    pass

class SVGRenditionField(Field):
    """
    A field that generates a rendition with the specified filter spec, and serialises
    details of that rendition.
    Example:
    "thumbnail": {
        "url": "/media/images/myimage.max-165x165.jpg",
        "width": 165,
        "height": 100
    }
    If there is an error with the source image. The dict will only contain a single
    key, "error", indicating this error:
    "thumbnail": {
        "error": "SourceImageIOError"
    }
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, icons_model):
        # print(self.context)
        try:
            return icons_model.rendered_svg

        except SourceImageIOError:
            return OrderedDict([
                ('error', 'SourceImageIOError'),
            
            ])
class ProjectCategorySerializer(serializers.ModelSerializer):
    icon = SVGRenditionField()
    class Meta:
        model = ProjectCategory
        fields = '__all__'

# class ProjectCategoryOrderableSerializer(Field):
#      def to_representation(self, model):
#         return Pro
#     class Meta:
#         model = ProjectCategoryOrderable
#         fields = ['project_category']


class ProjectSerializer(serializers.ModelSerializer):
    image = ImageRenditionField("original")
    _categories = ProjectCategorySerializer(read_only=True, many=True)

    #snippet = serializers.Field(source='snippet_html')
    class Meta:
        model = Project
        fields = '__all__'