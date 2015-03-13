# SHSassassin

What is the assassin game?  From [Wikipedia](http://en.wikipedia.org/wiki/Assassin_%28game%29):

>Assassin (also Gotcha, Assassins, KAOS (Killing as organized sport), Juggernaut, Battle Royal, Paranoia, Killer, Elimination, or Circle of Death) is a live-action game. Players try to eliminate each other from the game using mock weapons in an effort to become the last surviving player.

>Assassin is particularly popular on college campuses; several universities have a dedicated "Assassins' Guild" society, which organizes games for their members. Game play occurs at all hours and in all places unless otherwise disallowed by the rules. Since an elimination attempt could occur at any time, successful players are obliged to develop a healthy degree of watchful paranoia.

I wrote this program to manage my school's assassin game.

People will sign up to play using a Google Survey.  The results of the survey will be downloaded as a csv file.  Then gamesetup.py will be run to set up the game.  This will result in the creation of 'masterlist.csv', which contains information like remaining assassins, their targets, their emails, and their unique IDs.  gamesetup.py also emails every assassion who their target is.

A task scheduler will run killchecker.py every five minutes.  This will download the result of a Google Survey used to report kills.  After confirming the kills, the program removes the eliminated players from 'masterlist.csv', emails successful assassins who their next targets are, and sends out tweets detailing who was eliminated and how many assassins remain.
