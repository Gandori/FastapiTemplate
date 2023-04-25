import os
import time


def pytest_sessionstart() -> None:
    os.system('bash start_docker_compose_dev.sh')
    time.sleep(10)


def pytest_sessionfinish() -> None:
    time.sleep(5)
    os.system('docker-compose down')


def pytest_collection_modifyitems(items):
    numrepeats = 100
    items.extend(items * (numrepeats - 1))
