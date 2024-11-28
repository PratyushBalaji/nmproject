from flask import Flask, request, jsonify, render_template
import stationInfo
import time
import random

app = Flask(__name__)

# Game state
game_state = {
    'foundStations': set(),
    'missingStations': list(stationInfo.stationDict.keys()),
    'startTime': time.time(),
    'totalPauseTime': 0,
    'hintsUsed': 0,
    'foundStationsPerLine': {line: [0, len(station)] for line, station in zip(stationInfo.allLineNames, stationInfo.allLines)},
}

@app.route('/')
def index():
    # Serialize stationDict for frontend
    return render_template('index.html', stationDict=stationInfo.stationDict)

@app.route('/guess', methods=['POST'])
def guess_station():
    """Process user guesses."""
    data = request.get_json()
    print("Received data:", data)  # Debugging
    station_name = data.get('stationName', '').lower()
    print("Station Name:", station_name)  # Debugging

    # Match station name or alternative
    station_guess = stationInfo.alternativeStationNames.get(station_name, station_name)
    if station_guess in stationInfo.stationDict:
        if station_guess not in game_state['foundStations']:
            game_state['foundStations'].add(station_guess)
            game_state['missingStations'].remove(station_guess)
            for line in stationInfo.getLines(station_guess):
                game_state['foundStationsPerLine'][line][0] += 1
            return jsonify({'status': 'success', 'message': f'Station found: {station_guess}', 'station': station_guess})
        return jsonify({'status': 'info', 'message': f'Station already found: {station_guess}'})
    return jsonify({'status': 'error', 'message': 'Station not found!'})

@app.route('/stats', methods=['GET'])
def stats():
    """Return current game statistics."""
    elapsed_time = time.time() - game_state['startTime'] - game_state['totalPauseTime']
    minutes, seconds = divmod(int(elapsed_time), 60)
    return jsonify({
        'time': f"{minutes}m {seconds}s",
        'hintsUsed': game_state['hintsUsed'],
        'stationsFound': len(game_state['foundStations']),
        'stationsLeft': len(game_state['missingStations']),
        'percentage': round(100 * len(game_state['foundStations']) / len(stationInfo.stationDict), 2),
        'foundStationsPerLine': game_state['foundStationsPerLine'],
    })

@app.route('/reveal-random', methods=['GET'])
def reveal_random():
    """Reveal a random station."""
    if game_state['missingStations']:
        revealed_station = random.choice(game_state['missingStations'])
        game_state['missingStations'].remove(revealed_station)
        game_state['foundStations'].add(revealed_station)
        for line in stationInfo.getLines(revealed_station):
            game_state['foundStationsPerLine'][line][0] += 1
        game_state['hintsUsed'] += 1
        return jsonify({'station': revealed_station})
    return jsonify({'error': 'No stations left to reveal!'})

@app.route('/found-stations', methods=['GET'])
def found_stations():
    """Return the list of found stations."""
    return jsonify(list(game_state['foundStations']))

if __name__ == '__main__':
    app.run(debug=True)
