class Solution:
    # def dailyTemperatures(self, T: list[int]) -> list[int]:
    #     n, right_max = len(T), float('-inf') # n = length/size of T, right_max lowest possible float
    #     res = [0] * n  # creates a list of 0's with lenght n
    #     for i in range(n-1, -1, -1): # starting from len(T) - 1 (last index), stop at -1 (first index), skip by -1 (step from last element to first element)
    #         t = T[i] # t is the current element being pointed to
    #         if right_max <= t: # is right_max less than or equal to t?
    #             right_max = t # set right_max as t if true
    #             print(right_max)
    #         else:
    #             days = 1 
    #             while T[i+days] <= t: # while the next index after T[i] is less than or equal to t (T[i])
    #                 days += res[i+days] # increment and assign days to the value of the next index
    #             res[i] = days # assign days to result[i] (element at index i of res)
    #     return res
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        # keep track of numbers and their index
        track: list[dict] = []
        n = len(T)
        res = [0] * n
        # print(next(iter(track[0].items()))[0])

        for i in range(n - 1, -1, -1):
            curr = T[i]
            while len(track) != 0 and next(iter(track[0].items()))[1] <= curr:
                track.pop(0)
                
            res[i] = 0 if len(track) == 0 else next(iter(track[0])) - i
            track.insert(0, {i: curr})
            # while len(track) != 0 and next(iter(track)) <= curr:
        return res

# i = i + step
print(Solution.dailyTemperatures(Solution, [73, 74, 75, 71, 69, 72, 76, 73]))