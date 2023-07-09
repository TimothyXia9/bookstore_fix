# Generated by Django 2.0.2 on 2018-02-28 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180228_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='publication_time',
            new_name='published_time',
        ),
        migrations.AddField(
            model_name='book',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='上架时间'),
            preserve_default=False,
        ),
    ]
