# Generated by Django 2.2.7 on 2019-11-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GEEKBUUDY', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
    ]
