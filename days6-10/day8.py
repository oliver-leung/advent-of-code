from typing import List, Tuple


def run_terminates(insns: List[Tuple[str, int]]) -> Tuple[bool, int]:
    acc = 0
    pc = 0
    visited = set()

    while pc < len(insns):
        if pc in visited:
            return (False, acc)
        
        visited.add(pc)
        insn = insns[pc][0]
        if insn == 'jmp':
            pc += insns[pc][1]
            continue
        elif insn == 'acc':
            acc += insns[pc][1]
        pc += 1

    return (True, acc)

def fix_loop(insns: List[Tuple[str, int]]) -> int:
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for pc in range(len(insns)):
        if insns[pc][0] in swap:
            orig = insns[pc]
            insns[pc] = (swap[insns[pc][0]], insns[pc][1])

            terminates, acc = run_terminates(insns)
            if terminates:
                return acc
            
            insns[pc] = orig
    return 0

def tokenize(filename: str) -> List[Tuple[str, int]] :
    with open(filename) as f:
        lines = f.readlines()
    
    insns = []
    for line in lines:
        op, arg = line.strip().split()
        insns.append((op, int(arg.strip('+'))))

    return insns

insns = tokenize('day8.txt')
print(run_terminates(insns)[1])
print(fix_loop(insns))