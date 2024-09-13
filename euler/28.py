# Sum of spiral diagonals.

N = 1001 * 1001
#N = 5 * 5

def is_diagonal(x,y):
    return x == y or x == -y

# Making a spiral:
# - right
# - down
# Increment.
# - left
# - up
# Increment.

directions = [(1, 0), (0, -1), 
              (-1, 0), (0, 1)]

direction_index = 0

ans = 1 # for (0,0).

position = (0, 0)
offset = 0
current_val = 2

while current_val < N:
    
    if direction_index % 2 == 0:
        offset += 1

    for _ in range(offset):
        
        dx, dy = directions[direction_index]
        position = (position[0] + dx, 
                    position[1] + dy)
        
        if is_diagonal(*position):
            ans += current_val

        current_val += 1
        if current_val > N:
            break

    direction_index += 1
    direction_index %= 4

if __name__ == '__main__':

    print(f'answer = {ans}')
