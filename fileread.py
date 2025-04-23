"""
This file processes a file passed to it, removes any lines that are not relevant for MARIEJ, and separates elements
for future use in the program.
"""

def readFile(f):
    lines = []
    with open(f) as file:
        for txt in file:
            # removes comments
            line = txt.split('#',1)[0]
            # removes whitespace
            line = line.strip()
            # only appends non-empty lines
            if line:
                lines.append(line)
    return lines

def getLabel(line):
    # removes/separates the label (if it exists) by splitting at a comma
    if ',' in line:
        label, other = line.split(',',1 )
        return label.strip(), other.strip()
    return None, line

def getInst(other):
    parts = other.split(maxsplit=1)
    inst = parts[0].upper()
    value = parts[1].strip() if len(parts) > 1 else None
    return inst, value

def toInt(num):
    return int(num)