# Generated by Django 3.1.2 on 2020-10-29 12:20

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0011_auto_20201028_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='color',
            field=wagtail_color_panel.fields.ColorField(blank=True, default='#000000', max_length=7, null=True),
        ),
    ]
