class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # starting from reading off 1 (one 1)
        to_read = str(n)
        # initialize a list of read off integers
        counted = []

        # internal structure to read off one integer
        # initialize counter
        count = 1
        # if I don't initialize i, the very last counted.append complains the i can be referenced before assignment
        i = 0
        for i in range(1, len(to_read)):
            print('i:', i)
            # if an integer occurs again, we increase the counter
            if to_read[i-1] == to_read[i]:
                count += 1
                print('count: ', count)
            # if we find a different integer, write the number of the integer occurrences (count)
            # and the integer itself, then and reset the counter
            else:
                print('count:', count)
                counted.append(str(count) + to_read[i-1])
                count = 1
            print('counted:', counted)
        # the very last counter.append - required to count the last (i) element.
        # The one in the if/else counts (i-1) element
        counted.append(str(count) + to_read[i])
        output = "".join(counted)
        return output


x = Solution()
print(x.countAndSay(1))
# print(x.countAndSay(11))
# print(x.countAndSay(21))
# print(x.countAndSay(1211))
# print(x.countAndSay(111221))
# print(x.countAndSay(312211))
# print(x.countAndSay(13112221))
