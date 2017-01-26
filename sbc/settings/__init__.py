from sbc.settings.base import *


try:
    from sbc.settings.docker import *
except ImportError:
    pass

try:
    from sbc.settings.deploy import *
except ImportError:
    pass
