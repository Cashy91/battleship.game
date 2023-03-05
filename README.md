<h1>Battleship Conqueror</h1>

<p>Battleship Conqueror is a Python terminal game. It runs in the Code institute mock terminal on Heroku.<br>
The goal is to take out the Battleships on the board before your ammunition runs out. There are 5 ships hidden from the radar wich the unser needs to find.
</p>

[This is a link to the game](https://battleshipsgame.herokuapp.com/)<br>


![Image of different screen-sizes](Readme.images/Battleships-responsiveness.png)

<br>
<h1>Game functions</h1>

<p>Game instructions:<br>
Gives the user short info about the game<br>

![Image of intro information about the battleship game](Readme.images/battleshipsinfo.png)



<p>
Random board generation:
<br> 2 bords is generated one hidden wich contains the 5 battleships and the other is a blank one that keeps track och the users actions.</p>


![Image of the battefild board](Readme.images/battleshipsfunctions.png)

<p>Tracking correct user input:
<br>Checking if the user have entered a correct row and column also checks for repeat inputs.
Tracks the number of hits by the user and the turns remaining before losing the game if the user havent destoyed all ships before then.
<br>

![Image of the testing of hit trecking of ships and how many turns that remains.](Readme.images/battleshipstracking.png)

![Image of testing when targetting the same row and column.](Readme.images/battleshipstesting.png)

![Image of testing when not entering 1-8 for row and A-H for column.](Readme.images/battleshipstesting2.png).