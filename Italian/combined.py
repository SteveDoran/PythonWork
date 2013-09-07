# To allow command line argument management
import sys
# To process file lines for appropriate verb endings
import re
# Required to use the database entries file
import shelve

# Read the input filename from the command line
inputFile = sys.argv[1]

# Read the database filename from the command line
dbFile = sys.argv[2]

# Open the database file
try:
    # Open with 'n' flag to force creation of new database
    DB = shelve.open(dbFile)
except Exception as exc:
    print(exc)

# Dictionary of matched verbs
matchedVerbs = {}

# Open the input file as iterator instead of single line to avoid buffer overruns
for dataLine in open('verbs.txt'):
    # Cycle on all of the input file lines
    # Check through all known verb endings
    for ending in ('are', 'ire', 'ere'):
        # Attempt the match
        verbMatch = re.match('(.*)(' + ending + ')(\n*)$', dataLine)
        # Check for a match
        if verbMatch != None:
            # Read the shelve entry
            verbData = DB[ending]
            # match.group(0) is original text
            matchedVerbs[verbMatch.groups()[0] + verbMatch.group(2)] = verbData.printVerb(verbMatch.group(1))
            break
# List all resulting verb entries
for verb in matchedVerbs.keys():
    print('Verb {0} located\n'.format(verb))
    print('Conjugation:\n {0}'.format(matchedVerbs[verb]))
            
#print('Size: {1} {0}\n'.format(match.groups(), len(match.groups()))) 
#print('Size: %(length)s %(value)s\n' % {'value': match.groups(), 'length' : len(match.groups())}) 