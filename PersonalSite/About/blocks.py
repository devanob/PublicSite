from CustomBlock import blocks as custom_blocks
from wagtail.core import blocks
# from wagtailcolumnblocks.blocks import ColumnsBlock
#from wagtail_blocks.blocks import HeaderBlock,ImageSliderBlock
from wagtail_svgmap.blocks import ImageMapBlock
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



class AboutGenericColumnBlocks(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    about_content = AboutContentBlocks()
    
    