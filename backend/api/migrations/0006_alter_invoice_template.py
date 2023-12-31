# Generated by Django 4.2.6 on 2023-10-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_invoice_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='template',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices_received', to='api.template'),
        ),
    ]
