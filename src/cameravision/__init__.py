"""Camera library for 3D computer vision tasks."""

import numpy as np
from cameravision.cameravision import (
    Camera,
    # project_points,
    intrinsics_from_fov,
    visible_subbox,
)

from cameravision.reprojection import (
    reproject_box,
    reproject_box_corners,
    reproject_box_side_midpoints,
    reproject_image,
    reproject_image_fast,
    reproject_image_points,
    # reproject_points_homography,
    reproject_mask,
    reproject_rle_mask,
)

from cameravision.validity import (
    get_valid_mask,
    get_valid_mask_reproj,
)


__all__ = [
    "Camera",
    "intrinsics_from_fov",
    "visible_subbox",
    "reproject_box",
    "reproject_box_corners",
    "reproject_box_side_midpoints",
    "reproject_image",
    "reproject_image_fast",
    "reproject_image_points",
    "reproject_mask",
    "reproject_rle_mask",
    "get_valid_mask",
    "get_valid_mask_reproj",
]
