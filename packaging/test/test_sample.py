def setup_module():
    print "X" * 80, "module setup"


def teardown_module():
    print "X" * 80, "module teardown"


def test_alpha():
    assert True
    assert False


def test_bravo():
    assert True
    assert False


class TestSample:

    def setup_method(self, method):
        print "X" * 80, "setup, method-level"

    def teardown_method(self, method):
        print "X" * 80, "teardown, method-level"

    def test_alpha(self):
        assert True
        assert False

    def test_bravo(self):
        assert True
        assert False
