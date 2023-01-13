# Convert a (simple) csv (1 column) file to an array of integers parseable by gcc

Usage: `csv_to_c_array_parser.py [-h] IN.csv [IN.csv ...] OUT.h`

Example: `csv_to_c_array_parser.py input_file.csv output_file.h`

Example input file content:

`input_file.csv`

    0C
    00
    00
    0A
    00

Example output file content:

`output_file.h`


    #include <stdint.h>
    const uint8_t silego_fw[256] = {
        0x0C,0x00,0x00,0x0A,0x00
    }
