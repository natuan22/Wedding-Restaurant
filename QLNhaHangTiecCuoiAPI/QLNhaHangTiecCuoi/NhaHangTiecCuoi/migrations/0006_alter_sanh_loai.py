# Generated by Django 4.0.4 on 2022-05-09 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NhaHangTiecCuoi', '0005_sanh_ghi_chu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanh',
            name='loai',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanhs', to='NhaHangTiecCuoi.loaisanh'),
        ),
    ]
