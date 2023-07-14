# Generated by Django 4.1.1 on 2023-07-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cross", "0021_remove_main2_pre_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="main2",
            name="button_for_page",
        ),
        migrations.RemoveField(
            model_name="mainpage1_cross",
            name="button_for_page",
        ),
        migrations.AddField(
            model_name="main2",
            name="button_for_page1",
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name="main2",
            name="button_for_page2",
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name="mainpage1_cross",
            name="button_for_page1",
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name="mainpage1_cross",
            name="button_for_page2",
            field=models.CharField(max_length=900, null=True),
        ),
    ]
