import os
import subprocess


def get_project_root():
    library_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(library_dir)
    project_root = os.path.dirname(src_dir)
    return project_root


project_root = get_project_root()


def run_script(script_path: str):
    absolute_path = os.path.join(project_root, script_path)
    script_dir = os.path.dirname(absolute_path)
    result = subprocess.run(
        ["bash", absolute_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, cwd=script_dir
    )
    return result.stdout, result.stderr
