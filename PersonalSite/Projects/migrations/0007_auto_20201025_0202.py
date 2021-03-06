# Generated by Django 3.1.2 on 2020-10-25 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_svgmap', '0002_size_cache'),
        ('Projects', '0006_auto_20201025_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtail_svgmap.imagemap'),
        ),
        migrations.AlterField(
            model_name='project',
            name='show_case',
            field=models.BooleanField(default=True),
        ),
    ]
