from new_project.utils.singleton import Singleton


def test_singleton():
    """Test the Singleton class."""

    class A(metaclass=Singleton):
        def __init__(self):
            self.x = 1

    a1 = A()
    a2 = A()

    assert a1 is a2
    assert a1.x == 1
