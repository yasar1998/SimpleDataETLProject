import pandas as pd

extract_csv = pd.read_csv('resources/extract.csv')
extract_json = pd.read_json('resources/extract.json')


def mergeDataSets(dataSet1, dataSet2):
    dataSet = dataSet1.append(dataSet2, ignore_index=True)
    return dataSet


def removeNullValues(dataSet):
    null_removed = dataSet.dropna()
    null_removed = null_removed.reset_index(drop=True)
    return null_removed


def removeDuplicates(dataSet):
    dataSet.drop_duplicates(inplace=True)
    duplicates_removed = dataSet.reset_index(drop=True)
    return duplicates_removed


def calculateBMI(weight, height):
    return weight / (height ** 2)


extract = mergeDataSets(extract_csv, extract_json)
extract = removeNullValues(extract)
extract = removeDuplicates(extract)
extract['body_mass_index'] = calculateBMI(extract['weight'], extract['height'])

extract.to_csv('resources/load.csv', index=False)
extract.to_json('resources/load.json', orient='records', indent=2)

print(extract)
