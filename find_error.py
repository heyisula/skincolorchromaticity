import json
with open('d:/Projects/GitHub/skincolorchromaticity/skin_detection.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        for out in cell.get('outputs', []):
            if out.get('name') == 'stderr':
                print(f"Stderr in cell {i}:")
                source = "".join(cell.get('source', []))
                print("Source:")
                print(source)
                print("---")
                print("".join(out.get('text', [])))
                print("=" * 40)
