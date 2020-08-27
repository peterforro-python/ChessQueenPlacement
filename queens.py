from os import system

class QueenPlacement:
    def __init__(self) -> None:
        self.width = 8
        self.height = self.width
        self.board = [["W" if (x + y) % 2 == 0 else "B" for x in range(self.width)] for y in range(self.height)]

    def __str__(self) -> str:
        return "\n".join([" ".join(row) for row in self.board])




if __name__ == "__main__":
    system("cls")
    task = QueenPlacement()
    print(task)