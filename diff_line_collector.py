# Run with 'for d in */; do python3 diff_line_collector.py $d/diffs/ $d/entropy/; done'

import sys
import os

if len(sys.argv) < 3:
    print("Usage: python3 diff_line_collector.py <diff directory> <output directory>")
    sys.exit()

diff_dir = sys.argv[1]
out_dir = sys.argv[2]

results = []

for dirpath, dirnames, filenames in os.walk(diff_dir):
    for filename in filenames:
        current_line_add = None
        current_line_del = None
        additions = []
        deletions = []
        if ".c-diff" in filename:
            with open(os.path.join(dirpath, filename), 'r') as f:
                try:
                    for line in f:
                        if line.startswith('>'):
                            if not line.replace('>', '').strip() == '':
                                additions.append(current_line_add)
                            current_line_add += 1
                        elif line.startswith('<'):
                            if not line.replace('<', '').strip() == '':
                                deletions.append(current_line_del)
                            current_line_del += 1
                        elif len(line) > 0 and line[0].isdigit():
                            # Then we have a line number marker
                            if 'a' in line:
                                # Addition
                                parts = line.split('a')
                                rightpart = parts[1]
                                parts = rightpart.split(',')
                                start = parts[0]
                                current_line_add = int(start)
                            elif 'c' in line:
                                parts = line.split('c')
                                leftpart = parts[0]
                                rightpart = parts[1]
                                parts = leftpart.split(',')
                                start = parts[0]
                                current_line_del = int(start)
                                parts = rightpart.split(',')
                                start = parts[0]
                                current_line_add = int(start)
                                # Change
                            elif 'd' in line:
                                # Deletion
                                parts = line.split('d')
                                leftpart = parts[0]
                                parts = leftpart.split(',')
                                start = parts[0]
                                current_line_del = int(start)
                            else:
                                print("Failed on line {}".format(line))
                                raise 
                except:
                    pass
        filename_to_output = os.path.join(dirpath, filename)
        filename_to_output = os.path.relpath(filename_to_output, diff_dir)
        results.append((filename_to_output, additions, deletions))

with open(os.path.join(out_dir, 'difflines_add.csv'), 'w') as f:
    f.write('filename, additions\n')
    for (fn, additions, deletions) in results:
        if len(additions) > 0:
            f.write('{},{}\n'.format(fn.replace('.c-diff', '.c'), ",".join(str(addition) for addition in additions)))

with open(os.path.join(out_dir, 'difflines_del.csv'), 'w') as f:
    f.write('filename, deletions\n')
    for (fn, additions, deletions) in results:
        if len(deletions) > 0:
            f.write('{},{}\n'.format(fn.replace('.c-diff', '.c'), ",".join(str(deletion) for deletion in deletions)))