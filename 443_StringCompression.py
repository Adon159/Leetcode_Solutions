from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        unique_list = []
        count = 0
        prev = None

        for idx in range(len(chars)):
            if prev is None:
                unique_list.append(chars[idx])
                prev = chars[idx]
                count += 1

            elif chars[idx] == prev:
                count += 1

            else:
                if count > 1:
                    unique_list.extend(list(str(count)))
                unique_list.append(chars[idx])
                prev = chars[idx]
                count = 1

        if count > 1:
            unique_list.extend(list(str(count)))

        chars[:len(unique_list)] = unique_list
        return len(unique_list)