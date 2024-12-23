# Generated by Django 5.1.1 on 2024-11-23 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancehistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='users.employee'),
        ),
        migrations.AddField(
            model_name='post',
            name='current_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='current_datas', to='post.currentdata'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post_locations', to='post.location'),
        ),
        migrations.AddField(
            model_name='maintenancehistory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='post.post'),
        ),
    ]
