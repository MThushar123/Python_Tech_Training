def duplicateZeros(arr):
    n = len(arr)

    zeros_count = arr.count(0)

    write_pos = n - 1
    read_pos = n - 1
    
    while write_pos >= 0:
        if read_pos < 0:
            break
            
        if arr[read_pos] == 0:
            if write_pos < zeros_count:
                arr[write_pos] = 0
                zeros_count -= 1
                write_pos -= 1
            if write_pos >= 0:
                arr[write_pos] = 0
                write_pos -= 1
            read_pos -= 1
        else:
            arr[write_pos] = arr[read_pos]
            write_pos -= 1
            read_pos -= 1
    
    return arr

def main():
    arr_input = input("Enter space-separated numbers: ").strip().split()
    arr = [int(x) for x in arr_input]
    
    print("Original:", arr)
    result = duplicateZeros(arr)
    print("After duplicating zeros:", result)

if __name__ == "__main__":
    main()