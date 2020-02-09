
# THIS FILE WAS AUTOMATICALLY GENERATED BY deprecated_modules.py
import sys
from . import _svmlight_format
from ..externals._pep562 import Pep562
from ..utils.deprecation import _raise_dep_warning_if_not_pytest

deprecated_path = 'sklearn.datasets.svmlight_format'
correct_import_path = 'sklearn.datasets'

_raise_dep_warning_if_not_pytest(deprecated_path, correct_import_path)

def __getattr__(name):
    return getattr(_svmlight_format, name)

if not sys.version_info >= (3, 7):
    Pep562(__name__)
