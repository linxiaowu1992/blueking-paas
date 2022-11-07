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
from paasng.utils.basic import make_app_pattern, re_path

from . import views

urlpatterns = [
    re_path(
        r'^api/bkapps/applications/lists/latest/',
        views.LatestApplicationsViewSet.as_view(),
        name='api.applications.latest',
    ),
    re_path(
        make_app_pattern(r'/operations/', include_envs=False),
        views.ApplicationOperationsViewSet.as_view({'get': 'list'}),
        name='api.bkapps.application.operations',
    ),
]

# System APIs

urlpatterns += [
    re_path(
        r'^sys/api/operations/',
        views.SysOperationsViewSet.as_view({'post': 'create'}),
        name='sys_api.operations',
    ),
]
