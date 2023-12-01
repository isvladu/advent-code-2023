class Solution:
    input: str = ""

    def read_input():
        with open("input/day1_1.txt", "r") as f:
            input = f.read()


if __name__ == "__main__":
    solution = Solution()
    with open("output/day1.txt", "w") as f:
        f.write(str(solution))
