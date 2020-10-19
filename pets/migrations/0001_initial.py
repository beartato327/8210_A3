# Generated by Django 3.1.2 on 2020-10-19 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pet_type', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat')], max_length=3, verbose_name='type of pet')),
                ('pet_name', models.CharField(max_length=200)),
                ('pet_age', models.DateField()),
                ('pet_breed', models.CharField(max_length=200)),
                ('pet_active', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportName', models.CharField(max_length=200)),
                ('reportType', models.CharField(choices=[('VACCINES', 'Vaccines'), ('SURGERY', 'Surgery'), ('GENERAL', 'General')], max_length=100, verbose_name='type of report')),
                ('reportDetails', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='pets.pet')),
            ],
        ),
    ]
