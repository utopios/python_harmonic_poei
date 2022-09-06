import pytest


@pytest.mark.usefixtures("demo_fixture")
class TestClass():
    def test_method_1(self):
        pass


@pytest.mark.usefixtures("demo_fixture")
class TestClass2():
    def test_method_1(self):
        pass


@pytest.fixture(scope='class')
def demo_fixture():
    pass