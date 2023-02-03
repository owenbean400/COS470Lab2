import os
import re

# Extract the calendar date from a file
# Extract <Month Name> <Day>
# Extract <Day> <Month Name>
# Extract <Month Name> <Year>
# Extract <Year> <Month Name>
def extract_temporal_expressions(file):
    with open(file, "r") as f:
        text = f.read()

    monthNamesList = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                   'november', 'december']

    pattern1Month = []
    pattern2Month = []
    pattern3Month = []
    pattern4Month = []

    for month in monthNamesList:
        pattern1Month.append(month + "\s\d{1,2}")
        pattern2Month.append("\d{1,2}\s" + month)
        pattern3Month.append(month + "\s\d\d\d\d")
        pattern4Month.append("\d\d\d\d\s" + month)

    month_name_re = "|".join(pattern1Month + pattern2Month + pattern3Month + pattern4Month)

    pattern = re.compile(f"(?i){month_name_re}")
    matches2 = re.findall(pattern, text)

    return matches2


def replaceMonthName(pattMatches):
    # Function that takes in a list of temporal pattern matches
    # returned from the above function. Iterates through the list
    # looking for substring matches for Month string values. Given the
    # format we need to normalize to, when a month name is matched
    # to we take the numeric equivalent and append it to the
    # beginning of the string.
    #
    # pattMatches : List -> list of temporal regex matches
    # patternMatches : List -> resulting list of matches with month string
    #                 value replaced by numeric value

    paternMatches = []

    for match in pattMatches:
        match = match.lower()
        if match.find("january") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "01/" + str(res[0])
            else:
                fixedMatch = "01/" + str(res[1])
        elif match.find("february") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "02/" + str(res[0])
            else:
                fixedMatch = "02/" + str(res[1])
        elif match.find("march") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "03/" + str(res[0])
            else:
                fixedMatch = "03/" + str(res[1])
        elif match.find("april") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "04/" + str(res[0])
            else:
                fixedMatch = "04/" + str(res[1])
        elif match.find("may") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "05/" + str(res[0])
            else:
                fixedMatch = "05/" + str(res[1])
        elif match.find("june") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "06/" + str(res[0])
            else:
                fixedMatch = "06/" + str(res[1])
        elif match.find("july") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "07/" + str(res[0])
            else:
                fixedMatch = "07/" + str(res[1])
        elif match.find("august") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "08/" + str(res[0])
            else:
                fixedMatch = "08/" + str(res[1])
        elif match.find("september") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "09/" + str(res[0])
            else:
                fixedMatch = "09/" + str(res[1])
        elif match.find("october") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "10/" + str(res[0])
            else:
                fixedMatch = "10/" + str(res[1])
        elif match.find("november") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "11/" + str(res[0])
            else:
                fixedMatch = "11/" + str(res[1])
        elif match.find("december") != -1:
            res = match.split()
            if res[0].isdigit():
                fixedMatch = "12/" + str(res[0])
            else:
                fixedMatch = "12/" + str(res[1])
        else:
            fixedMatch = match

        paternMatches.append(fixedMatch)

    return paternMatches


def padWithZeros(data):
    # Function to take into account that not all of our day values
    # found within the documents are not of length 2. At this point
    # we know that we no longer have character values within the
    # date strings, so we check each item in the list -2 index. If we
    # find a "/" we know that we have a day value with only one number.
    # In that case we then append a 0 before the number following the
    # "/" and append it to the result list. If we find a number instead
    # of the "/" we just append the item to the result list.
    #
    # data : list -> list of either numeric date and month strings or
    #         date and year strings
    # paddedOutput : list -> result list where any string that had a
    #         date value of length 1 has been padded with a zero,
    #         otherwise the original list value is just appended to the
    #         result list

    paddedOutput = []
    padded = ''

    for i in data:
        if i[-2] == '/':
            i = i.replace('/', ' ')
            i = i.split()
            padded = str(i[0]) + '/0' + str(i[1])
        else:
            padded = i
        paddedOutput.append(padded)

    return paddedOutput


def normalize(data):
    # Function to take a list of numeric date string values of
    # either month/day or month/year. By checking the -3 index
    # we can tell which type it is by whether it finds a digit or
    # not. It will replace any "/" with " " and then use pythons
    # split() method to create a sublist of the orginal list item.
    # If it found a digit at the -3 index we append "/xx/" inbetween
    # the two substrings. Otherwise we append "/xxxx" to the end of
    # the original string. Then append the normalized string to the
    # result list.
    #
    # data : list -> list of numeric date string values of either
    #        month/day or month/year
    # normalizedData : list -> result list of all returned strings of
    #        the format 'dd/xx/dddd' or 'dd/dd/xxxx'

    normalizedData = []
    normal = ''
    for item in data:
        if item[-3].isdigit():
            item = item.replace('/', ' ')
            item = item.split()
            normal = str(item[0]) + '/xx/' + str(item[1])
        else:
            item = item.replace('/', ' ')
            item = item.split()
            normal = str(item[0]) + '/' + str(item[1]) + '/xxxx'
        normalizedData.append(normal)
    return normalizedData

# Looks through all of the files and uses extract the temporal expressions
def search_directory(directory):
    for subdir, dirs, files in os.walk(directory):
        for sdir in dirs:
            if sdir == "input_docs":
                input_dir = os.path.join(subdir, sdir)
                for subdir, dirs, files in os.walk(input_dir):
                    for file in files:
                        if file.endswith(".txt"):
                            file_path = os.path.join(subdir, file)
                            temporal_expressions = extract_temporal_expressions(file_path)
                            temporal_without_month_name = replaceMonthName(temporal_expressions)
                            padded = padWithZeros(temporal_without_month_name)
                            normalized = normalize(padded)
                            if normalized:
                                print(f"{file_path}: {normalized}")



search_directory("txt")