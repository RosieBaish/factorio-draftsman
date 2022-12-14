# instruments.py
# -*- encoding: utf-8 -*-

import pickle

try:  # pragma: no coverage
    import importlib.resources as pkg_resources  # type: ignore
except ImportError:  # pragma: no coverage
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources  # type: ignore

from draftsman import data


with pkg_resources.open_binary(data, "instruments.pkl") as inp:
    _data = pickle.load(inp)
    raw = _data[0]
    index = _data[1]
    names = _data[2]


def add_instrument(name, notes):
    raise NotImplementedError
