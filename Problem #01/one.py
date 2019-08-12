def simple_approach(k: int, numbers: list):
    # Complexity close to O(n^2) in the worst case

    length = len(numbers)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == k:
                return True
    return False


def smart_approach(k: int, numbers: list):
    # The smart Google solution, one timer
    # Complexity O(n)

    complements = set()
    for num in numbers:
        if num in complements:
            return True
        complements.add(k - num)
    return False


if __name__ == '__main__':
    print(simple_approach(17, [10, 15, 3, 7]))
    print(smart_approach(17, [10, 15, 3, 7]))
