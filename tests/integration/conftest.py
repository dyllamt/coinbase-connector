import pytest

from coinbase.utils import run_script


def setup():
    run_script("scripts/setup.sh")


def teardown():
    run_script("scripts/teardown.sh")
    print("teardown complete")


@pytest.fixture(scope="module")
def kubernetes_services():
    setup()
    yield
    teardown()
