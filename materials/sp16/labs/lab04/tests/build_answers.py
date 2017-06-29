from datascience import *
import numpy as np

def all_columns_equal(t1, t2):
    if t1.num_columns != t2.num_columns:
        return False
    
    for i in range(t1.num_columns):
        if np.any(t1.column(i) != t2.column(i)):
            return False

    return True


def q12answer1():
    t = Table.read_table("twitter_follows.csv")
    t = t.where(t.column("Followers") > 5000000)
    return t

def q15answer():
    t = Table().with_columns(["Medium", ["Both", "Film", "TV"],
                              "count", [4, 2, 2]])
    return t


def q16answer():
    columns = ["Medium", ["Both", "Film", "TV"],
               "Followers amax", [6.89094e+06, 1.40822e+07, 9.37407e+06],
               "Friends amax", [1931, 1178, 3341]]
    t = Table().with_columns(columns)
    return t
