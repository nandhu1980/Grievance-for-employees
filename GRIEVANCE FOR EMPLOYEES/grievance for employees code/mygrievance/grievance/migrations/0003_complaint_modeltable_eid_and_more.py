# Generated by Django 4.2.7 on 2023-11-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievance', '0002_complaint_modeltable'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint_modeltable',
            name='eid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='complaint_modeltable',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
