from PLTable.pltable import PLTable
def menu():
    def instruction():
        print("""Possible commands:
    * new PL- creating new Premier League file;
    * show PLTable- showing Premier League table in a browser window;
    * update PL- updating Premier League file;
    * team fixtures- showing selected team fixtures ordered by their dates;
    * team results- showing selected team results ordered by their dates;
    * teams- showing all teams currently in a file
    * q- quit session, your Premier League file won't be in a process
    """)
    commands={'?':instruction,'new PL':PLTable.new_table,'show PLTable':PLTable.show_table,'update PL':PLTable.update_table,'team fixtures':PLTable.team_fixture,'team results':PLTable.team_results,'teams':PLTable.teams}
    x=input('What do you want to do? Press "?" for possible commands. ')
    while True:
        if x in commands.keys():
            commands[x]()
            x=input('What do you want to do? Press "?" for possible commands. ')
        elif x=='q':
            break
        else:
            print('Invalid command.')
            instruction()
            x = input('What do you want to do? Press "?" for possible commands. ')



