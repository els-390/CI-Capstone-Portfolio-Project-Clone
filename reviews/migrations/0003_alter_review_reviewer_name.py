# Generated by Django 4.2.16 on 2024-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_client_remove_review_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer_name',
            field=models.CharField(max_length=100),
        ),
    ]
