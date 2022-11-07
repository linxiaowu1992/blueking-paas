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
from django.urls import path

from . import views

urlpatterns = [
    path("api/bkplugins/lists/", views.PluginInstanceViewSet.as_view({"get": "list"})),
    path("api/bkplugins/<str:pd_id>/plugins/", views.PluginInstanceViewSet.as_view({"post": "create"})),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/",
        views.PluginInstanceViewSet.as_view({"get": "retrieve", "post": "update"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/",
        views.PluginReleaseViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/schema/",
        views.PluginReleaseViewSet.as_view({"get": "get_release_schema"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/<str:release_id>/",
        views.PluginReleaseViewSet.as_view({"get": "retrieve"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/<str:release_id>/next/",
        views.PluginReleaseViewSet.as_view({"post": "enter_next_stage"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/<str:release_id>/cancel/",
        views.PluginReleaseViewSet.as_view({"post": "cancel_release"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/releases/<str:release_id>/stages/<str:stage_id>/",
        views.PluginReleaseStageViewSet.as_view({"get": "retrieve"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/market/",
        views.PluginMarketViewSet.as_view({"get": "retrieve", "post": "upsert"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/logs/standard_output/",
        views.PluginLogViewSet.as_view({"post": "query_standard_output_logs"}),
    ),
    path(
        "api/bkplugins/<str:pd_id>/plugins/<str:plugin_id>/logs/structure_logs/",
        views.PluginLogViewSet.as_view({"post": "query_structure_logs"}),
    ),
    path(
        "api/bkplugins/plugin_definitions/schemas/",
        views.SchemaViewSet.as_view({"get": "get_plugins_schema"}),
    ),
    path(
        "api/bkplugins/plugin_definitions/<str:pd_id>/market_schema/",
        views.SchemaViewSet.as_view({"get": "get_market_schema"}),
    ),
    path(
        "api/bkplugins/plugin_definitions/<str:pd_id>/basic_info_schema/",
        views.SchemaViewSet.as_view({"get": "get_basic_info_schema"}),
    ),
]
