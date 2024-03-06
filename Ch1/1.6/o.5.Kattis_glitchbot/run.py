import sys


STEPS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def execute(x, y, face, instruction):
    if instruction == 'Forward':
        x += STEPS[face][0]
        y += STEPS[face][1]
    elif instruction == 'Right':
        face = (face + 1) % 4
    elif instruction == 'Left':
        face = (face - 1 + 4) % 4
    return (x, y, face)


def run(x, y, face, instructions):
    for inst in instructions:
        x, y, face = execute(x, y, face, inst)
    return x, y


def main():
    lines = sys.stdin.read().splitlines()

    X, Y = [int(x) for x in lines[0].split()]
    N = int(lines[1])
    
    face = 0
    
    lines = lines[2:]
    x = 0
    y = 0
    result = 0
    for n in range(N):
        for inst in 'Forward', 'Right', 'Left':
            if inst == lines[n]:
                continue
            temp_x, temp_y, temp_face = execute(x, y, face, inst)
            new_x, new_y = run(temp_x, temp_y, temp_face, lines[n+1:N])
            if new_x == X and new_y == Y:
                print(n+1, inst)
                result = 1
                break
        if result == 1:
            break
        x, y, face = execute(x, y, face, lines[n])

    



if __name__ == "__main__":
    main()
