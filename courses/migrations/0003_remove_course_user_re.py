# Generated by Django 4.2 on 2023-04-26 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_user_re_courseregister'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user_re',
        ),
    ]