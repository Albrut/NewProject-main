# Generated by Django 4.1.1 on 2022-12-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0009_rename_text1_1_about_us_occup2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
