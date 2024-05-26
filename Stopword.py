import operator


def SWRLower(dictionary):
    global totalTf
    totalTf= 0
    keystore = []
    for value in dictionary.values():
        totalTf += value
    for key, value in dictionary.items():
        RF = value / totalTf
        lowerThreshold = 0.0001
        if RF < lowerThreshold:
            keystore.append(key)
    for key in keystore:
        dictionary.pop(key)
    return dictionary

def SWRUpper(dictionary):
    totalTf = 0
    keystore = []
    for value in dictionary.values():
        totalTf += value
    for key, value in dictionary.items():
        RF = value / totalTf
        UpperThreshold = 0.01
        if RF > UpperThreshold:
            keystore.append(key)
    for key in keystore:
        dictionary.pop(key)
    return dictionary






