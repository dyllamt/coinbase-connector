import os
import subprocess


def get_project_root():
    integration_tests_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.dirname(integration_tests_dir)
    project_root = os.path.dirname(tests_dir)
    return project_root


project_root = get_project_root()


def run_script(script_path: str):
    absolute_path = os.path.join(project_root, script_path)
    result = subprocess.run(
        ["bash", absolute_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
    )
    return result.stdout, result.stderr
