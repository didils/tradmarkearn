# Generated by Django 2.0.13 on 2019-04-07 16:38

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OAreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_file', models.DateField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('possibility', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('examinerComment', models.TextField(blank=True, null=True)),
                ('attorneyComment', models.TextField(blank=True, null=True)),
                ('clientGiveup', models.BooleanField(default=False)),
                ('is_notified', models.BooleanField(default=False)),
                ('image1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('date_of_image1', models.DateField(blank=True, null=True)),
                ('application_number1', models.CharField(blank=True, max_length=80, null=True)),
                ('applicant1', models.CharField(blank=True, max_length=80, null=True)),
                ('image2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('date_of_image2', models.DateField(blank=True, null=True)),
                ('application_number2', models.CharField(blank=True, max_length=80, null=True)),
                ('applicant2', models.CharField(blank=True, max_length=80, null=True)),
                ('image3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('date_of_image3', models.DateField(blank=True, null=True)),
                ('application_number3', models.CharField(blank=True, max_length=80, null=True)),
                ('applicant3', models.CharField(blank=True, max_length=80, null=True)),
                ('image4', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('date_of_image4', models.DateField(blank=True, null=True)),
                ('application_number4', models.CharField(blank=True, max_length=80, null=True)),
                ('applicant4', models.CharField(blank=True, max_length=80, null=True)),
                ('image5', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='')),
                ('date_of_image5', models.DateField(blank=True, null=True)),
                ('application_number5', models.CharField(blank=True, max_length=80, null=True)),
                ('applicant5', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
