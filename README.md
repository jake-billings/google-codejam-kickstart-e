# google-codejam-kickstart-e
This repository contains my code for Google Codejam Kickstart round E.

### Question 1

There exist some cities that are built along a straight road. The cities are numbered 1, 2, 3... from left to right.

There are N GBuses that operate along this road. For each GBus, we know the range of cities that it serves: the i-th gBus serves the cities with numbers between Ai and Bi, inclusive.

We are interested in a particular subset of P cities. For each of those cities, we need to find out how many GBuses serve that particular city.

Input
The first line of the input gives the number of test cases, T. Then, T test cases follow; each case is separated from the next by one blank line. (Notice that this is unusual for Kickstart data sets.)

In each test case:

The first line contains one integer N: the number of GBuses.
The second line contains 2N integers representing the ranges of cities that the buses serve, in the form A1 B1 A2 B2 A3 B3 ... AN BN. That is, the first GBus serves the cities numbered from A1 to B1 (inclusive), and so on.
The third line contains one integer P: the number of cities we are interested in, as described above. (Note that this is not necessarily the same as the total number of cities in the problem, which is not given.)
Finally, there are P more lines; the i-th of these contains the number Ci of a city we are interested in.
Output
For each test case, output one line containing Case #x: y, where x is the number of the test case (starting from 1), and y is a list of P integers, in which the i-th integer is the number of GBuses that serve city Ci.

Limits
1 ≤ T ≤ 10.
Small dataset
1 ≤ N ≤ 50
1 ≤ Ai ≤ 500, for all i.
1 ≤ Bi ≤ 500, for all i.
1 ≤ Ci ≤ 500, for all i.
1 ≤ P ≤ 50.
Large dataset
1 ≤ N ≤ 500.
1 ≤ Ai ≤ 5000, for all i.
1 ≤ Bi ≤ 5000, for all i.
1 ≤ Ci ≤ 5000, for all i.
1 ≤ P ≤ 500.

Sample Input
```
Input

2
4
15 25 30 35 45 50 10 20
2
15
25

10
10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5
3
5
10
27

```

Sample Output
```
Output

Case #1: 2 1
Case #2: 3 3 4


```

### Question 2


Your team is about to prove itself in a dance battle! Initially, your team has E points of energy, and zero points of honor. There are N rival teams who you must face; the i-th of these teams is the i-th in a lineup, and has a dancing skill of Si.

In each round of battle, you will face the next rival team in the lineup, and you can take one of the following actions:

Dance: Your team loses energy equal to the dancing skill of the rival team, and that team does not return to the lineup. You gain one point of honor. You cannot take this action if it would make your energy drop to 0 or less.
Delay: You make excuses ("our shoes aren't tied!") and the rival team returns to the back of the lineup. Your energy and honor do not change.
Truce: You declare a truce with the rival team, and that team does not return to the lineup. Your energy and honor do not change.
Recruit: You recruit the rival team onto your team, and that team does not return to the lineup. Your team gains energy equal to the dancing skill of the rival team, but you lose one point of honor. You cannot take this action if it would make your honor drop below 0.
The battle is over when there are no more rival teams in the lineup. If you make optimal decisions, what is the maximum amount of honor you can have when the battle is over?

Input
The first line of the input gives the number of test cases, T. T test cases follow; each consists of two lines. The first line consists of two integers E and N: your team's energy, and the number of rival teams. The second line consists of N integers Si; the i-th of these represents the dancing skill of the rival team that is i-th in line at the start of the battle.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum amount of honor you can have when the battle is over.

Sample Input
```
2
100 1
100
10 3
20 3 15
```

Sample Input
```
Case #1: 0
Case #2: 1
```