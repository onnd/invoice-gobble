# Generate text file with pdftotext -layout <pdf file>
import sys

INFILE = sys.argv[1]
with open(INFILE, 'r') as f:
    line = f.readline()
    while line:
        if line[:17] == 'Transaktionsdatum':
            description_pos = line.find('Beskrivning')
            locality_pos = line.find('Ort')
            amount_pos = line.find('Belopp')
            paid_pos = line.find('Inbetalt')
        if len(line) > 10:
            if line[4] == line[7] == "-":
                date = line[:10]
                if locality_pos == -1:
                    description = line[description_pos:description_pos + 22].strip()
                    if description == 'INBETALNING BANKGIRO':
                        line = f.readline()
                        continue
                    amount = "-" + line[description_pos + 25:].strip()
                else:
                    description = line[description_pos:description_pos + 22].strip() + " " + line[locality_pos:locality_pos + 13].strip()
                    amount = line[locality_pos + 14:].strip()
                print(f"{description};{date};{amount}")
        line = f.readline()
