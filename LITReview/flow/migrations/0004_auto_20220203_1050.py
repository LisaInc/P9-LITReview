# Generated by Django 3.2.9 on 2022-02-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0003_rename_body_ticket_ticket_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='review_body',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='review_title',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='title',
            new_name='ticket_title',
        ),
    ]
