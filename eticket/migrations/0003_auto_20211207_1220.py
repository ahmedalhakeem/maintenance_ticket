# Generated by Django 3.1.3 on 2021-12-07 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0002_auto_20211207_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_name', to='eticket.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sect_name', to='eticket.section'),
        ),
    ]
