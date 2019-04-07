# Generated by Django 2.0.13 on 2019-04-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('어플 사용 관련', '어플 사용 관련'), ('변리사/특허법인 관련', '변리사/특허법인 관련'), ('특허/디자인 업무 관련', '특허/디자인 업무 관련'), ('해외 출원 관련', '해외 출원 관련'), ('상표 출원 전반', '상표 출원 전반'), ('비용 관련', '비용 관련'), ('기타', '기타')], max_length=80, null=True),
        ),
    ]
