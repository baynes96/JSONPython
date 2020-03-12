'''
Created on Jan 11, 2020

https://www.nps.gov/subjects/developer/api-documentation.htm
Bill Nicholson
nicholdw@ucmail.uc.edu
@author: nicomp
'''
import json
import requests
import dictionary_utilities     # Eclipse shows a "not found" error here but we still need this

def get_info_from_one_park():
    response = requests.get('https://developer.nps.gov/api/v1/parks?parkCode=acad&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    #print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    total = int(parsed_json['total'])        # The number of parks that were returned
    for park in parsed_json['data']:
        print (park)
    
def get_alerts_from_smokey_mountains():
    # Great Smokey Mountains code is grsm
    response = requests.get('https://developer.nps.gov/api/v1/alerts?parkCode=grsm&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3')
    json_string = response.content
    parsed_json = json.loads(json_string)   # Now we have a python dictionary
    total = int(parsed_json['total'])        # The number of alerts that were returned
    for alert in parsed_json['data']:
        print (alert)
        print(alert['title'])

def college_scorecard():
    '''
    Get a boatload of college information about some schools
    Study the Data Dictionary here: https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx
    '''
    URL = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size&api_key=pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3'
    response = requests.get(URL)
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    dictionary_utilities.iterate_dictionary(parsed_json)
#    for school in parsed_json['results']:
#        print (school['school.name'])
#        for key, value in parsed_json.items():
#            print(key, '->', value)


def get_all_artwork_from_smithsonian():
    '''
    Retrieve all the artwork from the museum.
    https://smithsonian.github.io/api-docs/#/SAAM 
    '''
    URL = 'https://api.si.edu/saam/v1/artworks/'
    response = requests.get(URL, params={}, headers={'X-Api-Key': 'pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3'})
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    print(parsed_json)
    for art_data in parsed_json['data']:
        print (art_data)
    

def get_art_info_from_smithsonian():
    '''
    Get information about a work of art. The work of art is identified by a uuid in the URL variable, below.
    https://smithsonian.github.io/api-docs/#/SAAM
    '''
    URL = 'https://api.si.edu/saam/v1/artworks/dd19ac03-04e8-4d20-bfe9-ecfc238ebd54'
    response = requests.get(URL, params={}, headers={'X-Api-Key': 'pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3'})
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    dictionary_utilities.iterate_dictionary(parsed_json)
#    print(parsed_json)
#    art_data = parsed_json['data']
#    print (art_data)
#    print(art_data['type'])


def get_candidates():
    '''
    https://api.open.fec.gov/developers/#/candidate/get_candidate__candidate_id__
    https://godoc.org/github.com/tmc/openfec
    
    Also interesting: https://www.fec.gov/data/browse-data/?tab=bulk-data
    '''
    URL = 'https://api.open.fec.gov/v1/candidates/?page=99'
    response = requests.get(URL, params={}, headers={'X-Api-Key': 'pfJKDXPzTykVL73ehnPyY8pkDQLjfq5cz5LqCkl3'})
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
#   print (parsed_json)
    results = parsed_json['results']
    dictionary_utilities.iterate_dictionary(parsed_json)
#    for data in results:
#       print (data)
#        print (data['name']),
#        print(data['party'])

#get_art_info_from_smithsonian()
#get_candidates()
#get_all_artwork_from_smithsonian()
#college_scorecard()
#get_alerts_from_smokey_mountains()

