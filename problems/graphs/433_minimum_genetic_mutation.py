"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""
class Solution(object):
    choices = ['A', 'C', 'G', 'T']
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        return self.backtrack(startGene, endGene, set(bank), 0, set())

    def backtrack(self, currentGene, endGene, bank, steps, seen):
        if currentGene == endGene:
            return steps

        for index, char in enumerate(currentGene):
            for choice in self.choices:
                if char == choice:
                    continue
                nextGene = currentGene[:index] + choice + currentGene[index + 1:]
                if nextGene not in bank:
                    continue
                if nextGene in seen:
                    continue
                seen.add(nextGene)
                result = self.backtrack(nextGene, endGene, bank, steps + 1)
                if result != -1:
                    return result
        return -1
            


def run_test(test_name, input_desc, expected, actual):
    """Standard test runner"""
    status = "PASS" if actual == expected else "FAIL"
    print(f"{test_name}: Input={input_desc}, Expected={expected}, Got={actual}, {status}")
    return actual == expected


def test_433():
    solution = Solution()

    # Test case 1
    startGene1 = "AACCGGTT"
    endGene1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    expected1 = 1
    actual1 = solution.minMutation(startGene1, endGene1, bank1)
    run_test("Test 1", "startGene = 'AACCGGTT', endGene = 'AACCGGTA', bank = ['AACCGGTA']", expected1, actual1)

    # Test case 2
    startGene2 = "AACCGGTT"
    endGene2 = "AAACGGTA"
    bank2 = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    expected2 = 2
    actual2 = solution.minMutation(startGene2, endGene2, bank2)
    run_test("Test 2", "startGene = 'AACCGGTT', endGene = 'AAACGGTA', bank = ['AACCGGTA','AACCGCTA','AAACGGTA']", expected2, actual2)


if __name__ == "__main__":
    test_433()