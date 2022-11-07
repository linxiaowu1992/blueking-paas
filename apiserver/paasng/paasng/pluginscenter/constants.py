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
from blue_krill.data_types.enum import EnumField, StructuredEnum


class PluginReleaseMethod(str, StructuredEnum):
    """插件发布方式"""

    CODE = EnumField("code", label="源码发布")
    SOURCE_PACKAGE = EnumField("sourcePackage", label="源码包发布")
    IMAGE = EnumField("image", label="镜像发布")


class PluginReleaseVersionRule(str, StructuredEnum):
    """插件发布版本号规则"""

    AUTOMATIC = EnumField("automatic", label="自动生成 semver")
    REVISION = EnumField("revision", label="与代码分支一致")
    COMMIT_HASH = EnumField("commit-hash", label="与提交哈希一致")
    SELF_FILL = EnumField("self-fill", label="用户自助填写")


class SemverAutomaticType(str, StructuredEnum):
    """语义化版本生成规则"""

    MAJOR = EnumField("major", label="重大版本")
    MINOR = EnumField("minor", label="次版本")
    PATCH = EnumField("patch", label="修正版本")


class ReleaseStageInvokeMethod(str, StructuredEnum):
    """发布步骤触发方式"""

    DEPLOY_API = EnumField("deployAPI", label="部署接口")
    PIPELINE = EnumField("pipeline", label="流水线")
    SUBPAGE = EnumField("subpage", label="子页面")
    ITSM = EnumField("itsm", label="itsm 审批流程")
    BUILTIN = EnumField("builtin", label="内置功能(完善市场信息market, 灰度grayScale, 上线online)")


class PluginStatus(str, StructuredEnum):
    """插件状态"""

    WAITING_APPROVAL = EnumField("waiting-approval", label="创建审批中")
    DEVELOPING = EnumField("developing", label="开发中")
    RELEASING = EnumField("releasing", label="发布中")
    RELEASED = EnumField("released", label="已发布")


class PluginRole(int, StructuredEnum):
    """插件角色"""

    ADMINISTRATOR = EnumField(2, label='管理员')
    DEVELOPER = EnumField(3, label='开发者')


class MarketInfoStorageType(str, StructuredEnum):
    """市场信息存储类型"""

    THIRD_PARTY = EnumField("third-party", label="仅存储在第三方系统")
    PLATFORM = EnumField("platform", label="仅存储在插件开发中心")
    BOTH = EnumField("both", label="同时存储在插件开发中心和第三方系统")


class PluginReleaseStatus(str, StructuredEnum):
    """插件发布状态"""

    SUCCESSFUL = EnumField('successful', label='成功')
    FAILED = EnumField('failed', label='失败')
    PENDING = EnumField('pending', label='等待')
    INITIAL = EnumField("initial", label="初始化")
    INTERRUPTED = EnumField('interrupted', label='已中断')


class LogTimeChoices(str, StructuredEnum):
    """日志搜索-日期范围可选值"""

    FIVE_MINUTES = EnumField("5m", label="5分钟")
    ONE_HOUR = EnumField("1h", label="1小时")
    THREE_HOURS = EnumField("3h", label="3小时")
    SIX_HOURS = EnumField("6h", label="6小时")
    TWELVE_HOURS = EnumField("12h", label="12小时")
    ONE_DAY = EnumField("1d", label="1天")
    THREE_DAYS = EnumField("3d", label="3天")
    SEVEN_DAYS = EnumField("7d", label="7天")
    CUSTOMIZED = EnumField("customized", label="自定义")
