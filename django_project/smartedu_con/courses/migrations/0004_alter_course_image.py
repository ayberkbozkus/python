# Generated by Django 3.2.5 on 2021-07-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/default_course_image.jpeg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]
