# Generated by Django 4.0.4 on 2022-05-09 08:37

from django.db import migrations, models
import getrecipeapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('getrecipeapp', '0011_alter_complexity_name_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='image',
            field=models.ImageField(blank=True, help_text='Максимальный размер картинки 1 мб', null=True, upload_to='images_small', validators=[getrecipeapp.models.validate_image]),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='image_full',
            field=models.ImageField(blank=True, help_text='Максимальный размер картинки 1 мб', null=True, upload_to='images_full', validators=[getrecipeapp.models.validate_image]),
        ),
    ]
