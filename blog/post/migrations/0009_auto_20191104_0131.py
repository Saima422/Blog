# Generated by Django 2.2.6 on 2019-11-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(default='Others', max_length=50),
        ),
    ]
