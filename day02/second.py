from typing import List

def find_different_by_one_and_return_shared(input: List[str]) -> str:
    for i in range(0, len(input)):
        for j in range(i + 1, len(input)):
            differs_at = -1
            cnt_different = 0

            for idx, (ch1, ch2) in enumerate(zip(input[i], input[j])):
                if ch1 != ch2:
                    cnt_different += 1
                    differs_at = idx
                
                if cnt_different > 1:
                    break

            if cnt_different == 1:
                return input[i][:differs_at] + input[j][differs_at + 1:]    
    
    return None


with open("input.txt") as f:
    lines = [line.strip('\n') for line in f.readlines()]

    result = find_different_by_one_and_return_shared(lines)

    print(result)