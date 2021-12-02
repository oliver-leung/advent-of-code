from typing import Dict, List, Tuple
from collections import defaultdict
from queue import Queue


def invert_dict(d: Dict[Tuple[str, str], List[Tuple[int, str, str]]]):
    ans = defaultdict(list)
    for key, lst in d.items():
        for value in lst:
            ans[value[1:]].append(key)
    return ans

def bfs(root: Tuple[str, str], d: Dict[Tuple[str, str], List[Tuple[str, str]]]):
    queue = Queue()
    queue.put(root)
    discovered = set()
    discovered.add(root)

    while not queue.empty():
        source = queue.get()
        for dest in d[source]:
            if dest not in discovered:
                discovered.add(dest)
                queue.put(dest)
    
    discovered.remove(root)
    return discovered

def bags_contained(root: Tuple[str, str], d: Dict[Tuple[str, str], List[Tuple[int, str, str]]]):
    """Return the number of bags inside of root, not including root.

    Args:
        root (Tuple[str, str]): Original bag
        d (Dict[Tuple[str, str], List[Tuple[int, str, str]]]): Mapping from bag
            types to quantities of contained bags.
    """
    # Base case
    if len(d[root]) == 0 or d[root] is None:
        return 0
    
    # Inductive step
    ans = 0
    for bag in d[root]:
        bags = bags_contained(bag[1:], d) + 1 # + 1 includes the bag itself
        if bags == 0:
            ans += bag[0]
        else:
            ans += bag[0] * bags

    return ans

def parse():
    with open('day7.txt') as f:
        data = f.readlines()

    ans = defaultdict(list)
    for line in data:
        outer, inner = line.strip('\.\n').split('contain')
        if inner.strip() == 'no other bags':
            continue
        
        outer = tuple(outer.split()[:2])
        for bag in inner.split(', '):
            bag_split = bag.split()[:3]
            bag_split[0] = int(bag_split[0])
            ans[outer].append(tuple(bag_split))
    
    return ans

# If x contains [y, z], and w contains [y, z]
contained_by = parse() # contained_by(x) == [y, z]
contains = invert_dict(contained_by) # contains(y) == [w, x]
print(len(bfs(('shiny', 'gold'), contains)))
print(bags_contained(('shiny', 'gold'), contained_by))