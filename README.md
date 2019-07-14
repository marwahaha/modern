# modern

Notes on development available here:
https://docs.google.com/document/d/1PVrSsz4vDbDg07fLS2YzS0XoUwGU5c5QQJ66YOZdAx8/edit?usp=sharing


This is a work in progress of a Magic: the Gathering simulator capable of handling all
cards printed in the last 15 years. This amounts to 10,000+ cards.

Simulator handles the board and turn progression. Player handles individual actions (ie, 
drawing cards, shuffling, manipulating your deck, etc), and prompts Strategy to make
decisions when necessary. Card handles the individual cards. 

Simulator
This prompts player when they're given an opportunity to do something. Cards in play
and spells cast are handled by simulator (although the actual objects' code is stored
in card.py, simulator instantiates these objects). Simulator passes priority and checks
for abilities of cards in play, and gives player permission to do something whenever they
have priority (see pass_priority).

Player
This handles individual deck manipulations. The deck list is also given as a variable 
in instantiating a player object. Player prompts Strategy to make a decision when ever
the opportunity arises, but handles decision-less actions like drawing cards, taking
damage, etc

Strategy
This is just a basic, hard coded stupid AI right now, so I can test the rest of the 
simulator

Card
This is where all cards will live. The attributes every card needs will be in 
card_template, since some cards will reference "non creature" or "instant". 
Every spell also needs the ability to be rewound while casting because it may
suddenly become illegal to cast the spell.


This project is inspired by this project:
https://www.reddit.com/r/magicTCG/comments/4y3ooc/results_of_two_ais_playing_millions_of_games_of/

The first steps now are to have a Magic: the Gathering engine that's capable
of goldfishing modern Gifts Storm following some basic hard coded heuristics. The next
step is to be able to write games to a database efficiently. Eventually, I hope to expand
this game engine to be able to support all tier 1/2 modern decks, and develop 
some kind of AI to find optimal lines and experiment with other cards.
