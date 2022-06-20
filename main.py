import sys
from typing import List


def compute_required_energy(intersection_count: int, shortcuts: List[int]):
    energy_required_to_ith_interesection = [0] * intersection_count
    for i in range(2, intersection_count + 1):
        res = 0
        position = 1
        # print(f'from 1 to intersection {i}: ')
        while position != i:
            # print(position)
            # sleep(1)
            next_with_shortcut = shortcuts[position - 1]
            if next_with_shortcut != position and abs(
                    i - position) > 1 + abs(i - next_with_shortcut):
                position = next_with_shortcut
            elif position < i:
                position += 1
            elif position > i:
                position -= 1

            res += 1

        energy_required_to_ith_interesection[i - 1] = res

    return energy_required_to_ith_interesection


if __name__ == '__main__':
    inputs = list(sys.stdin)
    intersection_count = int(inputs[0].rstrip())
    shortcuts = list(map(int, inputs[1].rstrip().split(' ')))

    print(' '.join(
        map(str, compute_required_energy(intersection_count, shortcuts))))
