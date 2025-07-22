import os
import sys
import traceback
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_path, root):
    """Execute a single notebook."""
    try:
        with open(notebook_path, encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": root}})
        return True, None
    except Exception as e:
        return False, str(e)


def run_all_notebooks(path="."):
    abs_path = os.path.abspath(path)
    print(f"🔍 Scanning for notebooks in: {abs_path}\n")

    notebook_found = 0
    success_notebooks = []
    failed_notebooks = []

    for root, _, files in os.walk(abs_path):
        for file in files:
            if file.endswith(".ipynb") and not file.startswith("."):
                notebook_found += 1
                notebook_path = os.path.join(root, file)
                print(f"▶️ Running: {notebook_path}")

                success, error = run_notebook(notebook_path, root)

                if success:
                    print(f"✅ Success: {notebook_path}\n")
                    success_notebooks.append(notebook_path)
                else:
                    print(f"❌ Failed: {notebook_path}\nError: {error}\n")
                    failed_notebooks.append((notebook_path, error))

    # 📋 Summary
    print("🧾 Notebook Execution Summary")
    print(f"✅ {len(success_notebooks)} succeeded")
    print(f"❌ {len(failed_notebooks)} failed\n")

    if failed_notebooks:
        print("🚨 Failed notebooks:")
        for nb, error in failed_notebooks:
            last_line = error.strip().splitlines()[-1] if error else "Unknown error"
            print(f" - {nb}\n   ↳ {last_line}")
        sys.exit(1)

    if notebook_found == 0:
        print("❌ No notebooks were found. Check the folder path or repo contents.")
        sys.exit(1)

    print("🏁 All notebooks completed successfully.")


if __name__ == "__main__":
    target_path = sys.argv[1] if len(sys.argv) > 1 else "notebooks"
    run_all_notebooks(target_path)
