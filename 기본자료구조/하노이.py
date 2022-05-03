
def hanoi(n, from_pos, aus_pos, to_pos):
    if n==1:
        print(from_pos, "->", to_pos)
        return

    hanoi(n-1, from_pos, to_pos, aus_pos)
    print(from_pos, "->", to_pos)
    hanoi(n-1, aus_pos, from_pos, to_pos)

hanoi(3, 1, 2, 3)