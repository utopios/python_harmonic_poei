class TestClassDemo:

    value = 3

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

    def test_three(self):
        assert TestClassDemo.value == 3

# not used in our case
# if __name__ == "__main__":
#     test = TestClassDemo()
#     test.test_one()