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
# Generated by Django 3.2.12 on 2022-04-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_product_visiable_labels'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketconfig',
            name='prefer_https',
            field=models.BooleanField(null=True, verbose_name='当平台提供 https 协议时，是否优先使用'),
        ),
        migrations.AlterField(
            model_name='marketconfig',
            name='auto_enable_when_deploy',
            field=models.BooleanField(null=True, verbose_name='成功部署主模块正式环境后, 是否自动打开市场'),
        ),
    ]
