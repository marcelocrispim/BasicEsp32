from json import dumps as dumpsOld, loads as loadsOld
import numbers
import datetime
import types
from enum import Enum


def objectify(obj):
    """converts the obj(ect) into a json serializable object"""
    if isinstance(obj, numbers.Integral):
        return int(obj)
    elif isinstance(obj, (numbers.Rational, numbers.Real)):
        return float(obj)
    elif isinstance(obj, (datetime.date, datetime.datetime, datetime.time)):
        return obj.isoformat()
    elif isinstance(obj, str):
        return obj
    elif hasattr(obj, "__iter__") or isinstance(obj, types.GeneratorType):
        return list(obj)
    elif hasattr(obj, "xml"):
        return obj.xml()
    elif isinstance(
            obj, Enum
    ):  # Enum class handled specially to address self reference in __dict__
        return dict(name=obj.name, value=obj.value, __class__=obj.__class__.__name__)
    elif hasattr(obj, "__dict__") and hasattr(obj, "__class__"):
        d = dict(obj.__dict__)
        d["__class__"] = obj.__class__.__name__
        return d
    return str(obj)


def dumps(obj, **args):
    return dumpsOld(obj, ensure_ascii=False, sort_keys=True, indent=2, default=objectify, **args)


def loads(obj, **args):
    return loadsOld(obj, **args)
