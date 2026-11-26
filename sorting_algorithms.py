def remove_duplicates(name):
    unique_letters = []

    for letter in name.upper():
        if letter.isalpha() and letter not in unique_letters:
            unique_letters.append(letter)

    return unique_letters


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array



def main():

    full_name = "Dhanielle Belocura"


    unsorted_array = remove_duplicates(full_name)


    sorted_array = unsorted_array.copy()


    bubble_sort(sorted_array)


    print("ASSESSMENT 3.7: SORTING ALGORITHMS")
    print("Name: Dhanielle Belocura")
    print("Sorting Method: Bubble Sort")

    print("\nUnsorted Array:")
    print(unsorted_array)

    print("\nSorted Array:")
    print(sorted_array)


if __name__ == "__main__":
    main()
