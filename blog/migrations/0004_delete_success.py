# Generated by Django 4.0.3 on 2022-03-13 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_success_remove_post_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Success',
        ),
    ]