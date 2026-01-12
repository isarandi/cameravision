# cameravision

**This package has been renamed to [deltacamera](https://github.com/isarandi/deltacamera).**

Please update your imports:

```python
# Old
from cameravision import Camera

# New
from deltacamera import Camera
```

Install the new package:

```bash
pip install deltacamera
```

This transitional package (`cameravision`) depends on `deltacamera` and re-exports all
its symbols for backwards compatibility. It will be removed in a future release.