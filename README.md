# Fuzzy Init
This repository contains code that I wrote to understand the fuzzywuzzy. 
Compared the different scorer and tried to figue out use cases of the library.
 
## How to run

1. Run ```pip install -r requirements.txt``` in terminal
2. Execute ```python main.py``` 

The main file has two functions 
- one that loop over all the words in the list to find the closest match
- the over uses process to extract the closest match

## Sample Input Lists
I used two lists, sample_words and reference. 
- Sample Words are the words that can contain any number of words and are supposed to be identified which word in the reference they match the closest to.

```sample words = ["date of birth", "birth_date", "birth date", "ayush suman", "date of join"]```

- Reference contains the words that are considered to be standard and are supposed to be matched against.

```reference = ["ayush", "joining date", "birth day"]```

## Output

- loop over for closest match 
```  
date of birth ayush 11
date of birth joining date 48
date of birth birth day 73
date of birth matches closest with birth day
birth_date ayush 13
birth_date joining date 36
birth_date birth day 74
birth_date matches closest with birth day
birth date ayush 13
birth date joining date 36
birth date birth day 84
birth date matches closest with birth day
ayush suman ayush 62
ayush suman joining date 26
ayush suman birth day 30
ayush suman matches closest with ayush
date of join ayush 12
date of join joining date 75
date of join birth day 19
date of join matches closest with joining date
```

- extract using process

```
date of birth matches closes with birth day 73
birth_date matches closes with birth day 74
birth date matches closes with birth day 84
ayush suman matches closes with ayush 62
date of join matches closes with joining date 75
```

## openpyxl

The code accepts two arguments as parameter, both of them excel files. Currently the code creates a new excel file with 'hello world' columns.  

