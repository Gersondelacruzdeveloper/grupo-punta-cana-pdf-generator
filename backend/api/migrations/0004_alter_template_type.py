# Generated by Django 4.2.6 on 2023-10-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_invoice_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(choices=[('BoardingPass', 'BoardingPass'), ('Invoice', 'Invoice'), ('Advertisement', 'Advertisement')], max_length=50),
        ),
    ]