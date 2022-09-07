import pytest

from corrrection_tasks_tests.init import initialized_tasks_db, stop_tasks_db


def pytest_sessionstart(session):

    pass
@pytest.fixture(scope='class', autouse=True)
def setup_db():
    initialized_tasks_db()
    yield
    stop_tasks_db()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    ##Instructions avant le run et la génération du report by pytest
    result_of_runtest_report = yield
    result = result_of_runtest_report.get_result()
    if result.when == "call" and result.failed:
        with open("fails.txt", "a") as file:
            file.write("test failed : \n")
            file.write(str(result.duration) + "\n")
            file.write(result.nodeid + "\n")

    pass