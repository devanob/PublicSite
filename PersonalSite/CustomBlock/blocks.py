from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcolumnblocks.blocks import ColumnsBlock
from wagtail_svgmap.blocks import ImageMapBlock

class CustomImageBlock(blocks.StructBlock):
      image = ImageChooserBlock(required=True)
      width = blocks.IntegerBlock(required=False, min_value= 0, max_value=4000)
      height = blocks.IntegerBlock(required=False, min_value= 0, max_value=4000)
      class_name = blocks.CharBlock(required=False)


class CustomSVGImageBlock(blocks.StructBlock):
      svg_image = ImageMapBlock(required=True)
      class_name = blocks.CharBlock(required=False)
      description =  blocks.CharBlock(required=False)

class GridIconDescriptionList(blocks.StructBlock):
    icon_list = blocks.ListBlock(CustomSVGImageBlock(template="CustomBlock/custom_image_svg_block.html"),template = "CustomBlock/custom_list_icon_block.htm")
    class_name = blocks.CharBlock(required=False)





