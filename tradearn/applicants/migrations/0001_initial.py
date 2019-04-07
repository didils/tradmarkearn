# Generated by Django 2.0.13 on 2019-04-07 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=140, null=True)),
                ('representName', models.CharField(blank=True, max_length=140, null=True)),
                ('representNameEn', models.CharField(blank=True, max_length=140, null=True)),
                ('patentApplicantNumber', models.CharField(blank=True, max_length=140, null=True)),
                ('socialNumber', models.CharField(blank=True, max_length=140, null=True)),
                ('socialNumberFirm', models.CharField(blank=True, max_length=140, null=True)),
                ('socialNumberFirmReg', models.CharField(blank=True, max_length=140, null=True)),
                ('representNameFirm', models.CharField(blank=True, max_length=140, null=True)),
                ('socialNumberFirmPresident', models.CharField(blank=True, max_length=140, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
