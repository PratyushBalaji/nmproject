# Every station for every line stored in respective array
purpleLine = ['whitefield (kadugodi)', 'hopefarm channasandra', 'kadugodi tree park', 'pattandur agrahara', 'sri sathya sai hospital', 'nallur halli', 'kundalahalli', 'seetharampalya', 'hoodi', 'garudacharpalya', 'singayannapalya', 'kr pura', 'benniganahalli', 'baiyappanahalli', 'swami vivekananda road', 'indiranagar', 'halasuru', 'trinity', 'mahatma gandhi road', 'cubbon park', 'vidhana soudha', 'central college', 'nadaprabhu kempegowda majestic', 'ksr railway station', 'magadi road', 'hosahalli', 'vijayanagar', 'attigupe', 'deepanjali nagar', 'mysuru road', 'pantharapalya nayandahalli', 'rajarajeshwari nagar', 'jnanabarathi', 'pattanagere', 'kengeri bus terminal', 'kengeri', 'challaghatta']
greenLine = ['madavara', 'chikkabidarakallu', 'manjunathanagara', 'nagasandra', 'dasarahalli', 'jalahalli', 'peenya industry', 'peenya', 'goragunte palya', 'yeshwanthpur', 'sandal soap factory', 'mahalakshmi', 'rajajinagar', 'mahakavi kuvempu road', 'srirampura', 'mantri square sampige road', 'nadaprabhu kempegowda majestic', 'chickpete', 'kr market', 'national college', 'lalbagh', 'south end circle', 'jayanagar', 'rv road', 'banashankari', 'jp nagar', 'yelachenahalli', 'konanakunte cross', 'doddakallasandra', 'vajrahalli', 'thalaghattapura', 'silk institute']
blueLine = ['kial terminals', 'airport city', 'doddajala', 'chikkajala', 'bettahalasuru', 'begaluru cross', 'yelahanka', 'jakkuru plantation', 'jakkuru cross', 'kodigehalli', 'hebbala', 'kempapura', 'veerannapalya', 'nagawara', 'hbr layout', 'kalyan nagar', 'hrbr layout', 'horamavu', 'kasturi nagar', 'benniganahalli', 'kr pura', 'saraswathi nagar', 'drdo sports complex', 'doddanekundi', 'isro', 'marathahalli', 'kodibeesanahalli', 'kadubeesanahalli', 'belandur', 'ibbaluru', 'agara', 'hsr layout', 'central silk board']
yellowLine = ['rv road', 'ragigudde', 'jayadeva hospital', 'btm layout', 'central silk board', 'bommanahalli', 'hongasandra', 'kudlu gate', 'singasandra', 'hosa road', 'beratena agrahara', 'electronic city', 'konappana agrahara', 'huskur road (veerasandra)', 'hebbagodi', 'bommasandra']
pinkLine = ['nagawara', 'kadugundanahalli', 'venkateshpura', 'tannery road', 'pottery town', 'cantonment', 'shivajinagara', 'mahatma gandhi road', 'national military school', 'langford town', 'lakkasandra', 'dairy circle', 'tavarakere', 'jayadeva hospital', 'jp nagar 4th phase', 'iim bangalore', 'hulimavu', 'kalena agrahara']

allLines = [purpleLine,greenLine,blueLine,yellowLine,pinkLine]
allLineNames = ["Purple","Green","Blue","Yellow","Pink"]

# Every station is a dict entry with the key=station name, val=[names of lines it serves]
# This function populates the stationDict dictionary given a line array, and the name of the line
def populate(line, name):
    for station in line:
        if station in stationDict:
            stationDict[station].append(name)
        else:
            stationDict[station] = [name]

# Returns the line for a valid station (Input is assumed to be valid)       
def getLines(station):
    if station in stationDict:
        return stationDict[station]
    return # Invalid Station

