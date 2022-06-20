import sys
from typing import List


def compute_required_energy(intersection_count: int, shortcuts: List[int]):
    energy_required_to_ith_interesection = [0] * intersection_count
    for i in range(2, intersection_count + 1):
        position = 1
        
        # Use a depth first search (follow a path using shortcuts or going forward or backward and discard it when the minimum energy is reached)
        position_and_energy_stack = [(1, 0)]
        minimum_energy = abs(i - position)
        while position_and_energy_stack and minimum_energy > 1:
            position, energy = position_and_energy_stack.pop()

            # stop trying to move to the target intersection when it is reached
            if position == i and energy < minimum_energy:
                minimum_energy = energy
                continue

            next_with_shortcut = shortcuts[position - 1]
            # for all paths, stop trying to reach the target intersection when the energy used is greater than or equal to the maximum energy |1 - i|
            if next_with_shortcut != position and energy + 1 < minimum_energy and not (minimum_energy - (energy + 1) == 1 and next_with_shortcut < len(shortcuts) and shortcuts[next_with_shortcut] != i and abs(i - next_with_shortcut) != 1):
                position_and_energy_stack.append(
                    (next_with_shortcut, energy + 1))
            if position + 1 < intersection_count and energy + 1 < minimum_energy and not (minimum_energy - (energy + 1) == 1 and next_with_shortcut < len(shortcuts) and shortcuts[next_with_shortcut] != i and abs(i - next_with_shortcut) != 1):
                position_and_energy_stack.append((position + 1, energy + 1))
            if position - 1 > 0 and energy + 1 < minimum_energy and not (minimum_energy - (energy + 1) == 1 and next_with_shortcut < len(shortcuts) and shortcuts[next_with_shortcut] != i and abs(i - next_with_shortcut) != 1):
                position_and_energy_stack.append((position - 1, energy + 1))

        energy_required_to_ith_interesection[i - 1] = minimum_energy

    return energy_required_to_ith_interesection


if __name__ == '__main__':
    inputs = list(sys.stdin)
    intersection_count = int(inputs[0].rstrip())
    shortcuts = list(map(int, inputs[1].rstrip().split(' ')))

    print(' '.join(
        map(str, compute_required_energy(intersection_count, shortcuts))))

    sys.stdout.flush()
