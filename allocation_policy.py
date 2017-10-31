from hashing_policy import HashingPolicy
from random_policy import RandomPolicy

class AllocationPolicy:
    @classmethod
    def get_policy(cls, type):
        if type == "random":
            return RandomPolicy()

        if type == "hash":
            return HashingPolicy()

        print "No such type of policy defined"
        return