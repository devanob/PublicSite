# Generated by Django 3.0.6 on 2020-05-26 20:51

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_svgmap.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_auto_20200414_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpageindex',
            name='page_icon',
            field=wagtail.core.fields.StreamField([('icon_page', wagtail.core.blocks.StructBlock([('map', wagtail_svgmap.blocks._ImageMapChoiceBlock(label='Image map', required=True)), ('css_class', wagtail.core.blocks.CharBlock(label='CSS class', required=False))]))], default=0),
            preserve_default=False,
        ),
    ]
