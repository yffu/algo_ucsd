from collections import deque
import queue


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        prev = t - 3000
        self.q.append(t)
        while self.q and self.q[0] < prev:
            self.q.popleft()
        return len(self.q)


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q, c_r, c_d, v_r, v_d = queue.Queue(), 0, 0, 0, 0
        for s in senate:
            if s == "R":
                c_r += 1
            elif s == "D":
                c_d += 1
            q.put(s)
        while q:
            s = q.get()
            if s == 'R':
                if v_d:
                    v_d -= 1
                    c_r -= 1
                else:
                    q.put(s)
                    v_r += 1
            elif s == 'D':
                if v_r:
                    v_r -= 1
                    c_d -= 1
                else:
                    q.put(s)
                    v_d += 1
            if c_d == 0:
                return "Radiant"
            elif c_r == 0:
                return "Dire"
            # print("queue: {}, c_r: {}, c_d: {}, v_r: {}, v_d: {}".format(q.queue, c_r, c_d, v_r, v_d))


if __name__ == '__main__':
    s = Solution()
    print(s.predictPartyVictory("RD"))
    print(s.predictPartyVictory("RDD"))
