import pytest

from coinbase.utils import run_script


def install_strimzi():
    run_script("scripts/install-strimzi.sh")


def deploy_kafka():
    run_script("scripts/deploy-kafka.sh")


def deploy_connector():
    run_script("scripts/deploy-connector.sh")


def teardown():
    run_script("scripts/teardown.sh")


@pytest.fixture(scope="module")
def kubernetes_services():
    install_strimzi()
    deploy_kafka()
    deploy_connector()
    yield
    teardown()
