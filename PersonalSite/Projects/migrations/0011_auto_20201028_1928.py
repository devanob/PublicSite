# Generated by Django 3.1.2 on 2020-10-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0010_auto_20201028_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
