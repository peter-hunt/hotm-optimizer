from collections import deque

from data import *


Node = tuple[int, int]
Path = tuple[Node]
PATHS: dict[Node, list[Path]] = {
    (0, 3): [((0, 3),)], (1, 3): [((1, 3), (0, 3))]}
ENDPOINT = (0, 3)
for start in HOTM_TAKEN:
    if start in PATHS:
        continue
    valid_paths = {*()}
    paths_deque = deque(((start,),))
    while len(paths_deque) > 0:
        path = paths_deque.popleft()
        head = path[-1]
        hi, hj = head
        for nextup in ((hi + 1, hj), (hi, hj + 1), (hi - 1, hj), (hi, hj - 1)):
            if nextup in HOTM_TAKEN and nextup not in path:
                if nextup == ENDPOINT:
                    valid_paths.add(path + (nextup,))
                elif nextup in PATHS:
                    for continuation in PATHS[nextup]:
                        if len({*path} & {*continuation}) == 0:
                            valid_paths.add(path + continuation)
                else:
                    paths_deque.append(path + (nextup,))
    PATHS[start] = sorted(valid_paths)


def smart_union(*groups, max_len: int = 0):
    """
    Recursively finds all minimal-cost union combinations of paths.
    """
    if not groups:
        return []

    # Base case: If only one group left, filter by max_len
    if len(groups) == 1:
        return [set(g) for g in groups[0] if len(g) <= max_len]

    # Recursive step
    result_sets = []
    # Get results from the rest of the groups first
    sub_results = smart_union(*groups[1:], max_len=max_len)

    for group1_item in groups[0]:
        # Optimization: if the first item alone is too long, skip
        if len(group1_item) > max_len:
            continue
        for group2_item_set in sub_results:
            merged_set = set(group1_item) | group2_item_set
            if len(merged_set) <= max_len:
                result_sets.append(merged_set)

    # Pruning logic: Remove any path that is a superset of another valid path
    unique_sets = {tuple(sorted(list(s))) for s in result_sets}
    minimal_sets = []
    for s_tuple in unique_sets:
        s_set = set(s_tuple)
        is_minimal = True
        for other_tuple in unique_sets:
            if s_tuple != other_tuple and set(other_tuple).issubset(s_set):
                is_minimal = False
                break
        if is_minimal:
            minimal_sets.append(s_set)

    return minimal_sets


def union_pathfind(nodes: set[tuple[int, int]], hotm: int, tokens: int):
    """
    Finds all valid HotM trees for a given set of desired nodes.
    (Corrected Version)
    """
    # This function requires a pre-computed PATHS dictionary, which is not defined
    # in the provided snippets. Assuming it exists and maps a node to its possible paths.
    # For now, this will raise an error unless PATHS is defined elsewhere.
    if 'PATHS' not in globals():
        print("Error: PATHS dictionary not found. Pathfinding cannot proceed.")
        return []

    choice_groups = []
    for node in nodes:
        paths = PATHS.get(node, [])
        valid_paths = [path for path in paths if all(
            n[0] < hotm for n in path)]
        if not valid_paths:  # If a required node has no valid path, no solution is possible
            return []
        choice_groups.append(valid_paths)

    # Add paths for the Core of the Mountain
    cotm_paths = [path for path in PATHS.get(
        (4, 3), []) if all(n[0] < hotm for n in path)]

    # Token cost for CotM is 0, so we check paths up to tokens+1 and add CotM manually
    # The smart_union function will find all minimal combinations
    choices = smart_union(*choice_groups, cotm_paths, max_len=tokens + 1)

    # Ensure CotM is in every final path and remove it from the token count check
    final_choices = []
    for path in choices:
        final_path = path | {(4, 3)}
        # The true cost is the length of the set minus the free CotM node
        if len(final_path) - 1 <= tokens:
            final_choices.append(final_path)

    return final_choices


def to_set_pos(nodes: set[str]):
    return {to_pos(node) for node in nodes}


def find_trees(abilities, nodes, hotm, tokens):
    all_trees = []
    for ability in abilities:
        required_nodes = to_set_pos(nodes | {ability})

        tree_paths = union_pathfind(required_nodes, hotm, tokens)

        if not tree_paths:
            continue

        all_trees.extend(tree_paths)

    return [set(t) for t in {tuple(sorted(list(tree))) for tree in all_trees}]
