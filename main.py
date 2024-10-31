import random
import time

field = []
x0 = 30
y0 = 10
dist = 40

time_for_shooting = 0.03
time_for_moving = 0.2

for i in range(y0):
    field.append(x0*["."] + dist*[" "] + x0*["."])


k = 2

gun = [3, 11]

# ammunition = 20

for i in range(3, 6):
    (field[k])[i] = "o"
k+=1
for i in range(2, 11):
    (field[k])[i] = "o"
k+=1
for i in range(2, 6):
    (field[k])[i] = "o"
k+=1
for i in range(9):
    (field[k])[i] = "o"
k+=1
for i in range(9):
    (field[k])[i] = "o"
k+=1
for i in range(1, 8):
    (field[k])[i] = "o"
k+=1


targets = random.randint(7, 12)

ammunition = int(1.5 * targets)

for i in range(targets):
    xt = random.randint(x0+dist, x0+dist+x0-1)
    yt = random.randint(3, y0-3)
    while (field[yt])[xt] == "I" or yt == y0 - 3 and xt == x0+dist:
        xt = random.randint(x0 + dist, x0 + dist + x0 - 1)
        yt = random.randint(3, y0 - 3)
    (field[yt])[xt] = "I"
print("Welcome to the Battlefield! Press 'w' to move up, 's' to move down, 'd' - right, 'a' - left. Press ' ' to fire."
      " To exit press 'q'. \nYou have %d shells for all %d targets." %(ammunition, targets))

while True:
    for i in range(y0):
        for j in range(x0+dist+x0):
            print((field[i])[j], end="")
        print()
    print()
    command = input()
    for order in command:
        if order == "w":
            for i in range(x0):
                if (field[0])[i] == "o":
                    print("Game Over: you're in the ditch")
                    exit()
            for y in range(1, y0):
                stop = True
                for x in range(x0):
                    if (field[y])[x] == "o":
                        (field[y - 1])[x] = "o"
                        (field[y])[x] = "."
            gun[0] -= 1

            time.sleep(time_for_moving)
            for i in range(y0):
                for j in range(x0 + dist + x0):
                    print((field[i])[j], end="")
                print()
            print()


        if order == "s":
            for i in range(x0):
                if (field[y0-1])[i] == "o":
                    print("Game Over: you're in the ditch")
                    exit()
            for y in range(y0-2, -1, -1):
                for x in range(x0):
                    if (field[y])[x] == "o":
                        (field[y + 1])[x] = "o"
                        (field[y])[x] = "."
            gun[0] += 1

            time.sleep(time_for_moving)
            for i in range(y0):
                for j in range(x0 + dist + x0):
                    print((field[i])[j], end="")
                print()
            print()

        if order == "q":
            print("Thank you for game!")
            exit()

        if order == "a":
            for y in range(y0):
                if (field[y])[0] == "o":
                    print("Game Over: you're in the ditch")
                    exit()
            for y in range(y0):
                for x in range(1, x0):
                    if (field[y])[x] == "o":
                        (field[y])[x-1] = "o"
                        (field[y])[x] = "."
            gun[1] -= 1

            time.sleep(0.2)
            for i in range(y0):
                for j in range(x0 + dist + x0):
                    print((field[i])[j], end="")
                print()
            print()


        if order == "d":
            for y in range(y0):
                if (field[y])[x0-1] == "o":
                    print("Game Over: you're in the ditch")
                    exit()
            for y in range(y0):
                for x in range(x0-2, -1, -1):
                    if (field[y])[x] == "o":
                        (field[y])[x+1] = "o"
                        (field[y])[x] = "."
            gun[1] += 1

            time.sleep(time_for_moving)
            for i in range(y0):
                for j in range(x0 + dist + x0):
                    print((field[i])[j], end="")
                print()
            print()


        if order == " ":
            ammunition -= 1

            ballistic = 0
            count = 0
            g = 1
            hit = False
            for x in range(gun[1], x0+dist+x0):
                if (field[gun[0] + ballistic])[x] == "I":
                    hit = True

                (field[gun[0] + ballistic])[x] = "x"
                if (field[gun[0] + ballistic])[x-1] == "x":
                    if (field[gun[0] + ballistic - 1])[x-1] != "I":
                        (field[gun[0] + ballistic])[x-1] = (field[gun[0] + ballistic - 1])[x-1]
                    else:
                        (field[gun[0] + ballistic])[x - 1] = "."
                if (field[gun[0] + ballistic - 1])[x-1] == "x":
                    if (field[gun[0] + ballistic - 2])[x-1] != "I":
                        (field[gun[0] + ballistic - 1])[x-1] = (field[gun[0] + ballistic - 2])[x-1]
                    else:
                        (field[gun[0] + ballistic - 1])[x - 1] = "."

                if x == x0+dist+x0-1:
                    if (field[gun[0] + ballistic - 1])[x] != "I":
                        (field[gun[0] + ballistic])[x] = (field[gun[0] + ballistic - 1])[x]
                    else:
                        (field[gun[0] + ballistic])[x] = "."

                if hit:
                    targets -= 1
                    (field[gun[0] + ballistic])[x] = "."
                    if targets != 0:
                        print("Target has been destroyed! It's %d targets to hit!" %(targets))
                    else:
                        print("All targets have been destroyed!")
                    break

                count += 1
                if count == 30:
                    count = 0
                    ballistic += g
                    #g += 1
                if gun[0] + ballistic >= y0:
                    (field[y0 - 1])[x] = (field[y0 - 2])[x]

                for i in range(y0):
                    for j in range(x0 + dist + x0):
                        print((field[i])[j], end="")
                    print()
                print()

                time.sleep(time_for_shooting)

            if targets == 0:
                print("You are a winner!")
                exit()

            if ammunition == 0:
                print("It's impossible! You're out of ammunition!")
                exit()

            if ammunition < targets:
                print("It's impossible! It isn't enough for hitting each target!")

            print("You have %d ammo left." %(ammunition))