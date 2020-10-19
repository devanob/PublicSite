# Generated by Django 3.1.2 on 2020-10-17 22:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail_svgmap.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0014_auto_20201017_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpageindex',
            name='body',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StreamBlock([('One_Column', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user'))], grid_width=12, group='Columns One')), ('Two_Column', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_1', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user'))], grid_width=12, group='Columns Two')), ('Three_Column_', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_1', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_2', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user'))], grid_width=12, group='Columns Three')), ('Four_Column', wagtail.core.blocks.StructBlock([('column_0', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_1', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_2', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user')), ('column_3', wagtail.core.blocks.StructBlock([('column_instance', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('height', wagtail.core.blocks.IntegerBlock(max_value=4000, min_value=0, required=False)), ('class_name', wagtail.core.blocks.CharBlock(required=False))], classname='full title', required=False, template='About/block_templates/image_block.html')), ('rich_field_text', wagtail.core.blocks.RichTextBlock(required=False)), ('svg_image', wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html')), ('grid_block', wagtail.core.blocks.StructBlock([('icon_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('svg_image', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))], required=True)), ('class_name', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_image_svg_block.html'), template='CustomBlock/custom_list_icon_block.htm')), ('class_name', wagtail.core.blocks.CharBlock(required=False))], template='CustomBlock/custom_grid_icon_block.html'))])), ('ratio_number', wagtail.core.blocks.IntegerBlock(help_text='Ratios For Column', max_value=12, min_value=1))], icon='user'))], grid_width=12, group='Columns Four'))], required=False))], blank=True, null=True),
        ),
    ]
