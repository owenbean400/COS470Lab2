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
                            print(f"{file_path}: {temporal_expressions}")


search_directory("txt")