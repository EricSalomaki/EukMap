import sys

def parse_taxonomy(filename, output_filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    printed_lineages = set()

    with open(output_filename, 'w') as outfile:
        for line in lines:
            parts = line.strip().split(';')
            lineage = parts[0]

            for part in parts[1:]:
                lineage += ';' + part
                if lineage not in printed_lineages:
                    outfile.write(lineage + '\n')
                    printed_lineages.add(lineage)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 taxonomy_parser.py <input_filename> <output_filename>")
        sys.exit(1)

    filename = sys.argv[1]
    output_filename = sys.argv[2]

    parse_taxonomy(filename, output_filename)
