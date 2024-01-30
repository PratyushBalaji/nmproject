import stationInfo
import random
import os
import time

# Inspired by metro-memory tube game
# Text input where user types in a station name
# If station exists in the dictionary :
#   Add it to the foundStations array
#   Print out the lines its on, percentage of stations found, etc
# Else : 
#   Print error about station not found

# Type 'stats' to reveal percentage, line-wise findings of stations
# Type 'give up' to give up and reveal missing stations
# Type 'random' to reveal a random unfound station
# Type 'found' to see all the stations you've found so far.
# Type 'clear' to clear the screen
# Type 'help' to display this message
# Type 'pause' to pause timer, stop any other commands
# Type 'quit' to quit


# Variables to store progress :
foundStations = set() # Stores all the stations that have been found so far. This is a set to optimize lookups as order doesn't matter here
missingStations = list(stationInfo.stationDict.keys()) # Stores all the stations that haven't been found yet. This is a list as random.choice() needs a list argument
totalNumberOfStations = len(stationInfo.stationDict) # Total number of known stations.
hintsUsed = 0 # Number of hints used

# Records how many stations have been found on each line, total line length, hints used per line
foundStationsPerLine = {'Purple':[0,len(stationInfo.purpleLine),0],
                        'Green':[0,len(stationInfo.greenLine),0],
                        'Blue':[0,len(stationInfo.blueLine),0],
                        'Yellow':[0,len(stationInfo.yellowLine),0],
                        'Pink':[0,len(stationInfo.pinkLine),0]}


def revealRandom():
    global hintsUsed
    revealedStation = random.choice(missingStations)
    missingStations.remove(revealedStation)
    foundStations.add(revealedStation)
    # Update found stations per line
    for i in stationInfo.getLines(revealedStation):
        foundStationsPerLine[i][0]+=1
    # Print revealed station
    print(f'Station Name : {revealedStation}')
    print(f'Line(s) : {', '.join(stationInfo.getLines(revealedStation))}')
    hintsUsed+=1

def statistics():
    # Prints user statistics
    
    # Tracking time
    global totalPauseTime
    currentTime = time.time()
    elapsedTime = currentTime - startTime - totalPauseTime
    minutes, seconds = divmod(int(elapsedTime), 60)
    timeString = f"{minutes} minutes, {seconds} seconds" if minutes else f"{seconds} seconds"
    print("Your current statistics: ")
    print(f"You have been playing for {timeString}")
    
    # Tracking stats
    print(f'Hints Used : {hintsUsed}')
    print(f'Number of stations found : {len(foundStations)}')
    print(f'Number of stations left to find : {len(missingStations)}')
    print(f'Percentage : {round(100*len(foundStations)/totalNumberOfStations,2)}%')

    print(f'Number of stations found on each line :')
    print(f'    Purple Line : {foundStationsPerLine['Purple'][0]}/{foundStationsPerLine['Purple'][1]} ({round(100*foundStationsPerLine['Purple'][0]/foundStationsPerLine['Purple'][1],2)}%)')
    print(f'    Green Line : {foundStationsPerLine['Green'][0]}/{foundStationsPerLine['Green'][1]} ({round(100*foundStationsPerLine['Green'][0]/foundStationsPerLine['Green'][1],2)}%)')
    print(f'    Blue Line : {foundStationsPerLine['Blue'][0]}/{foundStationsPerLine['Blue'][1]} ({round(100*foundStationsPerLine['Blue'][0]/foundStationsPerLine['Blue'][1],2)}%)')
    print(f'    Yellow Line : {foundStationsPerLine['Yellow'][0]}/{foundStationsPerLine['Yellow'][1]} ({round(100*foundStationsPerLine['Yellow'][0]/foundStationsPerLine['Yellow'][1],2)}%)')
    print(f'    Pink Line : {foundStationsPerLine['Pink'][0]}/{foundStationsPerLine['Pink'][1]} ({round(100*foundStationsPerLine['Pink'][0]/foundStationsPerLine['Pink'][1],2)}%)')

def listFound():
    # Lists all the found stations
    for lineIndex in range(len(stationInfo.allLines)):
        print(f"{stationInfo.allLineNames[lineIndex]} Line :")
        for stationName in stationInfo.allLines[lineIndex]:
            if stationName in foundStations:
                print(stationName)
            else:
                display = ""
                revealedChars = [' ','(',')']
                for i in stationName:
                    if i in revealedChars:
                        display+=i
                    else:
                        display+='_'
                print(display)
        print("\n\n")

def pause():
    os.system('cls')
    
    global lastPauseTime, totalPauseTime
    currentTime = time.time()
    elapsedTime = currentTime - startTime - totalPauseTime
    minutes, seconds = divmod(int(elapsedTime), 60)
    timeString = f"{minutes} minutes, {seconds} seconds" if minutes else f"{seconds} seconds"
    print(f"You have been playing for {timeString}")
    
    lastPauseTime = time.time()  # Record when the pause started
    while True:
        pauseInput = input("The game is paused, type 'play' to continue: ")
        if pauseInput.strip().lower() == 'play':
            totalPauseTime += time.time() - lastPauseTime  # Update total pause time
            break

welcomeMessage = '''
Hello, and welcome to the Namma Metro Memory Game!
The game currently supports the Purple, Green, Blue, Yellow and Pink lines.

Type in any station's name. If it exists on the metro map, it will show up as 'found' and contribute to your progress.
Type 'stats' to see how many stations you've found, how many you have left, and how many stations on each line you've found
Type 'found' to see all the stations you've found so far.
Type 'random' to reveal a random unfound station's name
Type 'clear' to clear the screen
Type 'give up' to give up and reveal all unfound stations
Type 'help' to display this message
Type 'pause' to pause the game
Type 'quit' to quit
'''

# Tracking time
startTime = time.time()
totalPauseTime = 0
lastPauseTime = 0

print(welcomeMessage)

while True:
    if len(foundStations) == totalNumberOfStations:
        print("Congratulations! You have found all stations! Thanks for playing!")
        statistics()
        break
    print()
    userInput = input("Enter Station Name or Command : ").strip().lower()
    stationGuess = stationInfo.alternativeStationNames.get(userInput, userInput)  # Finds alt name as stored in db if exists, else returns user input back
    # Input is a command
    if userInput == 'stats':
        statistics()
        continue
    if userInput == 'random':
        revealRandom()
        continue
    if userInput == 'give up':
        print('\n\n\nThanks for playing!')
        statistics()
        input("Press 'enter' to view unfound stations")
        print(f"Unfound Stations : \n{'\n'.join(missingStations)}")
        break
    if userInput == 'clear':
        os.system('cls')
        continue
    if userInput == 'help':
        print(welcomeMessage)
        continue
    if userInput == 'found':
        listFound()
        continue
    if userInput == 'pause':
        pause()
        continue
    if userInput == 'quit':
        break
    
    # Input is a guess
    if stationGuess in stationInfo.stationDict:
        if stationGuess not in foundStations:
            # Add to found stations and remove from missing stations
            foundStations.add(stationGuess)
            missingStations.remove(stationGuess)

            # Update found stations per line
            for i in stationInfo.getLines(stationGuess):
                foundStationsPerLine[i][0]+=1

            print(f"Station found: {stationGuess}")
            print(f"Line(s): {', '.join(stationInfo.getLines(stationGuess))}")
        else:
            print(f"You have already found the station : {stationGuess}")
        continue
    else:
        print("Station / Command not found. Try again, or type 'help' for help.")
        continue