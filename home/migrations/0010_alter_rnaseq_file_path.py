# Generated by Django 4.1.12 on 2024-03-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_remove_rnaseq_username_rnaseq_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rnaseq",
            name="file_path",
            field=models.CharField(default="", max_length=128, verbose_name="文件路径"),
        ),
    ]
