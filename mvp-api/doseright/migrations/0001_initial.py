# Generated by Django 3.0.3 on 2020-03-02 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_name', models.CharField(max_length=128)),
                ('brand_name', models.CharField(max_length=128)),
                ('dosage', models.CharField(max_length=20)),
                ('formulation', models.CharField(max_length=20)),
                ('usage', models.TextField()),
                ('route', models.TextField()),
                ('side_effects', models.TextField()),
                ('storage', models.TextField()),
                ('image', models.URLField()),
                ('video', models.URLField()),
                ('info', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('dose', models.TextField()),
                ('taken', models.BooleanField(blank=True, default=None, null=True)),
                ('special_instructions', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doseright.Medication')),
            ],
        ),
    ]
