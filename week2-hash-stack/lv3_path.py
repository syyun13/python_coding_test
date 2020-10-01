# Level 3 Coding Challenge:
# A game character is moved with 4 commands.
# 'U': one space up / 'D': one space down / 'R': one space right / 'L': one space left
# Character starts at position (0,0) in the coordinate plane.
# Boundary of the plane is made of upper left: (5,5) / lower left: (5,-5) / upper right: (5,5) / lower right: (5,-5).
# Ignore the command that goes outside of the boundary.
# 'dirs' is a string of all commands.
# Return the length of path that the character walked for the first time.
# (ex. Do not count when the character walks on the same path for the second time)

def solution(dirs):
    answer = 0

    walked = [[ {"U": False, "D": False, "R": False, "L": False} for col in range(11) ] for row in range(11)]
    opposites = {"U": "D", "D": "U", "R": "L", "L": "R"}

    path = { "U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0] }
    x = 5
    y = 5
    
    for direction in dirs:
        add_x, add_y = path[direction]
        new_x = x + add_x
        new_y = y + add_y
        
        if 0 <= new_x <= 10 and 0 <= new_y <= 10:
            did_walk = walked[x][y][direction]
            if not did_walk:
                walked[x][y][direction] = True
                opposite = opposites[direction]
                walked[new_x][new_y][opposite] = True
                answer += 1
            x = new_x
            y = new_y

    return answer
