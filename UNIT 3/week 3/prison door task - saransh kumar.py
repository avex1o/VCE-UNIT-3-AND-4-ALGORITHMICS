# Number of doors
n = 500

# Initially all doors are locked (False)
doors = [False] * (n + 1)   # index 0 unused

# Perform passes
for pass_num in range(1, n + 1):
    for door in range(pass_num, n + 1, pass_num):
        doors[door] = not doors[door]  # toggle

# Collect open doors
open_doors = [i for i in range(1, n + 1) if doors[i]]

print(open_doors)