# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making
蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
Copyright (C) 2017-2022THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.

We undertake not to change the open source license (MIT license) applicable

to the current version of the project delivered to anyone in the future.
"""
# Generated by Django 3.2.12 on 2022-05-07 03:13

from django.db import migrations, models


from paasng.utils.i18n.migrate import copy_field


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_move_app_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='name_en',
            field=models.CharField(default='', max_length=20, verbose_name='应用名称(英文)', help_text="目前仅用于 S-Mart 应用"),
            preserve_default=False,
        ),
        migrations.RunPython(code=copy_field('applications', 'application', 'name', 'name_en')),
    ]
