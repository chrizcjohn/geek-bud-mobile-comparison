# Generated by Django 2.2.7 on 2019-12-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEEKBUUDY', '0010_auto_20191202_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='caption',
            field=models.CharField(max_length=50, null=True),
        ),
    ]