# Generated by Django 4.1.12 on 2024-03-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_alter_rnaseq_file_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="rnaseq",
            name="user_name",
            field=models.CharField(default="", max_length=128, verbose_name="用户名"),
        ),
    ]
