# Generated by Django 4.1.1 on 2022-09-09 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_alter_mymodel_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='upload',
            new_name='upload_csv',
        ),
    ]
