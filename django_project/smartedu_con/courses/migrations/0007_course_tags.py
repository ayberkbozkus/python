# Generated by Django 3.2.5 on 2021-08-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]
