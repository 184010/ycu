cube = 0.5   # この３乗根　
epsilon = 0.0001     # 精度
count_guesses = 0

# cubeが1未満なら、lowとhighは逆になる （ただし、highは１）
# cube = 0.5では
# 0 < cube < guess < 1
if abs(cube)<1:
    low = cube
    high = 1
else:
    low = 1
    high =cube


guess = (low + high)/2
while abs(guess**3 - cube) >= epsilon  :
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high)/2
    count_guesses += 1
print(' count_guess =', count_guesses )
print(guess, 'is close to the cube root of ',cube)


