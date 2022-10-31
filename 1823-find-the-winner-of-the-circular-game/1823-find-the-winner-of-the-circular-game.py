# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         q = [i for i in range(1, n + 1)]
#         while len(q) > 1:
#             for j in range(1, k+1):
#                 friend = q.pop(0)
#                 if j != k:
#                     q.append(friend)
#         return q[0]


# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         q = [i for i in range(1, n + 1)]
#         j = 0
#         while len(q) > 1:
#             j = (j + k - 1) % len(q)
#             q.pop(j)
#         return q[0]

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        return ((self.findTheWinner(n - 1, k) + k - 1) % n) +1
        