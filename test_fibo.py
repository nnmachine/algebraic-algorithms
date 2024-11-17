from test_base import TestBase


class Test(TestBase):
    _test_path = ["tests", "fibo"]
    _file_name = "test"

    def _run_test(self, in_: str) -> str:
        return self._run(in_)
