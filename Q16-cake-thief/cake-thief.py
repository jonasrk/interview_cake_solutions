#!/bin/python3

import sys
import os


# Complete the function below.

def zombieCluster(zombies):
    clusters = []
    for zombie_id, line in enumerate(zombies):
        zombie_in_cluster = False
        for cluster in clusters:
            if zombie_id in cluster:
                zombie_in_cluster = True
        if not zombie_in_cluster:
            new_zombie_set = set()
            new_zombie_set.add(zombie_id)
            clusters.append(new_zombie_set)
        for other_zombie_id, connection in enumerate(str(line)):
            if connection == "1":
                for cluster in clusters:
                    if zombie_id in cluster:
                        cluster.add(other_zombie_id)
    return len(set(clusters))

input = ["100000",
         "010000",
         "001000",
         "000100",
         "000010",
         "111111"]

print(zombieCluster(input))