# Every station and line it serves
stationDict = {'whitefield (kadugodi)': ['Purple'], 
               'hopefarm channasandra': ['Purple'], 
               'kadugodi tree park': ['Purple'],
               'pattandur agrahara': ['Purple'],
               'sri sathya sai hospital': ['Purple'],
               'nallur halli': ['Purple'],
               'kundalahalli': ['Purple'], 
               'seetharampalya': ['Purple'], 
               'hoodi': ['Purple'],
               'garudacharpalya': ['Purple'],
               'singayannapalya': ['Purple'],
               'kr pura': ['Purple', 'Blue'],
               'benniganahalli': ['Purple', 'Blue'],
               'baiyappanahalli': ['Purple'],
               'swami vivekananda road': ['Purple'],
               'indiranagar': ['Purple'],
               'halasuru': ['Purple'],
               'trinity': ['Purple'],
               'mahatma gandhi road': ['Purple', 'Pink'],
               'cubbon park': ['Purple'],
               'vidhana soudha': ['Purple'],
               'central college': ['Purple'],
               'nadaprabhu kempegowda majestic': ['Purple', 'Green'],
               'ksr railway station': ['Purple'],
               'magadi road': ['Purple'],
               'hosahalli': ['Purple'],
               'vijayanagar': ['Purple'],
               'attigupe': ['Purple'],
               'deepanjali nagar': ['Purple'],
               'mysuru road': ['Purple'],
               'pantharapalya nayandahalli': ['Purple'],
               'rajarajeshwari nagar': ['Purple'],
               'jnanabarathi': ['Purple'],
               'pattanagere': ['Purple'],
               'kengeri bus terminal': ['Purple'],
               'kengeri': ['Purple'], 
               'challaghatta': ['Purple'],
               'madavara': ['Green'],
               'chikkabidarakallu': ['Green'],
               'manjunathanagara': ['Green'], 
               'nagasandra': ['Green'],
               'dasarahalli': ['Green'],
               'jalahalli': ['Green'],
               'peenya industry': ['Green'], 
               'peenya': ['Green'], 
               'goragunte palya': ['Green'],
               'yeshwanthpur': ['Green'],
               'sandal soap factory': ['Green'],
               'mahalakshmi': ['Green'],
               'rajajinagar': ['Green'], 
               'mahakavi kuvempu road': ['Green'],
               'srirampura': ['Green'], 
               'mantri square sampige road': ['Green'],
               'chickpete': ['Green'], 
               'kr market': ['Green'],
               'national college': ['Green'], 
               'lalbagh': ['Green'], 
               'south end circle': ['Green'], 
               'jayanagar': ['Green'], 
               'rv road': ['Green', 'Yellow'], 
               'banashankari': ['Green'], 
               'jp nagar': ['Green'], 
               'yelachenahalli': ['Green'], 
               'konanakunte cross': ['Green'], 
               'doddakallasandra': ['Green'], 
               'vajrahalli': ['Green'],
               'thalaghattapura': ['Green'], 
               'silk institute': ['Green'], 
               'kial terminals': ['Blue'], 
               'airport city': ['Blue'], 
               'doddajala': ['Blue'],
               'chikkajala': ['Blue'],
               'bettahalasuru': ['Blue'],
               'begaluru cross': ['Blue'], 
               'yelahanka': ['Blue'], 
               'jakkuru plantation': ['Blue'],
               'jakkuru cross': ['Blue'], 
               'kodigehalli': ['Blue'],
               'hebbala': ['Blue'],
               'kempapura': ['Blue'],
               'veerannapalya': ['Blue'],
               'nagawara': ['Blue', 'Pink'], 
               'hbr layout': ['Blue'], 
               'kalyan nagar': ['Blue'],
               'hrbr layout': ['Blue'],
               'horamavu': ['Blue'], 
               'kasturi nagar': ['Blue'],
               'saraswathi nagar': ['Blue'],
               'drdo sports complex': ['Blue'],
               'doddanekundi': ['Blue'], 
               'isro': ['Blue'], 
               'marathahalli': ['Blue'],
               'kodibeesanahalli': ['Blue'],
               'kadubeesanahalli': ['Blue'],
               'belandur': ['Blue'],
               'ibbaluru': ['Blue'],
               'agara': ['Blue'], 
               'hsr layout': ['Blue'],
               'central silk board': ['Blue', 'Yellow'],
               'ragigudde': ['Yellow'],
               'jayadeva hospital': ['Yellow', 'Pink'],
               'btm layout': ['Yellow'],
               'bommanahalli': ['Yellow'], 
               'hongasandra': ['Yellow'],
               'kudlu gate': ['Yellow'], 
               'singasandra': ['Yellow'], 
               'hosa road': ['Yellow'],
               'beratena agrahara': ['Yellow'],
               'electronic city': ['Yellow'],
               'konappana agrahara': ['Yellow'],
               'huskur road (veerasandra)': ['Yellow'], 
               'hebbagodi': ['Yellow'],
               'bommasandra': ['Yellow'], 
               'kadugundanahalli': ['Pink'],
               'venkateshpura': ['Pink'],
               'tannery road': ['Pink'],
               'pottery town': ['Pink'], 
               'cantonment': ['Pink'],
               'shivajinagara': ['Pink'],
               'national military school': ['Pink'], 
               'langford town': ['Pink'], 
               'lakkasandra': ['Pink'], 
               'dairy circle': ['Pink'],
               'tavarakere': ['Pink'], 
               'jp nagar 4th phase': ['Pink'],
               'iim bangalore': ['Pink'],
               'hulimavu': ['Pink'], 
               'kalena agrahara': ['Pink']}

# Alternative names for stations (mg road vs mahatma gandhi road)
alternativeStationNames = {
    'whitefield': 'whitefield (kadugodi)',
    'kadugodi': 'whitefield (kadugodi)',
    'mg road': 'mahatma gandhi road',
    'huskur road':'huskur road (veerasandra)',
    'veerasandra':'huskur road (veerasandra)'
    # Add more mappings as necessary
}