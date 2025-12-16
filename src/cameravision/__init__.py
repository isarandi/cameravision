"""CameraVision: Camera calibration manipulation and image warping for computer vision.

This library provides coordinate transformations between world, camera, and image spaces
with support for Brown-Conrady and Kannala-Brandt (fisheye) lens distortion models.

Example:
    >>> from cameravision import Camera
    >>> cam = Camera(intrinsic_matrix=[[500, 0, 320], [0, 500, 240], [0, 0, 1]])
    >>> cam.world_to_image([[1, 2, 3]])
"""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0"

__all__ = [
    # Core
    "Camera",
    "intrinsics_from_fov",
    "visible_subbox",
    # Reprojection
    "reproject_box",
    "reproject_box_corners",
    "reproject_box_side_midpoints",
    "reproject_box_inscribed_ellipse",
    "reproject_image",
    "reproject_image_fast",
    "reproject_image_points",
    "reproject_mask",
    "reproject_rle_mask",
    "encode_srgb",
    "decode_srgb",
    # Validity
    "get_valid_mask",
    "get_valid_mask_reproj",
]

from cameravision.cameravision import (
    Camera,
    intrinsics_from_fov,
    visible_subbox,
)

from cameravision.reprojection import (
    decode_srgb,
    encode_srgb,
    reproject_box,
    reproject_box_corners,
    reproject_box_inscribed_ellipse,
    reproject_box_side_midpoints,
    reproject_image,
    reproject_image_fast,
    reproject_image_points,
    reproject_mask,
    reproject_rle_mask,
)

from cameravision.validity import (
    get_valid_mask,
    get_valid_mask_reproj,
)

# Set the __module__ attribute of all exported functions/classes to this module.
# This is necessary for sphinx-codeautolink to correctly resolve references like
# `Camera` to `cameravision.Camera` in code blocks. Without this, sphinx-codeautolink
# cannot link names that are imported (e.g., `from cameravision import Camera`) because
# it doesn't know that `Camera` refers to `cameravision.Camera` rather than
# `cameravision.cameravision.Camera`. The _module_original_ attribute preserves the true module
# for use by docs/conf.py's `module_restored` context manager when resolving source links.
for _x in __all__:
    _obj = globals().get(_x)
    if _obj is not None and hasattr(_obj, "__module__"):
        _obj._module_original_ = _obj.__module__
        _obj.__module__ = __name__
