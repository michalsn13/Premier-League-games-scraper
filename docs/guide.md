## Guide for the project

**How to get started?**
 1. Be sure that you have PostgreSQL with existing database.
 2. Put your database logging parameters in */Connection/'con_parameters.sample.py'* file.
 3. Rename the file to *'con_parameters.py'* (delete that *'sample'* part)
 4. Run 'app.py' and follow the instructions (type *'?'* if nessesary).

**Classes:**
* locators, queries and parameters classes:
  * Con_parameters (file: */Connection/con_parameters.py*)- stores logging parameters for connecting to SQL database
  * Game_locators (file: */Game/game_locators.py*)- stores css selectors for scraping single game details
  * Gameweek_locators (file: */Gameweek/gameweek_locators.py*)- stores css selectors for scraping whole gameweek of games
  * Queries (file: */PLTable/pltable_queries.py*)- stores PostgreSQL queries for visualization of games data stored in SQLTable
* environment classes:
  * Connection (file: */Connection/connection.py*)- simplifies connecting to the database with *enter* and *exit* dunder methods
* data classes:
  * Game (file: */Game/game.py*)- scrapes from html-code and stores information about perticular game in instance's properties
  * Gameweek (file: */Gameweek/gameweek.py*)- scrapes from html-code and stores list of Game instances of a specified gameweek
  * PLTable (file: */PLtABLE/pltable.py*)- takes Game instances and puts their data inside created SQLTable, provides informations such as current standings or given team fixtures/results
 
 **Main files:**
 * *menu.py*- with function menu() manages methods used in data classes in a more "user friendly" way, runs perticular code from given input
 * *app.py*- runs menu() from *menu.py*
 
  
