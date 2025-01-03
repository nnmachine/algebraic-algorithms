from test_base import TestBase


class Test(TestBase):
    _test_path = ["tests", "power"]
    _file_name = "test"

    def _run_test(self, in_: str) -> str:
        x, n = in_.split("\n")
        return self._run(x, n)
