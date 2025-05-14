def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_index = start
    pivot_value = array[pivot_index]
    left = start + 1
    right = end

    print(f"\n目前排序區間: {array[start:end+1]} (pivot={pivot_value})")

    while left <= right:
        while left <= right and array[right] >= pivot_value:
            right -= 1
        while left <= right and array[left] <= pivot_value:
            left += 1
        if left < right:
            print(f"  交換 {array[left]} 和 {array[right]}")
            array[left], array[right] = array[right], array[left]

    print(f"  將 pivot {pivot_value} 和 {array[right]} 交換")
    array[pivot_index], array[right] = array[right], array[pivot_index]

    print(f"  排序後：{array}")

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

demo = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

print("demo：")
print(demo)

quick_sort(demo, 0, len(demo) - 1)

print("\n排序完成：")
print(demo)
