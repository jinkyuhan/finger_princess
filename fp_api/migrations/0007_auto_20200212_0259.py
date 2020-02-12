# Generated by Django 2.2.5 on 2020-02-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp_api', '0006_auto_20200212_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='category_tag',
        ),
        migrations.AlterField(
            model_name='laptop',
            name='display',
            field=models.IntegerField(choices=[(13, '13인치 (32~34)cm'), (14, '14인치 (35~36)cm'), (15, '15인치 (37~39)cm'), (16, '16인치 (40~42)cm'), (17, '17인치 (43~44)cm')]),
        ),
    ]
