# Friend (or not) partitioning #

### How to separate everyone from everyone that they hate with an algorithm ###

---

This solves a problem given by an assignment for design and analysis of algorithms which is as follows:

A group of people is planning an expedition. For safety, they decide to split into two groups; it does not matter how many people are in each group. Not all of them are good friends, and one reason for splitting is to separate all pairs that are not friendly to each other. Your goal is to design and implement an algorithm that, given the map of friendship relations between people in the group, would find a partition of people into two groups of friends, or say that it is impossible. Assume that the input is an n x n matrix M, where n is the number of people in the group and M(i,j) = 1 if i and j are friends, and 0 otherwise. Also, if i is friendly, then j is friendly to i. Your output should be the sequence of numbers corresponding to people assigned to the first group.

---

Included in this repository are two python files

The main python file is called groupSplit.py. Currently to use it you place your friend matrix inside the file and run  `python groupSplit.py` / `python3 groupSplit.py` 

The other python file called createFriendNet.py generates an array based on a few parameters that you can copy and paste into groupSplit.py to test functionality.

To run this `python createFriendNet.py n x y` / `python3 createFriendNet.py n x y` 

Where n is the number of people in the network, and x, chance represent the proportion of values that will be 1 rather than 0. This can be read as an x in y chance. 

For example `python createFriendNet.py 10 9 10` creates a 10 x 10 friendship matrix where each person has a 9/10 or 90% chance of being any other persons friend.

---

## todo ##

- [x] implement algorithm 

- [x] optimize algorithm

- [ ] generate pseudo code

- [ ] add the ability to split into any number of groups

- [x]

- [x] wipe the last statement from your memory

