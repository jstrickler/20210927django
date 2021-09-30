file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        pass
except FileNotFoundError as err:
    print(err)
    # log, retry, etc here

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

index = 99
try:
    print(fruits[index])
except (KeyError, IndexError) as err:
    print(err)
except Exception as err:
    print(err)

factor = 22
values = 19, 0, 2.3, 8, 14

for v in values:
    try:
        result = factor / v
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)  # if no exceptions

import sqlite3

conn = None
database = "wombats.db"
try:
    conn = sqlite3.connect(database)
except sqlite3.Error as err:
    print(err)
    print("Exiting...")
    exit(1)  # exit program
else:
    cursor = conn.cursor()
    # do queries, inserts, updates, etc ...
    cursor.close()
finally:
    if conn:
        conn.close()


