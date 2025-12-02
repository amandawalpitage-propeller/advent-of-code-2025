with open("input.txt", "r") as f:
    ranges_ls = f.read().split(",")

def check_invalids_with_extra_rules(start,end):
    count_invalid = 0 # to store invalid 
    start_ = start
    end_ = end

    for i in range(start_,end_+1):
        # for each number we start splitting into substrings starting from 2 until length of string
        start_idx = 2
        while start_idx <= len(str(i)):
            # we check if the string can be split into equal parts of length start_idx
            if len(str(i)) % start_idx == 0:
                len_to_check = len(str(i)) // start_idx
                # check each part
                parts = [str(i)[j:j+len_to_check] for j in range(0, len(str(i)), len_to_check)]
                # check if all parts are equal
                if all(part == parts[0] for part in parts):
                    print(f"invalid ID found: {i}")
                    count_invalid += i 
                    # if we have found one invalid for this number no need to check further
                    break
            start_idx += 1

    return count_invalid


total_invalid =[]

for range_ in ranges_ls:
    range_ = range_.strip()
    range_arr = range_.split("-")

    start = int(range_arr[0])
    end = int(range_arr[1])

    print("start:", start, "end:", end)

    count_invalid = check_invalids_with_extra_rules(start,end)
    total_invalid.append(count_invalid)

print("total invalids sum:", sum(total_invalid))
