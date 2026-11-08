from src.calculator import add


class TestBasicAddition:
    def test_add_two_numbers(self):
        assert add(2, 3) == 5
