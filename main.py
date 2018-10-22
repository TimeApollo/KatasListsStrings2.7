#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python 2.7 Katas Lists and Strings.

First exercise in Python printing katas 1 that we learned in Javascript.

author: TimeApollo
"""

import re

gotCitiesCSV = "King's Landing,Braavos,Volantis,Old Valyria,Free Cities,Qarth,Meereen"
lotrCitiesList = ["Mordor","Gondor","Rohan","Beleriand","Mirkwood","Dead Marshes","Rhun","Harad"]
bestThing = "The best thing about a boolean is even if you are wrong you are only off by a bit"

def main():
    print '1. ----------------------------------'

    print gotCitiesCSV.split(',')

    print '2. ----------------------------------'

    print bestThing.split(' ')

    print '3. ----------------------------------'

    print gotCitiesCSV.replace(',',';')

    print '4. ----------------------------------'

    print ','.join(lotrCitiesList)

    print '5. ----------------------------------'

    print lotrCitiesList[:5]

    print '6. ----------------------------------'

    print lotrCitiesList[-5:]

    print '7. ----------------------------------'

    print lotrCitiesList[3:6]

    print '8. ----------------------------------'

    lotrCitiesList.remove('Rohan')
    print lotrCitiesList

    print '9. ----------------------------------'

    del lotrCitiesList[lotrCitiesList.index("Dead Marshes") + 1 :]
    print lotrCitiesList

    print '10. ----------------------------------'

    lotrCitiesList.insert(lotrCitiesList.index("Gondor") + 1, "Rohan")
    print lotrCitiesList

    print '11. ----------------------------------'

    lotrCitiesList[lotrCitiesList.index('Dead Marshes')] = 'Deadest Marshes'
    print lotrCitiesList

    print '12. ----------------------------------'

    print bestThing[0:14]

    print '13. ----------------------------------'

    print bestThing[-12:]

    print '14. ----------------------------------'

    print bestThing[23:38]

    print '15. ----------------------------------'

    print bestThing.index('only')

    print '16. ----------------------------------'

    print bestThing.index(bestThing.split(' ')[-1])

    print '17. ----------------------------------'
    # used regex. can find any of the double vowels.
    # findalll only returns matched characters so have to pull out whole word.
    doubleVowels = re.compile(r'aa|ee|ii|oo|uu')
    for city in gotCitiesCSV.split(','):
        found = doubleVowels.findall(city)
        if found: print city + ',', 

    print '\n18. ----------------------------------'
    # good example in regex of using metacharacters
    endingOR = re.compile(r'or$')
    for city in lotrCitiesList:
        found = endingOR.findall(city)
        if found: print city + ',', 

    print '\n19. ----------------------------------'

    beginningB = re.compile(r'^b', re.IGNORECASE)
    for word in bestThing.split(' '):
        found = beginningB.findall(word)
        if found: print word + ',', 

    print '\n20. ----------------------------------'

    print 'Yes' if 'Mirkwood' in lotrCitiesList else 'No'

    print '21. ----------------------------------'

    print 'Yes' if 'Hollywood' in lotrCitiesList else 'No'

    print '22. ----------------------------------'

    print lotrCitiesList.index('Mirkwood')

    print '23. ----------------------------------'

    print next(city for city in lotrCitiesList if ' ' in city)

    print '24. ----------------------------------'

    lotrCitiesList.reverse()
    print lotrCitiesList

    print '25. ----------------------------------'

    list.sort(lotrCitiesList)
    print lotrCitiesList

    print '26. ----------------------------------'

    list.sort(lotrCitiesList, key=lambda city: len(city))
    print lotrCitiesList

    print '27. ----------------------------------'

    popped = lotrCitiesList.pop()
    print lotrCitiesList

    print '28. ----------------------------------'

    lotrCitiesList.append(popped)
    print lotrCitiesList

    print '29. ----------------------------------'

    removed = lotrCitiesList.pop(0)
    print lotrCitiesList

    print '30. ----------------------------------'

    lotrCitiesList.insert(0, removed)
    print lotrCitiesList


if __name__ == '__main__':
    main()