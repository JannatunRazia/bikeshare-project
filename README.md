# <u>**Explore US Bikeshare Data**</u>
In this project, the bike share system usage between three large cities: Chicago, New York City, and Washington, DC will be compared. </br>
Data provided by [Motivate](https://www.motivateco.com/) will be used here.

### *What is Bike Share Data*
Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. It is easy for a user of the system to access a dock within the system to unlock or return bicycles.</br>
Regardless, each bike can serve several users per day. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

### *Project Data*
* chicago.csv
* new_york_city.csv
* washington.csv

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### *Project Details*
###### The program takes user input:</br>
for the city(Chicago, New York City or Washington), </br>
for which month user wants to view the data(January, February, March, April, May, June or All) and </br>
for which day(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All).

###### Depending on the user input, the program shows the following output: </br>
* _Popular times of travel:_ (most common month, most common day of week, most common hour of day)

* _Popular stations and trip:_ (most common start station, most common end station, most common trip from start to end)

* _Trip duration:_ (total travel time, average travel time)

* _User info:_ (counts of each user type, counts of each gender, earliest, most recent, most common year of birth)

At the end it will ask if the user wants to restart the program or not.

### *Software Requirement*
To complete this project, the following software will be needed:
* [Python 3](https://www.python.org/), [NumPy](https://numpy.org/), and [pandas](https://pandas.pydata.org/) installed using Anaconda
* A text editor, like [Sublime](https://www.sublimetext.com/) or [Atom](https://atom.io/).
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

_**Documentation has been written by** Jannatun Razia with the help of Udacity guidelines._
