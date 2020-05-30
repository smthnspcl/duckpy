## duckpy
[![Build Status](https://build.eberlein.io/buildStatus/icon?job=python_duckpy)](https://build.eberlein.io/job/python_duckpy/)
### how to use it
```python
from duckpy import DuckDuckGo

results = DuckDuckGo.query("Jeff Bezos")
for result in results:
    print(result.title)
    print(result.url)
```
