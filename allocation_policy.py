from hashing_policy import HashingPolicy
from random_policy import RandomPolicy
from shortest_job_first_policy import SJF

class AllocationPolicy:
    @classmethod
    def get_policy(cls, type):
        if type == "random":
            return RandomPolicy()

        if type == "hash":
            return HashingPolicy()

        if type == "sjf":
            return SJF()

        print "No such type of policy defined"

        return