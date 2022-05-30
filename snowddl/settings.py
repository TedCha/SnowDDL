from dataclasses import dataclass, field
from typing import List

from snowddl.blueprint import Ident, ObjectType

@dataclass
class SnowDDLSettings:
    execute_safe_ddl: bool = False
    execute_unsafe_ddl: bool = False
    execute_replace_table: bool = False
    execute_masking_policy: bool = False
    execute_row_access_policy: bool = False
    execute_account_params: bool = False
    execute_network_policy: bool = False
    execute_resource_monitor: bool = False
    refresh_user_passwords: bool = False
    refresh_future_grants: bool = False
    exclude_object_types: List[ObjectType] = field(default_factory=list)
    include_object_types: List[ObjectType] = field(default_factory=list)
    include_databases: List[Ident] = field(default_factory=list)
    max_workers: int = 8
