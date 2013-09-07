# The class that is the verb-types and suffix-endings
from verbdata import VerbData 
# To interact with an external pseudo-DB file
import shelve
# Command line argument support
import sys 

# Save the filename
databaseName = sys.argv[1]
# Open the file names by the command line argument
try:
    # Open with 'n' flag to force creation of new database
    DB = shelve.open(databaseName, flag='n')
except Exception as exc:
    print(exc)

# default function for the branch operation
def branchDefault(tense):
    print('Bad branch selection: %s' % tense)
    exit(1)

# Create an instance of 'are' verbs
verb = VerbData('are')
# Populate the 7 tenses of the verb
for tense in range(0, 7):
    # First the selection statement
    branch = { 0: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('o','i','a',
                                                'iamo','ate','ano')
                                              ),
               1: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('avo','avi','ava',
                                                'avamo','avate','avano')
                                              ),
               2: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('erò','erai','erà',
                                                'eremo','erete','eranno')
                                              ),
               3: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('erei','eresti','erebbe',
                                                'eremmo','ereste','erebbero')
                                              ),
               4: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('ai','asti','ò',
                                                'ammo','aste','arono')
                                              ),
               5: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('i','i','i',
                                                'iamo','iate','ino')
                                              ),
               6: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('assi','assi','asse',
                                                'assimmo','aste','assero')
                                              )
             }
    # Execute the branching step
    branch.get(tense, branchDefault)(tense)

# Now save the object in the shelve DB
DB['are'] = verb


# Create an instance of 'are' verbs
verb = VerbData('ire')
# Populate the 7 tenses of the verb
for tense in range(0, 7):
    # First the selection statement
    branch = { 0: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('o','i','e',
                                                'iamo','ite','ono')
                                              ),
               1: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('ivo','ivi','iva',
                                                'ivamo','ivate','ivano')
                                              ),
               2: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('irò','irai','irà',
                                                'iremo','irete','iranno')
                                              ),
               3: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('irei','iresti','irebbe',
                                                'iremmo','ireste','irebbero')
                                              ),
               4: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('iì','isti','ì',
                                                'immo','iste','irono')
                                              ),
               5: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('a','a','a',
                                                'iamo','iate','ano')
                                              ),
               6: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('issi','issi','isse',
                                                'issimmo','iste','issero')
                                              )
             }
    # Execute the branching step
    branch.get(tense, branchDefault)(tense)

# Now save the object in the shelve DB
DB['ire'] = verb


# Create an instance of 'are' verbs
verb = VerbData('ere')
# Populate the 7 tenses of the verb
for tense in range(0, 7):
    # First the selection statement
    branch = { 0: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('o','i','e',
                                                'iamo','ete','ono')
                                              ),
               1: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('evo','evi','eva',
                                                'evamo','evate','evano')
                                              ),
               2: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('erò','erai','erà',
                                                'eremo','erete','eranno')
                                              ),
               3: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('erei','eresti','erebbe',
                                                'eremmo','ereste','erebbero')
                                              ),
               4: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('ei','esti','ette',
                                                'emmo','este','ettero')
                                              ),
               5: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('a','a','a',
                                                'iamo','iate','ano')
                                              ),
               6: lambda tense: verb.setSuffix(verb.tenses[tense],
                                               ('essi','essi','esse',
                                                'essimmo','este','essero')
                                              )
             }
    # Execute the branching step
    branch.get(tense, branchDefault)(tense)

# Now save the object in the shelve DB
DB['ere'] = verb

# Close the database file to commit changes
DB.close()


