import pytest

from coinbase.utils import run_script


def setup():
    out, err = run_script("scripts/setup.sh")
    print(out, err)


def teardown():
    out, err = run_script("scripts/teardown.sh")
    print(out, err)


@pytest.fixture(scope="module")
def kubernetes_services():
    setup()
    yield
    teardown()
