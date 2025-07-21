import os
import sys
import traceback
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_all_notebooks(path='.'):
    print(f"🔍 Scanning for notebooks in: {os.path.abspath(path)}\n")
    notebook_found, success_notebook = 0, 0
    failed_notebooks = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".ipynb") and not file.startswith("."):
                notebook_found += 1
                notebook_path = os.path.join(root, file)
                print(f"▶️ Running: {notebook_path}")

                with open(notebook_path, encoding="utf-8") as f:
                    nb = nbformat.read(f, as_version=4)

                ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

                try:
                    ep.preprocess(nb, {'metadata': {'path': root}})
                    print(f"✅ Success: {notebook_path}\n")
                    success_notebook += 1
                except Exception as e:
                    print(f"❌ Failed: {notebook_path}")
                    traceback.print_exception(type(e), e, e.__traceback__)
                    failed_notebooks.append((notebook_path, e))
                    print()  # extra newline for clarity

    # Summary
    print("=" * 60)
    print(f"📊 Summary: {success_notebook} / {notebook_found} notebooks ran successfully.")
    if failed_notebooks:
        print(f"\n🚨 Failed notebooks:")
        for nb, error in failed_notebooks:
            print(f" - {nb}")
            if hasattr(error, "__traceback__"):
                tb_lines = traceback.format_exception(type(error), error, error.__traceback__)
                for line in tb_lines[-3:]:
                    print("     ↳ " + line.strip())
            else:
                lines = str(error).strip().splitlines()
                if lines:
                    for line in lines[:3]:
                        print(f"     ↳ {line}")
                else:
                    print("     ↳ (No error message captured)")

    # Exit with appropriate code
    sys.exit(1 if failed_notebooks else 0)

if __name__ == "__main__":
    run_all_notebooks("notebooks")
