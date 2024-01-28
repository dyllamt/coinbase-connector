import os
import subprocess
import sys

import pytest


def get_project_root():
    integration_tests_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.dirname(integration_tests_dir)
    project_root = os.path.dirname(tests_dir)
    return project_root


project_root = get_project_root()


def run_script(script_path: str):
    absolute_path = os.path.join(project_root, script_path)
    subprocess.run(["bash", absolute_path], stdout=sys.stdout, stderr=sys.stderr, check=True)


def install_strimzi():
    run_script("scripts/install-strimzi.sh")


def deploy_kafka():
    run_script("scripts/deploy-kafka.sh")


def deploy_connector():
    run_script("scripts/deploy-connector.sh")


@pytest.fixture(scope="module")
def kubernetes_services():
    install_strimzi()
    deploy_kafka()
    deploy_connector()

    yield
