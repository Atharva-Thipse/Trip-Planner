# Generated by Django 4.0.6 on 2023-03-13 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripPlanner', '0007_alter_place_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='locationId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tripPlanner.place'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
