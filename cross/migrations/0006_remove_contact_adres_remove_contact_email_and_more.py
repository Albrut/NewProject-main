# Generated by Django 4.1.1 on 2022-12-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0005_remove_products_text1_1_remove_products_text1_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='adres',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image_down1',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image_down2',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image_down3',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image_mem',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='insta',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name3',
        ),
        migrations.AddField(
            model_name='contact',
            name='addres',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email1',
            field=models.EmailField(default='albertgadiev@yandex.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='email2',
            field=models.EmailField(default='albertgadiev@yandex.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='email3',
            field=models.EmailField(default='albertgadiev@yandex.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='our_client1',
            field=models.TextField(default='Best of the best'),
        ),
        migrations.AddField(
            model_name='contact',
            name='our_client2',
            field=models.TextField(default='Better than best'),
        ),
    ]