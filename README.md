# SHSassassin

Program to manage SHS' assassin game.

People will sign up to play using a Google Survey.  The results of the survey will be downloaded as a csv file.  Then the host computer will run gamesetup.py to set up the game.  This will result in a csv file called masterlist that has all of the information like assassins, targets, emails, and IDs.  gamesetup.py also emails everyone who their target is.

Then a computer will run the killchecker.py file every 5 minutes or so.  This will download a Google Survey with all of the kills.  After confirming the kills, the program removes the eliminated players from the master list, emails the assassin who their next target is, sends out a tweet detailing who was eliminated, and updates the masterlist.csv file.
