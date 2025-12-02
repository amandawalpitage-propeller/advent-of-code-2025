with open("input3.txt", "r") as f:
    ranges_ls = f.read().split(",")


def check_invalids(start,end):
    count_invalid = 0 # to store invalid 
    start_ = start
    end_ = end

    for i in range(start_,end_+1):
        # check only even length strings
        if len(str(i)) % 2 == 0:
            # even length string 
            # we check first and second half
            len_to_check = len(str(i)) // 2
            if (str(i)[:len_to_check] == str(i)[len_to_check:]):
                count_invalid += i # add the ids to count_invalid 
    return count_invalid


total_invalid =[]

for range_ in ranges_ls:
    range_ = range_.strip()
    range_arr = range_.split("-")

    start = int(range_arr[0])
    end = int(range_arr[1])

    print("start:", start, "end:", end)

    count_invalid = check_invalids(start,end)
    total_invalid.append(count_invalid)


print("total invalids sum:", sum(total_invalid))