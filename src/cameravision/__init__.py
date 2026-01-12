"""CameraVision is now deltacamera.

This package has been renamed to deltacamera. Please update your imports:

    # Old
    from cameravision import Camera

    # New
    from deltacamera import Camera

This transitional package re-exports everything from deltacamera for backwards
compatibility but will be removed in a future release.
"""

import warnings

warnings.warn(
    "cameravision has been renamed to deltacamera. "
    "Please update your imports: 'from deltacamera import ...' "
    "This compatibility package will be removed in a future release.",
    DeprecationWarning,
    stacklevel=2,
)

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0"

from deltacamera import *  # noqa: E402, F401, F403
from deltacamera import __all__  # noqa: E402, F401