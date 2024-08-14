# Tallest Tree
class Tree:
    def __init__(self, feets: int, inches: int) -> None:
        self.feets = feets
        self.inches = inches


def tallestTree(trees: list[Tree]) -> int:
    maxHeight = 0
    for tree in trees:
        height = (12 * tree.feets) + tree.inches
        maxHeight = max(maxHeight, height)
    
    return maxHeight


trees: list[Tree] = [
    Tree(10, 4),
    Tree(23, 5),
    Tree(21, 2),
    Tree(27, 7)
]
print(tallestTree(trees))