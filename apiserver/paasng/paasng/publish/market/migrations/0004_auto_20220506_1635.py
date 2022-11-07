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
# Generated by Django 3.2.12 on 2022-05-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20220422_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name_zh_cn',
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, default='', help_text='目前与应用名称保持一致，在 2 个表中修改时都需要相互同步数据，不能超过20个字符', max_length=64,
                                   verbose_name='应用在市场中的名称'),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_zh_cn',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='introduction',
            new_name='introduction_zh_cn',
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, default='', help_text='应用描述', verbose_name='应用描述'),
        ),
        migrations.AddField(
            model_name='product',
            name='introduction_en',
            field=models.TextField(blank=True, default='', help_text='应用简介', verbose_name='应用简介'),
            preserve_default=False,
        ),
    ]
