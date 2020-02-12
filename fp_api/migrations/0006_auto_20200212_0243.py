# Generated by Django 2.2.5 on 2020-02-12 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fp_api', '0005_auto_20200212_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='min_cpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fp_api.Cpu'),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_gpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fp_api.Gpu'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='cpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fp_api.Cpu'),
        ),
    ]
