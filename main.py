import nbformat
import argparse
import os
    
if __name__ == '__main__':
    ap = argparse.ArgumentParser(description="convert python files to jupyter notebooks")
    ap.add_argument("-d", help="examples directory", default="examples")
    args = ap.parse_args()
    
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