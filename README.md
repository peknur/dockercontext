# Docker Context
*This is still work in progress ..*  
Run containers using `with` statement.  
```
with client.Context("nginx:alpine", {"80/tcp": 8080}):
    with request.urlopen("http://localhost:8080/") as response:
        self.assertEqual(response.code, 200)
```
```
with client.Context("nginx:alpine", {}) as ctx:
    self.assertEqual(64, len(ctx.container_id()))
self.assertEqual(0, len(ctx.container_id()), ctx.container_id())
```
