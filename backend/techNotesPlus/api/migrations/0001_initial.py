# Generated by Django 3.2.6 on 2021-08-17 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NOTE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE', models.TextField(max_length=512, verbose_name='TITLE')),
                ('CONTENT', models.TextField(verbose_name='CONTENT')),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, null=True, verbose_name='TIME_STAMP')),
                ('CREATED_BY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
