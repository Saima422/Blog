# Generated by Django 2.1.7 on 2019-10-06 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20191005_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagg', models.ForeignKey(default='Others', on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
    ]
