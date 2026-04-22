import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20



def selection_sort(seznam_cisel):
    numbers = seznam_cisel.copy()
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    return numbers

def bubble_sort(seznam_cisel):

    numbers_copy = seznam_cisel.copy()
    n = len(numbers_copy)
    plt.ion()
    plt.show()

    for i in range(n):
        min_index = i
        for j in range(0, n-i-1):

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers_copy[j] > numbers_copy[j+1]:
                numbers_copy[j], numbers_copy[j+1] = numbers_copy[j+1], numbers_copy[j]

        plt.ioff()
        plt.show()

    return numbers_copy


def main():
    short_list = [5, 1, 4, 2, 8]
    sorted_short = selection_sort(short_list)
    bubble_short = bubble_sort(short_list)
    # 1. test na krátkém seznamu
    print("--- Test na krátkém seznamu ---")
    print(f"Původní: {short_list}")
    print(f"Seřazený(sort): {sorted_short}")
    print(f"Seřazený(bubble): {bubble_short}")

    # 2. Test na náhodně generovaném seznamu
    random_list = random_numbers(20)
    sorted_random = selection_sort(random_list)
    bubble_random = bubble_sort(random_list)

    print("\n--- Test na náhodném seznamu (20 čísel) ---")
    print(f"Původní: {random_list}")
    print(f"Seřazený(sort): {sorted_random}")
    print(f"Seřazený(bubble): {bubble_random}")

    # Ověření
    print()
    print(f"Kontrola (původní seznam stále stejný): {random_list[:6]}...")

    data = [15, 3, 9, 21, 5, 12, 1, 8]
    bubble_sort_visualized(data)
    print()
    print({bubble_sort(data)})

if __name__ == "__main__":
    main()



