from CustomBlock import blocks as custom_blocks
from wagtail.core import blocks
from wagtailcolumnblocks.blocks import ColumnsBlock
#from wagtail_blocks.blocks import HeaderBlock,ImageSliderBlock
from wagtail_svgmap.blocks import ImageMapBlock
#from wagtailclearstream import ClearBlock

class AboutContentBlocks(blocks.StreamBlock):
    """
    Allowed Blocks 
    """
    image = custom_blocks.CustomImageBlock(classname="full title",required=False,template="About/block_templates/image_block.html")
    #headers = HeaderBlock(required=False)
    rich_field_text = blocks.RichTextBlock(required=False)
    #image_slider = ImageSliderBlock()
    svg_image = custom_blocks.CustomSVGImageBlock(template = "CustomBlock/custom_image_svg_block.html")
    grid_block = custom_blocks.GridIconDescriptionList(template="CustomBlock/custom_grid_icon_block.html")



class AboutColumnBlocksTwoColumn(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    Two_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        AboutContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Two",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )
class AboutColumnBlocksThreeColumn(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    Three_Column_ = ColumnsBlock(
        # Blocks you want to allow within each column
        AboutContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,1,1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns Three",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )

class AboutColumnBlocksOneColumn(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    One_Column = ColumnsBlock(
        # Blocks you want to allow within each column
        AboutContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1,),
        # Used for grouping related fields in the streamfield field picker
        group="Columns One",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        # template='About/block_templates/image_block.html',
    )