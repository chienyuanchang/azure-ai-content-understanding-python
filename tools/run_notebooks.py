import os
import sys
import traceback
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_all_notebooks(path="."):
    abs_path = os.path.abspath(path)
    print(f"🔍 Scanning for notebooks in: {abs_path}\n")

    notebook_found = 0
    success_notebooks = []
    failed_notebooks = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".ipynb") and not file.startswith("."):
                notebook_found += 1
                notebook_path = os.path.join(root, file)
                print(f"▶️ Running: {notebook_path}")

                with open(notebook_path, encoding="utf-8") as f:
                    nb = nbformat.read(f, as_version=4)

                ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

                try:
                    ep.preprocess(nb, {"metadata": {"path": root}})
                    print(f"✅ Success: {notebook_path}\n")
                    success_notebooks.append(notebook_path)
                except Exception as e:
                    print(f"❌ Failed: {notebook_path}\nError: {e}\n")
                    failed_notebooks.append((notebook_path, e))

    # 📋 Summary
    print("🧾 Notebook Execution Summary")
    print(f"✅ {len(success_notebooks)} succeeded")
    print(f"❌ {len(failed_notebooks)} failed\n")

    if failed_notebooks:
        for nb, error in failed_notebooks:
            print(f" - {nb}")
            # Show the full traceback if available
            if hasattr(error, "__traceback__"):
                tb_lines = traceback.format_exception(type(error), error, error.__traceback__)
                print("".join("     " + line for line in tb_lines[-3:]))  # last 3 lines
            else:
                lines = error.strip().splitlines()
                if lines:
                    for line in lines[:3]:  # first 3 lines if no traceback
                        print(f"     ↳ {line}")
                else:
                    print("     ↳ (No error message captured)")
        sys.exit(1)

    if notebook_found == 0:
        print("❌ No notebooks were found. Check the folder path or repo contents.")
        sys.exit(1)
        print("🏁 All notebooks completed successfully.")


if __name__ == "__main__":
    run_all_notebooks("notebooks")
