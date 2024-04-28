n = int(input("Type a number: "))

def powers_of_2(n):
    powers = []
    power = 0
    while n:
        if n % 2:
            powers.append(2 ** power)
        n //= 2
        power += 1
    return powers

result = powers_of_2(n)

print("Numbers of 2's powers that sum up to", n, ":", ' '.join(map(str, result)))
