# Generated by Django 2.2 on 2019-04-02 17:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_auto_20190402_1343'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Todo',
        ),
    ]
