# Docker Context
Run containers using `with` statement. 
## Install
```
$ pip install dockercontext
```
## Example
```python
import unittest
from urllib import request

from dockercontext import container


class ContextTest(unittest.TestCase):

    def test_response(self):
        with container.Context("nginx:alpine", {"80/tcp": 8080}):
            with request.urlopen("http://localhost:8080/") as response:
                self.assertEqual(response.code, 200)

    def test_container_id(self):
        with container.Context("nginx:alpine", {}) as ctx:
            self.assertEqual(64, len(ctx.container_id()))

        self.assertEqual(0, len(ctx.container_id()), ctx.container_id())
```
Note that although context blocks until container's state is `running` this does not mean that service inside container is ready. 

## Tests
`$ python -m unittest`
