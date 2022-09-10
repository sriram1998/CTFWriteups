In this question, an interactive shell is givem and we have to play a simple game against the computer. The description of the given is as follows:

```
In this game, two players take turns saying days of the year ("January 30", "July 5", etc)

The first player may start with any day in the month of January, and on each turn a player may say another date that either has the same month or the same day as the previous date. You can also only progress forward in time, never backwards.

For example, this is a valid series of moves:

Player 1: January 1
Player 2: February 1
Player 1: February 9
Player 2: July 9
Player 1: July 14
Player 2: July 30
Player 1: December 30
Player 2: December 31

This is an illegal set of moves:

Player 1: January 1
Player 2: July 29 (not same day or month)
Player 1: July 1 (going backwards in time)

The objective of the game is simple: be the first player to say December 31.
```

For getting the flag, we are supposed to win the computer 100 times in a row.

The simple logic here is that, if we give a set of month and date, we can always win against the computer. For instance, if we give Novemeber 30 as input, the computer has no choice but to give December 30. Which means I will win. 

Similarly if I give October 29, the computer has the following choices which are October 30, October 31, November 29, December 29. If computer chooses Oct 30, I can give Nov 30 and win as explained above. And for all the other options I can always win. October 31 -> December 31 ( I win ), November 29 -> November 30 -> I win as explained above. December 29 -> December 31 (I win)

Going backwards like this, I can generate a set of pair of dates and months for which I will always follow a sequence that will lead to my victory.

```winning_dates = {"January": 20, "February": 21, "March": 22, "April": 23, "May": 24, "June": 25, "July": 26, "August": 27, "September": 28, "October": 29, "November": 30, "December": 31}```

Having this logic in hand, it was fairly easy to code the logic. All I had to do was send in any of the above pairs according to the computers move and I can always win.

Implementaion in soln.py.

Final flag is ```ictf{br0ken_game_smh_8b1f014a}``

