# Generated by Django 4.0.6 on 2023-03-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanner', '0002_rename_rate_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedbackId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='locationId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]