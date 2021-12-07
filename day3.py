def get_in():
    in_file = open('in3.txt', 'r')
    nums = [num for num in in_file.read().split()]
    in_file.close()
    return nums

def shave_list(nums, bit_value, index):
    return [x for x in nums if x[index] == bit_value]

def solve(nums):
    nums_co2 = nums
    j = 0
    while len(nums) > 1:
        count0 = 0
        count1 = 0
        for i in range(len(nums)):
            if nums[i][j] == '0':
                count0 += 1
            elif nums[i][j] == '1':
                count1 += 1
        if count0 > count1:
                nums = shave_list(nums, '0', j)
        else:
                nums = shave_list(nums, '1', j)
        j += 1

    j = 0
    while len(nums_co2) > 1:
        count0 = 0
        count1 = 0
        for i in range(len(nums_co2)):
            if nums_co2[i][j] == '0':
                count0 += 1
            elif nums_co2[i][j] == '1':
                count1 += 1
        if count0 > count1:
                nums_co2 = shave_list(nums_co2, '1', j)
        else:
                nums_co2 = shave_list(nums_co2, '0', j)
        j += 1



    ox_gen_rating = int(nums[0], 2)
    co2_scr_rating = int(nums_co2[0], 2)
    return ox_gen_rating * co2_scr_rating


if __name__ == '__main__':
    print(solve(get_in()))