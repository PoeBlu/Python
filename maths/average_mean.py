"""Find mean of a list of numbers."""


def average(nums):
    """Find mean of a list of numbers."""
    return sum(nums) / len(nums)


def main():
    """Call average module to find mean of a specific list of numbers."""
    print(average([2, 4, 6, 8, 20, 50, 70]))


if __name__ == "__main__":
    main()
