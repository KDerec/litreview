# Generated by Django 4.0.4 on 2022-05-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(blank=True, max_length=8192),
        ),
        migrations.AlterField(
            model_name="review",
            name="headline",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=128),
        ),
    ]
