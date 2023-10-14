from enum import Enum
import sys

class State(Enum):
    BEGIN = 1
    CARD = 2
    DATE = 3
    AMOUNT = 4

INFILE=sys.argv[1]

with open(INFILE, 'r') as f:
    state = State.BEGIN
    line = f.readline()
    while line:
        stripped = line.strip()
        if stripped != '':
            if state == State.BEGIN:
                if stripped[:3] == 'Köp':
                    description = stripped[4:]
                    state = State.CARD
                if stripped[:11] == 'Kreditering':
                    description = stripped[12:]
                    state = State.CARD
            elif state == State.CARD:
                state = State.DATE
            elif state == State.DATE:
                date = stripped
                state = State.AMOUNT
            elif state == State.AMOUNT:
                amount = stripped
                state = State.BEGIN
                print(f"{description};{date};{amount}")
        line = f.readline()
