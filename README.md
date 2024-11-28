# Namma Metro Memory Game

An interactive game to test your knowledge of the operational and upcoming stations on Bengaluru's Namma Metro network!

Inspired by [Metro Memory](https://metro-memory.com/) by Benjamin Tran Dinh (which is much more professional and now features many more cities, you have to check it out!)

Currently there are two variants of the game : the original CLI based game, and the new Web based game. The CLI is built using Python, while the UI is built using Flask & Python for the backend and HTML & Leaflet.js for map visualization.

---
## Features
**Station Guessing Game:** Users can guess station names and track their progress.

#### CLI Features

- **Commands** Various commands can be used by the user to enhance the experience
    - `stats` can be used to see all stats including : 
        - Number of found stations
        - Number of stations found on each line
        - Stations left to find
        - Current progress %
        - Time in current session
        - Hints used
    - `found` can be used to list all currently found stations : 
        - Redacted display of every station on each line (only found stations are visible)
        - Unfound stations are displayed as underscores corresponding to station title length (tiny hint!)
    - `random` reveals a random unfound station's name (increments hint counter)
    - `clear` clears the screen (this **is** a command line interface)
    - `give up` displays users final stats and on pressing `Enter`, shows you all the stations you missed
    - `help` displays an informative message
    - `pause` pauses session timer, displays stats and clears the screen
        - While paused, stations cannot be guessed and hints cannot be used
        - No commands except `found` can be used
    - `quit` exits the program

#### Web Features

- **Interactive Map:** Displays Namma Metro stations on an interactive Leaflet.js map.
- **Dynamic Marker Updates:** Correctly guessed stations' markers turn green on the map.
- **Statistics Tracking:** View stats such as time elapsed, stations found, and completion percentage.

---

## Installation

### Prerequisites
- Python 3.7+
- Pip (Python Package Installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/PratyushBalaji/nmproject.git
   cd nmproject
   ```

2. Install required packages : (Currently only requires `flask`, all other imports are part of Python's standard library)
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   **Web version :** 
   ```bash
   python app.py
   ```
   Open your web browser and navigate to http://127.0.0.1:5000/

   **CLI version :**
   ```bash
   python stationGuesser.py
   ```

---

## File Structure

```
nmproject/
├── app.py                 # Flask application
├── README.md              # The file you are reading right now 
├── requirements.txt       # Requirements file
├── stationGuesser.py      # CLI-based variant of the game
├── stationInfo.py         # Metro station data and functions
├── stations.txt           # Text file with all stations on each line
└── templates/
    └── index.html         # Frontend for the web application
```

---

## How to Play

### CLI-based variant
1. Change directory to install location
2. Run `python stationGuesser.py` in your terminal.
3. Enter commands such as `stats`, `found`, `help`, etc, or guess stations
4. Enjoy!

### Web-based variant
1. Change directory to install location
2. Run `python app.py` in your terminal
3. Visit the url found in your terminal output (The default is http://127.0.0.1:5000/)
4. Type a station name in the text box and click "Submit" or hit "Enter".
5. Correct guesses will turn the corresponding station marker green on the map.
6. View your progress stats (time elapsed, stations found, etc.) above the map.

---

## Current Limitations

While the Namma Metro Memory Game is functional, there are several areas for improvement, especially with the web variant of the game.

1. **Random Coordinates for Markers**:
   - Currently, station markers are placed using random offsets on the map. This was purely for testing purposes and will be fixed.

2. **Unfinished UI**:
   - The user interface is extreeeeemely basic and lacks features such as tooltips, progress bars, or visual feedback beyond marker updates
   - The map has place locations which can kinda give away a station's location (if the coordinates were accurate that is...)
   - Clicking on a marker straight up tells you which station that corresponds to
   - Web page does not include stats for stations found on each line, etc

3. **Lack of Persistence**:
   - Game state (e.g., stations found, statistics) is persistant, however markers are not. Refreshing or reloading the page resets the markers.

4. **Limited Commands**:
   - While the CLI variant includes commands such as `stats`, `found`, `random`, `clear`, `help`, `pause`, `give up` and `quit`, the web variant does not allow for any command usage.
   - Only functionality on the web variant is typing in a station name
   - Future versions will include this functionality through UI elements like a pause button, etc

There's a lot more I haven't touched, but these are a few things I want to address in future versions. Feel free to fork or even use the data to make your own implementations.

---

## On The Future Of This Project

I'm honestly just a guy who likes trains. This project originally started as a way for me to test myself and see how many of the operational and under construction stations of the Namma Metro network I could recall from memory (super nerdy stuff, I know). Heck, I even have a whole Google Sheet filled with coach serial numbers, construction years, trainset liveries, etc that I used to religiously update everytime I saw a train pass by my balcony or rode the metro (which was a lot). 

As a result, this project is extremely catered to my needs and I'm not in much of a rush to make it look beautiful, be on top of bugs, etc. During initial development, I really didn't care how the output looked, how unintentionally "obfuscated" the code looked, or even how inefficient my logic was. Now I'm starting to pay more attention to the "professional development" aspect of this project, but due to the nature of how this project began, I'm not entirely sure how that looks.

Maybe someday I'll make it an actual professional website like the London-Tube-based "Metro Memory" game this whole thing was inspired by. Perhaps I can even get in contact with its creator Benjamin TD and learn how he makes all his cool projects. 