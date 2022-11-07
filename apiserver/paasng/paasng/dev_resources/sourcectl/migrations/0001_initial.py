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
# Generated by Django 2.2.17 on 2020-11-27 02:50

import blue_krill.models.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import paasng.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', paasng.utils.models.BkUserField(blank=True, db_index=True, max_length=64, null=True)),
                ('server_name', models.CharField(max_length=32, verbose_name='GIT 服务名称')),
                ('repo_url', models.CharField(max_length=2048, verbose_name='项目地址')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SvnAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account', models.CharField(help_text='目前仅支持固定格式', max_length=64, unique=True)),
                ('user', paasng.utils.models.BkUserField(blank=True, db_index=True, max_length=64, null=True)),
                ('synced_from_paas20', models.BooleanField(default=False, help_text='账户信息是否从 PaaS 2.0 同步过来')),
            ],
        ),
        migrations.CreateModel(
            name='SvnRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', paasng.utils.models.BkUserField(blank=True, db_index=True, max_length=64, null=True)),
                ('server_name', models.CharField(max_length=32, verbose_name='SVN 服务名称')),
                ('repo_url', models.CharField(max_length=2048, verbose_name='项目地址')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepoBasicAuthHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=64, verbose_name='仓库用户名')),
                ('password', blue_krill.models.fields.EncryptField(verbose_name='仓库密码')),
                ('repo_id', models.IntegerField(verbose_name='关联仓库')),
                ('repo_type', models.CharField(max_length=32, verbose_name='仓库类型')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.Module', verbose_name='蓝鲸应用模块')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourcePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(help_text='部署区域', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', paasng.utils.models.BkUserField(blank=True, db_index=True, max_length=64, null=True)),
                ('version', models.CharField(max_length=128, verbose_name='版本号')),
                ('package_name', models.CharField(max_length=128, verbose_name='源码包原始文件名')),
                ('package_size', models.BigIntegerField(verbose_name='源码包大小, bytes')),
                ('storage_engine', models.CharField(help_text='源码包真实存放的存储服务类型', max_length=64, verbose_name='存储引擎')),
                ('storage_path', models.CharField(help_text='源码包在存储服务中存放的位置', max_length=1024, verbose_name='存储路径')),
                ('meta_info', jsonfield.fields.JSONField(help_text='源码包的元信息, 例如 S-Mart 应用的 app.yaml', null=True)),
                ('sha256_signature', models.CharField(max_length=64, null=True, verbose_name='sha256数字签名')),
                ('relative_path', models.CharField(help_text="如果压缩时将目录也打包进来, 入目录名是 foo, 那么 relative_path = 'foo/'", max_length=255, verbose_name='源码入口的相对路径')),
                ('module', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='modules.Module')),
            ],
            options={
                'unique_together': {('module', 'version')},
            },
        ),
    ]
