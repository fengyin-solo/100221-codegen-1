"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import collection as router_collection
from app.routers import relic as router_relic
from app.routers import disease as router_disease
from app.routers import scheme as router_scheme
from app.routers import process as router_process
from app.routers import material as router_material
from app.routers import environment as router_environment
from app.routers import box as router_box
from app.routers import scan as router_scan
from app.routers import rubbing as router_rubbing
from app.routers import exhibit as router_exhibit
from app.routers import transport as router_transport
from app.routers import pest as router_pest
from app.routers import accept as router_accept
from app.routers import shelf as router_shelf
from app.routers import extract as router_extract
from app.routers import photo as router_photo
from app.routers import log as router_log

ROUTERS = [router_collection, router_relic, router_disease, router_scheme, router_process, router_material, router_environment, router_box, router_scan, router_rubbing, router_exhibit, router_transport, router_pest, router_accept, router_shelf, router_extract, router_photo, router_log]
