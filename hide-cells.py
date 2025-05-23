import os
import nbformat

def add_remove_cell_tag_to_ipynb_files(directory):
    for root, _, files in os.walk(directory):
        # './_build' 디렉토리는 생략
        if './_build' in root:
            continue
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                print(f"{file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                hidden_cells_count = 0
                for cell in notebook.cells:
                    if cell.cell_type == 'code' and ('# hide' in cell.source or '#hide' in cell.source):
                        if 'tags' not in cell.metadata:
                            cell.metadata['tags'] = []
                        cell.metadata['tags'].append('remove-cell')
                        hidden_cells_count += 1
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    nbformat.write(notebook, f)
                
                if hidden_cells_count > 0:
                    print(f"{file_path}에서 {hidden_cells_count}개의 셀을 숨김처리했습니다.")

add_remove_cell_tag_to_ipynb_files(".")