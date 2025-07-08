# run_notebooks.py

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_all_notebooks(path='.'):
    print(f"🔍 Scanning for notebooks in: {os.path.abspath(path)}\n")

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".ipynb") and not file.startswith("."):
                notebook_path = os.path.join(root, file)
                print(f"▶️ Running: {notebook_path}")

                with open(notebook_path, encoding="utf-8") as f:
                    nb = nbformat.read(f, as_version=4)

                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

                try:
                    ep.preprocess(nb, {'metadata': {'path': root}})
                    print(f"✅ Success: {notebook_path}\n")
                except Exception as e:
                    print(f"❌ Failed: {notebook_path}\nError: {e}\n")
                    raise RuntimeError(f"Notebook execution failed: {notebook_path}") from e


if __name__ == "__main__":
    run_all_notebooks("/workspaces/azure-ai-content-understanding-python/notebooks")
