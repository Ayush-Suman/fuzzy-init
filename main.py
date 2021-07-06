from fuzzywuzzy import process, fuzz

sample_words = ["date of birth", "birth_date", "birth date", "ayush suman", "date of join"]
reference = ["ayush", "joining date", "birth day"]


# Input Arrays :
# sample words : ["date of birth", "birth_date", "birth date", "ayush suman", "date of join"]
# reference words or the words that are considered to be standard : ["ayush", "joining date", "birth day"]

# algorithm to identify closest match
def loop_over_for_max_score():
    for i in sample_words:
        max_score = 0
        closest_match = ""
        for j in reference:
            score = fuzz.token_sort_ratio(i, j)
            print(i, j, score)
            if max_score < score:
                max_score = score
                closest_match = j
        print(i, "matches closest with", closest_match)


# Output :
# date of birth ayush 11
# date of birth joining date 48
# date of birth birth day 73
# date of birth matches closest with birth day
# birth_date ayush 13
# birth_date joining date 36
# birth_date birth day 74
# birth_date matches closest with birth day
# birth date ayush 13
# birth date joining date 36
# birth date birth day 84
# birth date matches closest with birth day
# ayush suman ayush 62
# ayush suman joining date 26
# ayush suman birth day 30
# ayush suman matches closest with ayush
# date of join ayush 12
# date of join joining date 75
# date of join birth day 19
# date of join matches closest with joining date


# algorithm using process extractOne
def extract_using_process():
    for i in sample_words:
        closest_match = process.extractOne(i, reference, scorer=fuzz.token_sort_ratio, score_cutoff=50)
        print(i, "matches closes with", closest_match.__getitem__(0), closest_match.__getitem__(1))


# Output:
# date of birth matches closes with birth day 73
# birth_date matches closes with birth day 74
# birth date matches closes with birth day 84
# ayush suman matches closes with ayush 62
# date of join matches closes with joining date 75

if __name__ == "__main__":
    extract_using_process()
    # loop_over_for_max_score()
