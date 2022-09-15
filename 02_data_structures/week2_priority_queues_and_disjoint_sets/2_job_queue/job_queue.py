# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
debug = False


class Workers():
    def __init__(self, n):
        self.__size = n - 1    # size is always the same, as number of threads is the same
        self.__index = list(range(n))     # array of indices of the workers
        self.__next = [0] * n  # array of times when worker is next free

    def ExtractMin(self):
        next_free = self.__next[0]
        next_ind = self.__index[0]
        self.__next[0] = self.__next[self.__size]
        self.__index[0] = self.__index[self.__size]
        self.__size -= 1
        if debug:
            print('extract min at: ' + str(self.__size))
            print('next: ' + str(self.__next))
            print('index: ' + str(self.__index))
        self.SiftDown(0)
        if debug:
            print('after extract min')
            print('next: ' + str(self.__next))
            print('index: ' + str(self.__index))
        return next_free, next_ind

    def Insert(self, time, i):
        self.__size += 1
        self.__next[self.__size] = time
        self.__index[self.__size] = i
        if debug:
            print('insert at: ' + str(self.__size))
            print('next: ' + str(self.__next))
            print('index: ' + str(self.__index))
        self.SiftUp(self.__size)
        if debug:
            print('after insert: ')
            print('next: ' + str(self.__next))
            print('index: ' + str(self.__index))

    def Parent(self, i):
        return i//2

    def LChild(self, i):
        return 2*i

    def RChild(self, i):
        return 2*i+1

    def IsBefore(self, a_t, a_i, b_t, b_i):
        if a_t != b_t:
            return a_t < b_t
        return a_i < b_i

    def SiftUp(self, i):
        while i > 0 and self.IsBefore(self.__next[i], self.__index[i], self.__next[self.Parent(i)], self.__index[self.Parent(i)]):
            self.__next[self.Parent(i)], self.__next[i] = self.__next[i], self.__next[self.Parent(i)]
            self.__index[self.Parent(i)], self.__index[i] = self.__index[i], self.__index[self.Parent(i)]
            i = self.Parent(i)


    def SiftDown(self, i):
        m_ind = i
        l = self.LChild(i)
        r = self.RChild(i)
        if l <= self.__size and self.IsBefore(self.__next[l], self.__index[l], self.__next[m_ind], self.__index[m_ind]):
            m_ind = l
        if r <= self.__size and self.IsBefore(self.__next[r], self.__index[r], self.__next[m_ind], self.__index[m_ind]):
            m_ind = r
        if i != m_ind:
            self.__next[i], self.__next[m_ind] = self.__next[m_ind], self.__next[i]
            self.__index[i], self.__index[m_ind] = self.__index[m_ind], self.__index[i]
            self.SiftDown(m_ind)


def assign_jobs(n_workers, jobs):
    '''
    change to implementation with min heap for next_free_time with these methods:
    1. ExtractMin - replace the root with the last leaf and let it sift down
    2. Insert - attached at leftmost vacant position in the last level and sift up
    '''
    result = []
    workers = Workers(n_workers)
    for job in jobs:
        next_free, i = workers.ExtractMin()
        if debug:
            print('job: ' + str(job))
            print('next_free: ' + str(next_free) + ' next_ind: ' + str(i))
        result.append(AssignedJob(i, next_free))
        workers.Insert(next_free+job, i)

    ''' naive implementation
    next_free_time = [0] * n_workers
    for job in jobs:    # take jobs off queue one by one and assign to worker with the lowest next free time
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])    # index of the worker with the lowest next free time O(log(n))
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job  # keep cycling the work threads, and adding to the next available time
    '''
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
