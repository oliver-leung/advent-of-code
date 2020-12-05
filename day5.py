def code_to_count(code: str, one_char: str):
    bits = ['1' if c is one_char else '0' for c in code]
    binary = ''.join(bits)
    dec = int(binary, 2)
    return dec

def code_to_seat(code: str):
    row_code = list(code[:7])
    row = code_to_count(row_code, 'B')
    col_code = list(code[-3:])
    col = code_to_count(col_code, 'R')
    return row, col

seat_to_id = lambda row, col : (row * 8) + col

def parse():
    with open('day5.txt') as f:
        codes = f.readlines()
        codes = [line.strip() for line in codes]

    return codes

codes = parse()
seats = map(code_to_seat, codes)
ids = [seat_to_id(*seat) for seat in seats]
ids = sorted(ids)

for num, id in enumerate(ids):
    if id + 1 not in ids:
        print(id + 1)