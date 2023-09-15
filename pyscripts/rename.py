import re
import argparse
from rules import RULES

parser = argparse.ArgumentParser(description='Rename bibtex titles based on pre-defined rules.')
parser.add_argument('bibfile_path', metavar='bibfile', nargs='+', type=str, help='path to the bibtex file(s) to be renamed')

args = parser.parse_args()

def process_file(file_path: str):
    with open(file_path, 'r') as f:
        content = f.read()

    for abbreviation, name_patterns in RULES.items():
        for name_pattern in name_patterns:
            content = re.sub(name_pattern, abbreviation, content)

    with open(file_path, 'w') as f:
        f.write(content)


for i, bibfile_path in enumerate(args.bibfile_path):
    print(f"Processing {i+1}/{len(args.bibfile_path)}: {bibfile_path}")
    process_file(bibfile_path)

print('Done.')
