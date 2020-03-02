# Generated by Django 3.0.3 on 2020-03-02 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doseright', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administration',
            name='medication',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='doseright.Medication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='administration',
            name='title',
            field=models.TextField(),
        ),
    ]