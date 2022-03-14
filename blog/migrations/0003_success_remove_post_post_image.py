# Generated by Django 4.0.3 on 2022-03-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
    ]