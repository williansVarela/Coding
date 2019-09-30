# Generated by Django 2.2.5 on 2019-09-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_auto_20190928_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='entry_date',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='exit_date',
        ),
        migrations.AddField(
            model_name='animal',
            name='day_of_birth',
            field=models.DateField(default='2000-01-01', verbose_name='Data Nascimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shelter',
            name='date_entry',
            field=models.DateField(default='2000-01-01', verbose_name='Data Entrada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shelter',
            name='date_exit',
            field=models.DateField(blank=True, null=True, verbose_name='Data Saída'),
        ),
    ]