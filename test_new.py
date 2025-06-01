print("Hello")
def test_hello():
    assert True, "This test should always pass"
def test_fail():
    assert False, "This test should always fail"
def test_skip():
    import pytest
    pytest.skip("Skipping this test intentionally")
def test_pass():
    assert True, "This test should always pass"
def test_error():
    raise RuntimeError("This test should raise an error")
def test_assertion_error():
    assert False, "This test should raise an assertion error"