import os
import sys
import platform
import pytest
import requests

# 1) Skipped because a feature is not implemented yet
@pytest.mark.skip(reason="Feature not implemented yet")
def test_feature_not_implemented():
    assert True


# 2) Runs only on Linux and skips on Windows (and other OS)
@pytest.mark.skipif(platform.system() != "Linux", reason="Runs only on Linux")
def test_only_on_linux():
    assert True


# 3) API health endpoint
# If status code is not 200 -> skip dynamically
def test_api_health_skip_if_not_200():
    url = os.getenv("HEALTH_URL", "http://localhost:8000/health")

    try:
        res = requests.get(url, timeout=5)
    except requests.RequestException as e:
        pytest.skip(f"Health endpoint not reachable: {e}")

    if res.status_code != 200:
        pytest.skip(f"Health check not OK, status={res.status_code}")

    assert res.status_code == 200


# 4) Mark a failing test as xfail with reason "Bug #123"
@pytest.mark.xfail(reason="Bug #123")
def test_known_bug_123():
    assert 1 == 2

#5) Five parameterized cases
cases = [
    (1, 1, 2, None),
    (2, 3, 5, None),
    pytest.param(10, 20, 999, marks=pytest.mark.xfail(reason="Known bug #A")),
    pytest.param(7, 8, 999, marks=pytest.mark.xfail(reason="Known bug #B")),
    (4, 6, 10, None),
]

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected,_", cases)
def test_add_param_xfail_only_some(a, b, expected, _):
    assert add(a, b) == expected