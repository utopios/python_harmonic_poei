import pytest


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