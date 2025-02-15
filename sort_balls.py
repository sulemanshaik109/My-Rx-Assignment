def sort_balls(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == "B":
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == "G":
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


    return arr

if __name__ == "__main__":
    input_balls = ["R", "B", "G", "G", "G", "R", "B", "B", "G"]
    sorted_balls = sort_balls(input_balls)
    print(sorted_balls)