from shittybirthdaycards_com.settings.base import *


try:
    from shittybirthdaycards_com.settings.docker import *
except ImportError:
    pass

try:
    from shittybirthdaycards_com.settings.deploy import *
except ImportError:
    pass
