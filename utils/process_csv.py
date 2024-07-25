import csv
import sys
import os

def process_csv(input_file_path):
    # Determine the output file path
    base, ext = os.path.splitext(input_file_path)
    output_file_path = base + '_processed' + ext
    
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['year', 'month', 'day', 'state', 'fips', 'cases', 'deaths']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            date_parts = row['date'].split('-')
            year, month, day = date_parts[0], date_parts[1], date_parts[2]
            new_row = {
                'year': year,
                'month': month,
                'day': day,
                'state': row['state'],
                'fips': row['fips'],
                'cases': row['cases'],
                'deaths': row['deaths']
            }
            writer.writerow(new_row)

    print(f"Processed file saved as: {output_file_path}")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: python3 -m utils.process_csv [filepath]")
        sys.exit( )
    process_csv(sys.argv[1])