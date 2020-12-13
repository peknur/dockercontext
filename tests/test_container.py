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
