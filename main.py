def Sqrt(x: int) -> int:
    limit = 100
    iG = x / 2.0
    accuracy = 1e-3
    tries = 0

    for i in range(limit):
        sqrtX = 0.5 * (iG + (x/iG))

        if abs(sqrtX - iG) < accuracy:
            break

        iG = sqrtX
        tries += 1

    return round(sqrtX, 3), tries

number = 1032546965
result, tries = Sqrt(number)
print(f"Square root of {number} is approximately {result}. Found in {tries} iterations")