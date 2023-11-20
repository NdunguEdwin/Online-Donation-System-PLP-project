# Generated by Django 4.0.1 on 2022-03-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDonation', '0005_rename_supplied_donations_distributed'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Delivered'), (3, 'Distributed')], default=1),
            preserve_default=False,
        ),
    ]
