#!/usr/bin/env python3
import csv
from pathlib import Path

def csv_to_txt(folder: Path = Path('.')):
    for csv_path in folder.glob('*.csv'):
        txt_path = csv_path.with_suffix('.txt')
        with csv_path.open(newline='') as csvfile, txt_path.open('w') as txtfile:
            reader = csv.reader(csvfile)
            # Skip header row if present
            headers = next(reader, None)
            if headers and headers[0].lower() == 'host':
                pass  # header consumed
            else:
                # if first row wasn't actually a header, treat it as data
                csvfile.seek(0)
                reader = csv.reader(csvfile)
            # Write each Host:Port
            for row in reader:
                if len(row) < 2:
                    continue
                host, port = row[0].strip(), row[1].strip()
                txtfile.write(f'{host}:{port}\n')
        print(f'Wrote {txt_path}')

if __name__ == '__main__':
    csv_to_txt()
