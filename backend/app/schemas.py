"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class CollectionEntry(BaseModel):
    """藏品档案明细结构。"""

    field_0: str | None = None  # 藏品编号
    field_1: str | None = None  # 藏品名称
    field_2: str | None = None  # 藏品类别
    field_3: str | None = None  # 年代
    field_4: str | None = None  # 质地
    field_5: str | None = None  # 来源方式
    field_6: str | None = None  # 入藏日期
    field_7: str | None = None  # 藏品状态

class RelicEntry(BaseModel):
    """文物本体明细结构。"""

    field_0: str | None = None  # 文物编号
    field_1: str | None = None  # 文物名称
    field_2: str | None = None  # 文物级别
    field_3: str | None = None  # 尺寸规格
    field_4: str | None = None  # 文物重量
    field_5: str | None = None  # 完残程度
    field_6: str | None = None  # 存放位置
    field_7: str | None = None  # 文物状态

class DiseaseEntry(BaseModel):
    """病害调查记录明细结构。"""

    field_0: str | None = None  # 调查编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 病害类型
    field_3: str | None = None  # 病害面积
    field_4: str | None = None  # 病害程度
    field_5: str | None = None  # 调查日期
    field_6: str | None = None  # 调查人员
    field_7: str | None = None  # 调查状态

class SchemeEntry(BaseModel):
    """修复方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 病害概况
    field_3: str | None = None  # 修复目标
    field_4: str | None = None  # 技术路线
    field_5: str | None = None  # 材料选择
    field_6: str | None = None  # 编制人员
    field_7: str | None = None  # 方案状态

class ProcessEntry(BaseModel):
    """修复工序明细结构。"""

    field_0: str | None = None  # 工序编号
    field_1: str | None = None  # 所属方案
    field_2: str | None = None  # 工序名称
    field_3: str | None = None  # 工序顺序
    field_4: str | None = None  # 工艺要求
    field_5: str | None = None  # 计划工时
    field_6: str | None = None  # 实施人员
    field_7: str | None = None  # 工序状态

class MaterialEntry(BaseModel):
    """修复材料明细结构。"""

    field_0: str | None = None  # 材料编号
    field_1: str | None = None  # 材料名称
    field_2: str | None = None  # 材料规格
    field_3: str | None = None  # 配比说明
    field_4: str | None = None  # 生产厂商
    field_5: str | None = None  # 入库日期
    field_6: str | None = None  # 有效期
    field_7: str | None = None  # 材料状态

class EnvironmentEntry(BaseModel):
    """环境监测记录明细结构。"""

    field_0: str | None = None  # 监测编号
    field_1: str | None = None  # 监测点位
    field_2: str | None = None  # 展厅名称
    field_3: str | None = None  # 环境温度
    field_4: str | None = None  # 相对湿度
    field_5: str | None = None  # 光照度
    field_6: str | None = None  # 采集时间
    field_7: str | None = None  # 监测状态

class BoxEntry(BaseModel):
    """囊匣明细结构。"""

    field_0: str | None = None  # 囊匣编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 囊匣材质
    field_3: str | None = None  # 内衬材料
    field_4: str | None = None  # 尺寸规格
    field_5: str | None = None  # 制作人员
    field_6: str | None = None  # 完成日期
    field_7: str | None = None  # 囊匣状态

class ScanEntry(BaseModel):
    """三维扫描记录明细结构。"""

    field_0: str | None = None  # 扫描编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 扫描设备
    field_3: str | None = None  # 扫描精度
    field_4: str | None = None  # 点云数量
    field_5: str | None = None  # 扫描日期
    field_6: str | None = None  # 操作人员
    field_7: str | None = None  # 扫描状态

class RubbingEntry(BaseModel):
    """拓片明细结构。"""

    field_0: str | None = None  # 拓片编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 拓片类型
    field_3: str | None = None  # 纸张规格
    field_4: str | None = None  # 墨色描述
    field_5: str | None = None  # 制作日期
    field_6: str | None = None  # 制作人员
    field_7: str | None = None  # 拓片状态

class ExhibitEntry(BaseModel):
    """展陈项目明细结构。"""

    field_0: str | None = None  # 展陈编号
    field_1: str | None = None  # 展览名称
    field_2: str | None = None  # 展厅位置
    field_3: str | None = None  # 展品数量
    field_4: str | None = None  # 布展日期
    field_5: str | None = None  # 撤展日期
    field_6: str | None = None  # 策展人员
    field_7: str | None = None  # 展陈状态

class TransportEntry(BaseModel):
    """借展运输单明细结构。"""

    field_0: str | None = None  # 运输编号
    field_1: str | None = None  # 借展单位
    field_2: str | None = None  # 展品清单
    field_3: str | None = None  # 运输方式
    field_4: str | None = None  # 押运人员
    field_5: str | None = None  # 出借日期
    field_6: str | None = None  # 归还日期
    field_7: str | None = None  # 运输状态

class PestEntry(BaseModel):
    """虫害防治单明细结构。"""

    field_0: str | None = None  # 防治编号
    field_1: str | None = None  # 防治区域
    field_2: str | None = None  # 有害生物
    field_3: str | None = None  # 危害等级
    field_4: str | None = None  # 防治方式
    field_5: str | None = None  # 用药名称
    field_6: str | None = None  # 防治日期
    field_7: str | None = None  # 防治状态

class AcceptEntry(BaseModel):
    """保护验收单明细结构。"""

    field_0: str | None = None  # 验收编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 验收项目
    field_3: str | None = None  # 验收标准
    field_4: str | None = None  # 验收结论
    field_5: str | None = None  # 验收专家
    field_6: str | None = None  # 验收日期
    field_7: str | None = None  # 验收状态

class ShelfEntry(BaseModel):
    """库房排架明细结构。"""

    field_0: str | None = None  # 排架编号
    field_1: str | None = None  # 库房名称
    field_2: str | None = None  # 排架位置
    field_3: str | None = None  # 存放文物数
    field_4: str | None = None  # 柜架类型
    field_5: str | None = None  # 上次整理日
    field_6: str | None = None  # 保管人员
    field_7: str | None = None  # 排架状态

class ExtractEntry(BaseModel):
    """提取单明细结构。"""

    field_0: str | None = None  # 提取编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 提取事由
    field_3: str | None = None  # 提取人
    field_4: str | None = None  # 审批人
    field_5: str | None = None  # 提取日期
    field_6: str | None = None  # 归还日期
    field_7: str | None = None  # 提取状态

class PhotoEntry(BaseModel):
    """影像资料明细结构。"""

    field_0: str | None = None  # 影像编号
    field_1: str | None = None  # 关联文物
    field_2: str | None = None  # 拍摄视角
    field_3: str | None = None  # 分辨率
    field_4: str | None = None  # 拍摄设备
    field_5: str | None = None  # 拍摄日期
    field_6: str | None = None  # 摄影人员
    field_7: str | None = None  # 影像状态

class LogEntry(BaseModel):
    """保护日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 记录对象
    field_2: str | None = None  # 记录类型
    field_3: str | None = None  # 记录日期
    field_4: str | None = None  # 环境温湿度
    field_5: str | None = None  # 异常情况
    field_6: str | None = None  # 记录人员
    field_7: str | None = None  # 日志状态
