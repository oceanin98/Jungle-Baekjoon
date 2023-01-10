from collections.abc import Iterable, Iterator
from typing import Any, TypeVar, overload
from typing_extensions import TypeAlias

_CallExpr: TypeAlias = Any  # mypy.nodes._CallExpr
_Context: TypeAlias = Any  # mypy.nodes._Context
_Expression: TypeAlias = Any  # mypy.nodes._Expression
_JsonDict: TypeAlias = Any  # mypy.nodes._JsonDict
_NameExpr: TypeAlias = Any  # mypy.nodes._NameExpr
_Statement: TypeAlias = Any  # mypy.nodes._Statement
_TypeInfo: TypeAlias = Any  # mypy.nodes._TypeInfo
_ClassDefContext: TypeAlias = Any  # mypy.plugin._ClassDefContext
_DynamicClassDefContext: TypeAlias = Any  # mypy.plugin._DynamicClassDefContext
_SemanticAnalyzerPluginInterface: TypeAlias = Any  # mypy.plugin._SemanticAnalyzerPluginInterface
_Type: TypeAlias = Any  # mypy.types._Type

_TArgType = TypeVar("_TArgType", bound=_CallExpr | _NameExpr)

class SQLAlchemyAttribute:
    name: Any
    line: Any
    column: Any
    type: Any
    info: Any
    def __init__(self, name: str, line: int, column: int, typ: _Type | None, info: _TypeInfo) -> None: ...
    def serialize(self) -> _JsonDict: ...
    def expand_typevar_from_subtype(self, sub_type: _TypeInfo) -> None: ...
    @classmethod
    def deserialize(cls, info: _TypeInfo, data: _JsonDict, api: _SemanticAnalyzerPluginInterface) -> SQLAlchemyAttribute: ...

def name_is_dunder(name): ...
def establish_as_sqlalchemy(info: _TypeInfo) -> None: ...
def set_is_base(info: _TypeInfo) -> None: ...
def get_is_base(info: _TypeInfo) -> bool: ...
def has_declarative_base(info: _TypeInfo) -> bool: ...
def set_has_table(info: _TypeInfo) -> None: ...
def get_has_table(info: _TypeInfo) -> bool: ...
def get_mapped_attributes(info: _TypeInfo, api: _SemanticAnalyzerPluginInterface) -> list[SQLAlchemyAttribute] | None: ...
def set_mapped_attributes(info: _TypeInfo, attributes: list[SQLAlchemyAttribute]) -> None: ...
def fail(api: _SemanticAnalyzerPluginInterface, msg: str, ctx: _Context) -> None: ...
def add_global(ctx: _ClassDefContext | _DynamicClassDefContext, module: str, symbol_name: str, asname: str) -> None: ...
@overload
def get_callexpr_kwarg(callexpr: _CallExpr, name: str, *, expr_types: None = ...) -> _CallExpr | _NameExpr | None: ...
@overload
def get_callexpr_kwarg(callexpr: _CallExpr, name: str, *, expr_types: tuple[type[_TArgType], ...]) -> _TArgType | None: ...
def flatten_typechecking(stmts: Iterable[_Statement]) -> Iterator[_Statement]: ...
def unbound_to_instance(api: _SemanticAnalyzerPluginInterface, typ: _Type) -> _Type: ...
def info_for_cls(cls, api: _SemanticAnalyzerPluginInterface) -> _TypeInfo | None: ...
def expr_to_mapped_constructor(expr: _Expression) -> _CallExpr: ...