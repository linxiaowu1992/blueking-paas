# Generated by Django 3.2.12 on 2022-09-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_template_processes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='repo_url',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='代码仓库信息'),
        ),
    ]
