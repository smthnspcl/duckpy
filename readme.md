## duckpy
### how to use it
```python
from duckpy import DuckDuckGo

results = DuckDuckGo.query("Jeff Bezos")
for result in results:
    print(result.title)
    print(result.url)
```