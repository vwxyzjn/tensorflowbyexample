import nbformat
import argparse
import os
import subprocess
import shutil

# https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description="convert python files to jupyter notebooks")
    ap.add_argument("-d", help="examples directory", default="examples")
    args = ap.parse_args()
    
    # 1. Create Jupyter Notebooks.
    for dirpath, dirnames, filenames in os.walk("examples"):
        # if we reach the leaf directory
        if not dirnames:
            for fn in filenames:
                extension = fn.split('.')[-1]
                file_title = fn.rstrip(extension)
                if extension == 'py':
                    with open(os.path.join(dirpath, fn), 'r') as f:
                        code = f.read()
                elif extension == 'sh':
                    with open(os.path.join(dirpath, fn), 'r') as f:
                        temp_output = f.read()
                    real_ourputs = False
                    outputs = []
                    for line in temp_output.split('\n'):
                        if line.startswith("$"):
                            real_ourputs = True
                            continue
                        if real_ourputs:
                            outputs += [line]
                    output = "\n".join(outputs)
                            

            nb = nbformat.v4.new_notebook()
            code_cell = nbformat.v4.new_code_cell(code)
            code_cell.outputs += [nbformat.v4.new_output("stream", text=output)]
            nb.cells += [code_cell]
            with open(os.path.join(dirpath, file_title+"ipynb"), 'w') as f:
                nbformat.write(nb, f)

    # 2. Generate Docs and paste them to the current folder.
    # https://stackoverflow.com/questions/43515481/python-how-to-move-list-of-folders-with-subfolders-to-a-new-directory
    root_dst_dir = os.path.join(os.getcwd(), "docs")
    with cd("./examples"):
        subprocess.run(["pycco", "-p", "-i", "-n", "4", "."])
        root_src_dir = os.path.join(os.getcwd(), "docs")
        for src_dir, dirs, files in os.walk(root_src_dir):
            dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    # in case of the src and dst are the same file
                    if os.path.samefile(src_file, dst_file):
                        continue
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
