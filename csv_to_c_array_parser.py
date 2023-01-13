import argparse
import pathlib
import textwrap

ARRAY_TYPES = "const uint8_t"
ARRAY_LENGTH = 256

def parse_csv_to_array_str(csv_file, array_name: str):
    yield f"{ARRAY_TYPES} {array_name}[{ARRAY_LENGTH}] = " '{'
    yield "    " + ",".join(f"0x{line.strip()}" for line in csv_file.readlines())
    yield "};"

def add_header(out_file):
    out_file.write("#include <stdint.h>\n")

def main():
    parser = argparse.ArgumentParser(
        description='Convert a csv file to an array of integers parseable by gcc.', 
        epilog=textwrap.dedent('''\
            Example input file content:
                
                0C
                00
                00
                0A
                00
            
            Example output file content:

                #include <stdint.h>
                    const uint8_t silego_fw[256] = {
                        0x0C,0x00,0x00,0x0A,0x00
                    }
            '''),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('csv_tables', metavar='IN.csv', type=open, nargs='+',
                        help='The input csv files. More csv files = more arrays.')
    parser.add_argument('output_file', metavar='OUT.h', type=argparse.FileType('w'), 
                        help='The input csv files. More csv files = more arrays.')

    args = parser.parse_args()

    array_names = [ "silego_fw", ] if len(args.csv_tables) == 1 else [ f"silego_fw_{num}" for num in range(args.csv_tables) ]
    
    with args.output_file as out_file:
        add_header(out_file)
        for i, in_file in enumerate(args.csv_tables):
            with in_file as _in_file:
                print(in_file)
                for line in parse_csv_to_array_str(_in_file, array_names[i]):
                    out_file.write(line + "\n")

if __name__ == "__main__":
    main()