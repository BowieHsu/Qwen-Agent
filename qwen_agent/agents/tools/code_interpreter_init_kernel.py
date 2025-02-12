import json  # noqa
import math  # noqa
import os  # noqa
import re  # noqa
import signal

import matplotlib  # noqa
import matplotlib.pyplot as plt
import numpy as np  # noqa
import pandas as pd  # noqa
import seaborn as sns
from matplotlib.font_manager import FontProperties
from sympy import Eq, solve, symbols  # noqa


def input(*args, **kwargs):
    raise NotImplementedError('Python input() function is disabled.')


def _m6_timout_handler(_signum=None, _frame=None):
    raise TimeoutError('M6_CODE_INTERPRETER_TIMEOUT')


signal.signal(signal.SIGALRM, _m6_timout_handler)


class _M6CountdownTimer:
    @classmethod
    def start(cls, timeout: int):
        try:
            signal.alarm(timeout)
        except AttributeError:  # windows
            pass  # TODO: I haven't found a solution that works with jupyter yet.

    @classmethod
    def cancel(cls):
        try:
            signal.alarm(0)
        except AttributeError:  # windows
            pass  # TODO


sns.set_theme()

_m6_font_prop = FontProperties(fname='{{M6_FONT_PATH}}')
plt.rcParams['font.family'] = _m6_font_prop.get_name()
