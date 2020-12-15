# Some experiments with generators
import os
import sys
import time
import itertools

sys.path.append(os.path.abspath("../"))
from procedures.procedure import Procedure


class testProc(Procedure):

    def __init__(self):
        super().__init__()
        self.nums = [x for x in range(5)]
        self.idx = 0

    def iteration(self):
        # forever loop
        while True:
            yield self.nums[self.idx]
            self.idx += 1
            if self.idx == len(self.nums):
                self.idx = 0


def main():
    p = testProc()
    gen = p.iteration()
    for _ in range(7):
        print(next(gen))
        time.sleep(1)


if __name__ == "__main__":
    main()
