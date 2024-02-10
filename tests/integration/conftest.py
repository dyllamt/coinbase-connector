import pytest

from coinbase.utils import run_script


def install_strimzi():
    run_script("scripts/install-strimzi.sh")
    print("strimzi installed")


def deploy_kafka():
    run_script("scripts/deploy-kafka.sh")
    print("kafka deployed")


def deploy_connector():
    run_script("scripts/deploy-connector.sh")
    print("connector deployed")


def teardown():
    run_script("scripts/teardown.sh")
    print("teardown complete")


@pytest.fixture(scope="module")
def kubernetes_services():
    install_strimzi()
    deploy_kafka()
    deploy_connector()
    yield
    teardown()
