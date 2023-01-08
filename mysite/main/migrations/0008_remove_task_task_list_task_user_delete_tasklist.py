# Generated by Django 4.1.5 on 2023-01-08 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_remove_task_user_tasklist_task_task_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_list',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]