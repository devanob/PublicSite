from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcolumnblocks.blocks import ColumnsBlock
from wagtail_svgmap.blocks import ImageMapBlock
from Projects.blocks import ProjectListing

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







from CustomBlock import blocks as custom_blocks
from wagtail.core import blocks
from wagtailcolumnblocks.blocks import ColumnsBlock
#from wagtail_blocks.blocks import HeaderBlock,ImageSliderBlock
from wagtail_svgmap.blocks import ImageMapBlock
#from wagtailclearstream import ClearBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock
class GeneralContentBlocks(blocks.StreamBlock):
    """
    Allowed Blocks 
    """
    image_block = ImageChooserBlock(required=False)
    #headers = HeaderBlock(required=False)
    rich_field_text = blocks.RichTextBlock(required=False)
    #image_slider = ImageSliderBlock()
    svg_image = custom_blocks.CustomSVGImageBlock(template = "CustomBlock/custom_image_svg_block.html")
    header_block= HeaderBlock(),
    list_block = ListBlock()
    image_text_overlay = ImageTextOverlayBlock()
    cropped_images_with_text= CroppedImagesWithTextBlock()
    list_with_images = ListWithImagesBlock()
    thumbnail_gallery = ThumbnailGalleryBlock()
    chart = ChartBlock()
    map_block = MapBlock()
    image_slider = ImageSliderBlock()
    project_listing = ProjectListing()
   
class InnerColumnBlocks(blocks.StreamBlock):
    """ 
    All the root level blocks you can use
    """
    #
    One_Column = ColumnsBlock(
        # Blocks you want to allow within each column
         GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,),
        # Used for grouping related fields in the streamfield field picker
        group="Columns One",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )
    ##
    Two_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Two",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )
    ##
    Three_Column_ = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,1,1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Three",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/im
    )
    ##
    Four_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,1,1,1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Four",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )

class ColumnBlocks(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    #
    One_Column = ColumnsBlock(
        # Blocks you want to allow within each column
         GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,),
        # Used for grouping related fields in the streamfield field picker
        group="Columns One",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )
    ##
    Two_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Two",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )
    ##
    Three_Column_ = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,1,1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Three",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/im
    )
    ##
    Four_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        GeneralContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,1,1,1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Four",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )








