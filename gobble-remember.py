from enum import Enum
import sys


class State(Enum):
    BEGIN = 1
    TRANSACTIONS = 2


INFILE = sys.argv[1]

with open(INFILE, 'r') as f:
    state = State.BEGIN
    line = f.readline()
    while line:
        stripped = line.strip()
        if stripped != '':
            if stripped[:17] == 'Transaktionsdatum':
                state = State.TRANSACTIONS
            elif state == State.TRANSACTIONS:
                if stripped[4] == stripped[7] == "-":
                    parts = stripped.split(' ')
                    date = parts[0]
                    description = ' '.join(parts[2:-1])
                    if parts[2] == 'Rabatt':
                        amount = '-' + parts[-1]
                    else:
                        amount = parts[-1]
                    if parts[2] != 'INBETALNING':
                        print(f"{description};{date};{amount}")
                else:
                    state = State.BEGIN
        line = f.readline()
