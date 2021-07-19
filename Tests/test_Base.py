import pytest

"Parent of all test class"


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass