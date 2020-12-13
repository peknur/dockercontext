"""
 ref:
    https://docs.docker.com/engine/api/sdk/
    https://docker-py.readthedocs.io/en/stable/containers.html
"""
import time
from typing import Dict, Optional

import docker
from docker import errors
from docker.models import containers
from requests.exceptions import ReadTimeout


class ContextError(Exception):
    pass


class Context:
    STATE_RUNNING = "running"

    def __init__(self,
                 image: str,
                 ports: Dict[str, int],
                 command: Optional[str] = None,
                 remove: bool = True,
                 start_timeout: int = 20) -> None:
        self.image = image
        self.ports = ports
        self.command = command
        self.remove = remove
        self.start_timeout = start_timeout
        self.id = None
        self.container: Optional[containers.Container] = None
        self.client = docker.from_env()

    def run(self) -> None:
        """
         raises:
            docker.errors.ContainerError – If the container exits with a non-zero exit code and detach is False.
            docker.errors.ImageNotFound – If the specified image does not exist.
            docker.errors.APIError – If the server returns an error.
            RuntimeError - if 'run' returns unexpected type
        """
        resp = self.client.containers.run(
            self.image,
            detach=True,
            remove=self.remove,
            auto_remove=self.remove,
            ports=self.ports,
            command=self.command
        )
        if not isinstance(resp, containers.Container):
            raise RuntimeError("docker run returned unexpected type: '{}'".format(type(resp)))
        self.container = resp
        i = 1
        while i <= self.start_timeout:
            if self.container.status == self.STATE_RUNNING:
                break
            time.sleep(1)
            self.container.reload()
            i = i+1

    def close(self) -> None:
        if self.container:
            try:
                self.container.stop()
                self.container.wait()
            except (errors.APIError, ReadTimeout) as e:
                pass
        if self.client:
            self.client.close()

        self.container = None
        self.client = None

    def container_id(self) -> str:
        if self.container:
            return str(self.container.id)
        return ""

    def __enter__(self) -> 'Context':
        """
         raises: ContextError
        """
        try:
            self.run()
        except (errors.ContainerError, errors.ImageNotFound, errors.APIError, RuntimeError) as e:
            self.close()
            raise ContextError("Unable to start container") from e
        return self

    def __exit__(self, *args) -> None:
        self.close()
