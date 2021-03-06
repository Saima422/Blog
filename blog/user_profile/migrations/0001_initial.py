# Generated by Django 2.0.1 on 2019-10-14 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('website', models.URLField(verbose_name='Web Address')),
                ('bio', models.TextField()),
                ('interests', models.TextField()),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('user_created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
