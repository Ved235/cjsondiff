from . import jsondiff

for _name in jsondiff.__all__:
    globals()[_name] = getattr(jsondiff, _name)

__all__ = [*jsondiff.__all__, "jsondiff"]
