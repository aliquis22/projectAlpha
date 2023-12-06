# Generated by Django 4.2.3 on 2023-12-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='organisations', to='auth.group'),
        ),
    ]