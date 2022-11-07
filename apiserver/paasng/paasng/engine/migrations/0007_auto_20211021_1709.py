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
# Generated by Django 2.2.17 on 2021-10-21 09:09

from django.db import migrations, models
import paasng.engine.models.deployment


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20210817_1518'),
        ('modules', '0004_module_user_preferred_root_domain'),
        ('engine', '0006_auto_20210426_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='path_prefix',
            field=models.CharField(default='/', help_text='the accessable path for current domain', max_length=64),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='advanced_options',
            field=paasng.engine.models.deployment.AdvancedOptionsField(null=True, verbose_name='高级选项'),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together={('module', 'name', 'environment', 'path_prefix')},
        ),
    ]
