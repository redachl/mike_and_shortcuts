import sys
from typing import List


def compute_required_energy(intersection_count: int, shortcuts: List[int]):
    energy_required_to_ith_interesection = [0] * intersection_count
    for i in range(2, intersection_count + 1):
        position = 1
        position_and_energy_queue = [(1, 0)]
        possible_energies = [abs(i - position)]
        while position_and_energy_queue:
            position, energy = position_and_energy_queue.pop(0)

            # stop trying to move to the target intersection when it is reached
            if position == i:
                possible_energies.append(energy)
                continue

            # stop trying to reach the target intersection when the energy used is greater than or equal to the maximum energy |1 - i|
            if energy >= possible_energies[0]:
                continue

            next_with_shortcut = shortcuts[position - 1]
            if next_with_shortcut != position:
                position_and_energy_queue.append(
                    (next_with_shortcut, energy + 1))
            if position + 1 < intersection_count:
                position_and_energy_queue.append((position + 1, energy + 1))
            if position - 1 > 0:
                position_and_energy_queue.append((position - 1, energy + 1))

        energy_required_to_ith_interesection[i - 1] = min(possible_energies)

    return energy_required_to_ith_interesection


if __name__ == '__main__':
    inputs = list(sys.stdin)
    intersection_count = int(inputs[0].rstrip())
    shortcuts = list(map(int, inputs[1].rstrip().split(' ')))

    print(' '.join(
        map(str, compute_required_energy(intersection_count, shortcuts))))

    sys.stdout.flush()
