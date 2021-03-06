import sys
import builtins
from typing import Any, Optional, Text
import threading as threading
from collections import namedtuple as namedtuple
from io import BytesIO
from io import StringIO as StringIO
from inspect import getargspec as inspect_getfullargspec
from operator import attrgetter

byte_buffer = BytesIO
dottedgetter = attrgetter

if sys.version_info < (3, 0):
    from itertools import izip_longest
    zip_longest = izip_longest
    import cPickle
    pickle = cPickle
    from urllib import quote_plus as quote_plus, unquote_plus as unquote_plus, quote as quote, unquote as unquote
    from urlparse import parse_qsl as parse_qsl
else:
    from itertools import zip_longest as zip_longest
    import pickle as pickle
    from urllib.parse import (quote_plus as quote_plus, unquote_plus as unquote_plus,
                              parse_qsl as parse_qsl, quote as quote, unquote as unquote)

py36: bool = ...
py33: bool = ...
py32: bool = ...
py3k: bool = ...
py2k: bool = ...
py265: bool = ...
jython: bool = ...
pypy: bool = ...
win32: bool = ...
cpython: bool = ...
next = builtins.next
safe_kwarg: Any = ...

ArgSpec = namedtuple('ArgSpec', ['args', 'varargs', 'keywords', 'defaults'])

def inspect_getargspec(func): ...

string_types: Any = ...
binary_types: Any = ...
binary_type: Any = ...
text_type = Text
int_types: Any = ...
iterbytes: Any = ...

def u(s): ...
def ue(s): ...
def b(s): ...

callable = builtins.callable

def cmp(a, b): ...

print_: Any = ...
import_: Any = ...
itertools_filterfalse: Any = ...
itertools_filter: Any = ...
itertools_imap: Any = ...

def b64encode(x): ...
def b64decode(x): ...

reduce: Any = ...
time_func: Any = ...

def reraise(tp, value, tb: Optional[Any] = ..., cause: Optional[Any] = ...): ...
def raise_from_cause(exception, exc_info: Optional[Any] = ...): ...

exec_: Any = ...

def with_metaclass(meta, *bases): ...
def nested(*managers): ...
