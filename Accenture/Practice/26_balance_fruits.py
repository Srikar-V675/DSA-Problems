# Balance Apples and Mangoes
def balanceFruits(apple: int, mango: int, rupees: int) -> int:
    if apple > mango:
        rupees -= (apple - mango)
    elif mango > apple:
        rupees += (mango - apple)
    return rupees


apple = 4
mango = 8
rupees = 6
print(balanceFruits(apple, mango, rupees))