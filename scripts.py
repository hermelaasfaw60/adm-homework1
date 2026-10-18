"""HackerRank solutions for the project exercises.

"""

import textwrap
import calendar
import email.utils
from html.parser import HTMLParser
import re
import xml.etree.ElementTree as ET
import numpy as np
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from datetime import datetime


# Introduction

# 1. Say "Hello, World!" With Python
def hello_world():
    print("Hello, World!")


# 2. Python If-Else
def python_if_else(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# 3. Arithmetic Operators
def arithmetic_operators(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


# 4. Python: Division
def python_division(a, b):
    print(a // b)
    print(a / b)


# 5. Loops
def print_squares(n):
    for i in range(n):
        print(i**2)


# 6. Write a Function
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# 7. Print Function
def print_function(n):
    for i in range(1, n + 1):
        print(i, end="")


# Data Types

# 1. List Comprehensions
def list_comprehensions(x, y, z, n):
    coordinates = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(coordinates)


# 2. Find the Runner-Up Score!
def runner_up_score(scores):
    unique_scores = sorted(set(scores))
    print(unique_scores[-2])


# 3. Nested Lists
def nested_lists(records):
    grades = sorted({score for _, score in records})
    second_lowest = grades[1]
    names = sorted(name for name, score in records if score == second_lowest)

    for name in names:
        print(name)


# 4. Finding the Percentage
def finding_percentage(student_marks, query_name):
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")


# 5. Lists
def lists(commands):
    items = []

    for command_line in commands:
        command = command_line.split()

        if command[0] == "insert":
            items.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(items)
        elif command[0] == "remove":
            items.remove(int(command[1]))
        elif command[0] == "append":
            items.append(int(command[1]))
        elif command[0] == "sort":
            items.sort()
        elif command[0] == "pop":
            items.pop()
        elif command[0] == "reverse":
            items.reverse()


# 6. Tuples (legacy hash expected by the HackerRank judge)
def tuples(numbers):
    values = tuple(numbers)
    mask = (1 << 64) - 1
    result = 0x345678
    multiplier = 1000003
    remaining = len(values)
    for value in values:
        remaining -= 1
        result = ((result ^ hash(value)) * multiplier) & mask
        multiplier = (multiplier + 82520 + 2 * remaining) & mask
    result = (result + 97531) & mask
    if result >= (1 << 63):
        result -= 1 << 64
    if result == -1:
        result = -2
    print(result)


# Strings

# 1. sWAP cASE
def swap_case(s):
    return s.swapcase()


# 2. String Split and Join
def string_split_and_join(line):
    return "-".join(line.split())


# 3. What's Your Name?
def whats_your_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}! You just delved into python.")


# 4. Mutations
def mutations(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


# 5. Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


# 6. String Validators
def string_validators(s):
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# 7. Text Alignment
def text_alignment(thickness):
    c = "H"

    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    for _ in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    for _ in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    for _ in range(thickness + 1):
        print((c * thickness).center(thickness * 2) +
              (c * thickness).center(thickness * 6))

    for i in range(thickness):
        cone = ((c * (thickness - i - 1)).rjust(thickness) + c +
                (c * (thickness - i - 1)).ljust(thickness))
        print(cone.rjust(thickness * 6))


# 8. Text Wrap
def text_wrap(string, max_width):
    return textwrap.fill(string, max_width)


# 9. Designer Door Mat
def designer_door_mat(n, m):
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n - 2, 0, -2):
        print((".|." * i).center(m, "-"))


# 10. String Formatting
def print_formatted(number):
    width = len(format(number, "b"))

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            format(i, "o").rjust(width),
            format(i, "X").rjust(width),
            format(i, "b").rjust(width),
        )


# 11. Alphabet Rangoli
def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        row = "-".join(left + alphabet[size - i - 1:size])
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines + lines[-2::-1]))


# 12. Capitalize!
def capitalize_words(s):
    # word[:1].upper() changes only the first letter; str.capitalize() would
    # also lowercase the rest of the word ("hELLO" -> "Hello").
    return " ".join(word[:1].upper() + word[1:] for word in s.split(" "))


# 13. The Minion Game
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i, char in enumerate(string):
        points = length - i
        if char in "AEIOU":
            kevin_score += points
        else:
            stuart_score += points

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


# 14. Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        segment = string[i:i + k]
        seen = set()
        result = []

        for char in segment:
            if char not in seen:
                seen.add(char)
                result.append(char)

        print("".join(result))


# Sets

# 1. Introduction to Sets
def introduction_to_sets(array):
    heights = set(array)
    return sum(heights) / len(heights)


# 2. No Idea!
def no_idea(array, set_a, set_b):
    happiness = 0
    for number in array:
        if number in set_a:
            happiness += 1
        if number in set_b:
            happiness -= 1
    print(happiness)


# 3. Symmetric Difference
def symmetric_difference(set_m, set_n):
    result = sorted(set_m ^ set_n)
    print(*result, sep="\n")


# 4. Set .add()
def set_add(countries):
    stamps = set()
    for country in countries:
        stamps.add(country)
    print(len(stamps))


# 5. Set .discard(), .remove() & .pop()
def set_discard_remove_pop(values, commands):
    values = set(values)
    for command in commands:
        parts = command.split()
        if parts[0] == "pop":
            values.pop()
        elif parts[0] == "remove":
            values.remove(int(parts[1]))
        elif parts[0] == "discard":
            values.discard(int(parts[1]))
    print(sum(values))


# 6. Set .union() Operation
def set_union(english, french):
    print(len(set(english) | set(french)))


# 7. Set .intersection() Operation
def set_intersection(english, french):
    print(len(set(english) & set(french)))


# 8. Set .difference() Operation
def set_difference(english, french):
    print(len(set(english) - set(french)))


# 9. Set .symmetric_difference() Operation
def set_symmetric_difference_operation(english, french):
    print(len(set(english) ^ set(french)))


# 10. Set Mutations
def set_mutations(initial_set, operations):
    values = set(initial_set)
    for operation, other_values in operations:
        other_set = set(other_values)
        if operation == "intersection_update":
            values.intersection_update(other_set)
        elif operation == "update":
            values.update(other_set)
        elif operation == "symmetric_difference_update":
            values.symmetric_difference_update(other_set)
        elif operation == "difference_update":
            values.difference_update(other_set)
    print(sum(values))


# 11. The Captain's Room
def captains_room(group_size, room_numbers):
    unique_rooms = set(room_numbers)
    captain_room = (sum(unique_rooms) * group_size - sum(room_numbers)) // (group_size - 1)
    print(captain_room)


# 12. Check Subset
def check_subsets(test_cases):
    for set_a, set_b in test_cases:
        print(set(set_a).issubset(set(set_b)))


# 13. Check Strict Superset
def check_strict_superset(main_set, other_sets):
    main_set = set(main_set)
    print(all(main_set > set(other) for other in other_sets))


# Collections

# 1. Collections.Counter()
def collections_counter(shoe_sizes, customers):
    shoes = Counter(shoe_sizes)
    total = 0
    for size, price in customers:
        if shoes[size] > 0:
            total += price
            shoes[size] -= 1
    print(total)


# 2. DefaultDict Tutorial
def defaultdict_tutorial(group_a, group_b):
    positions = defaultdict(list)
    for i, word in enumerate(group_a, start=1):
        positions[word].append(i)
    for word in group_b:
        matches = positions[word]
        print(*matches if matches else [-1])


# 3. Collections.namedtuple()
def collections_namedtuple(fields, rows):
    Student = namedtuple("Student", fields)
    total = 0
    for row in rows:
        student = Student(*row)
        total += int(student.MARKS)
    print(f"{total / len(rows):.2f}")


# 4. Collections.OrderedDict()
def collections_ordereddict(purchases):
    items = OrderedDict()
    for name, price in purchases:
        items[name] = items.get(name, 0) + int(price)
    for name, price in items.items():
        print(name, price)


# 5. Word Order
def word_order(words):
    counts = Counter(words)
    print(len(counts))
    print(*counts.values())


# 6. Collections.deque()
def collections_deque(commands):
    values = deque()
    for command in commands:
        parts = command.split()
        if len(parts) == 2:
            getattr(values, parts[0])(int(parts[1]))
        else:
            getattr(values, parts[0])()
    print(*values)


# 7. Piling Up!
def piling_up(test_cases):
    for cube_values in test_cases:
        cubes = deque(cube_values)
        previous = float("inf")
        possible = True

        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()

            if current > previous:
                possible = False
                break
            previous = current

        print("Yes" if possible else "No")


# 8. Company Logo
def company_logo(s):
    counts = Counter(s)
    for character, frequency in sorted(
        counts.items(), key=lambda item: (-item[1], item[0])
    )[:3]:
        print(character, frequency)


# Date and Time

# 1. Calendar Module
def calendar_module(month, day, year):
    weekday = calendar.weekday(year, month, day)
    print(calendar.day_name[weekday].upper())


# 2. Time Delta
def time_delta(timestamp_pairs):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    for timestamp1, timestamp2 in timestamp_pairs:
        time1 = datetime.strptime(timestamp1, time_format)
        time2 = datetime.strptime(timestamp2, time_format)
        print(int(abs((time1 - time2).total_seconds())))


# Exceptions
def exceptions(input_pairs):
    for a, b in input_pairs:
        try:
            print(int(a) // int(b))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as error:
            print("Error Code:", error)


# Built-ins

# 1. Zipped
def zipped(student_count, subject_scores):
    subject_count = len(subject_scores)
    for student_scores in zip(*subject_scores):
        print(sum(student_scores) / subject_count)


# 2. Python Sort Sort (Athlete Sort)
def athlete_sort(rows, attribute_index):
    for row in sorted(rows, key=lambda athlete: athlete[attribute_index]):
        print(*row)


# 3. ginortS
def ginorts(value):
    def sort_key(char):
        if char.islower():
            return (0, char)
        if char.isupper():
            return (1, char)
        return (2, int(char) % 2 == 0, char)

    print("".join(sorted(value, key=sort_key)))


# Python Functionals
# 1. Map and Lambda Function
def map_and_lambda(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    cubes = list(map(lambda value: value ** 3, fibonacci[:n]))
    print(cubes)


# Regex and Parsing
# 1. Detect Floating Point Number
def detect_floating_point_numbers(values):
    pattern = re.compile(r"^[+-]?[0-9]*\.[0-9]+$")
    for value in values:
        print(bool(pattern.fullmatch(value.strip())))


# 2. Re.split()
def re_split(value):
    print("\n".join(re.split(r"[,.]", value)))


# 3. Group(), Groups() & Groupdict()
def first_repeated_alphanumeric(value):
    match = re.search(r"([A-Za-z0-9])\1", value)
    print(match.group(1) if match else -1)


# 4. Re.findall() & Re.finditer()
def regex_vowel_substrings(value):
    matches = re.findall(
        r"(?<=[b-df-hj-np-tv-z])([aeiou]{2,})(?=[b-df-hj-np-tv-z])",
        value,
        re.IGNORECASE,
    )
    print("\n".join(matches) if matches else -1)


# 5. Re.start() & Re.end()
def regex_start_end(string, substring):
    matches = list(re.finditer(r"(?=" + re.escape(substring) + r")", string))
    if matches:
        for match in matches:
            print((match.start(), match.start() + len(substring) - 1))
    else:
        print((-1, -1))


# 6. Regex Substitution
def regex_substitution(lines):
    for line in lines:
        line = re.sub(r"(?<= )&&(?= )", "and", line)
        line = re.sub(r"(?<= )\|\|(?= )", "or", line)
        print(line)


# 7. Validating Roman Numerals
def validating_roman_numerals(value):
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    print(bool(re.fullmatch(pattern, value)))


# 8. Validating phone numbers
def validating_phone_numbers(numbers):
    pattern = re.compile(r"^[789]\d{9}$")
    for number in numbers:
        print("YES" if pattern.fullmatch(number.strip()) else "NO")


# 9. Validating and Parsing Email Addresses
def validating_named_email_addresses(entries):
    pattern = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$")
    for entry in entries:
        name, address = email.utils.parseaddr(entry)
        if pattern.fullmatch(address):
            print(email.utils.formataddr((name, address)))


# 10. Detect HTML Tags, Attributes and Attribute Values
class HTMLTagAttributeParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")


def detect_html_tags_attributes(lines):
    parser = HTMLTagAttributeParser()
    parser.feed("\n".join(lines))


# 11. Hex Color Code
def hex_color_code(lines):
    inside_rule = False
    for line in lines:
        if "{" in line:
            inside_rule = True
            line = line.split("{", 1)[1]
        if inside_rule:
            if "}" in line:
                line = line.split("}", 1)[0]
                inside_rule = False
            for color in re.findall(
                r"#[A-Fa-f0-9]{6}(?![A-Fa-f0-9])|#[A-Fa-f0-9]{3}(?![A-Fa-f0-9])",
                line,
            ):
                print(color)


# 12. HTML Parser - Part 1
class HTMLPartOneParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")


def html_parser_part_one(lines):
    parser = HTMLPartOneParser()
    parser.feed("\n".join(lines))


# 13. HTML Parser - Part 2
class HTMLPartTwoParser(HTMLParser):
    def handle_comment(self, data):
        print(">>> Multi-line Comment" if "\n" in data else ">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


def html_parser_part_two(lines):
    parser = HTMLPartTwoParser()
    parser.feed("\n".join(lines))


# 14. Validating UID
def validating_uids(uids):
    for uid in uids:
        valid = (
            len(uid) == 10
            and re.fullmatch(r"[A-Za-z0-9]{10}", uid) is not None
            and len(set(uid)) == 10
            and sum(char.isupper() for char in uid) >= 2
            and sum(char.isdigit() for char in uid) >= 3
        )
        print("Valid" if valid else "Invalid")


# 15. Validating Credit Card Numbers
def validating_credit_cards(cards):
    pattern = re.compile(r"^(?:[456][0-9]{15}|[456][0-9]{3}(?:-[0-9]{4}){3})$")
    for card in cards:
        digits = card.replace("-", "")
        valid = (
            pattern.fullmatch(card) is not None
            and re.search(r"(\d)\1{3,}", digits) is None
        )
        print("Valid" if valid else "Invalid")


# 16. Validating Postal Codes
def validating_postal_codes(codes):
    integer_in_range = re.compile(r"^[1-9]\d{5}$")
    alternating_pair = re.compile(r"(\d)(?=\d\1)")
    for code in codes:
        valid = (
            integer_in_range.fullmatch(code) is not None
            and len(alternating_pair.findall(code)) < 2
        )
        print(valid)


# 17. Matrix Script
def matrix_script(rows):
    decoded = "".join(
        rows[row][column]
        for column in range(len(rows[0]))
        for row in range(len(rows))
    )
    print(re.sub(r"(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])", " ", decoded))


# XML
# 1. XML 1 - Find the Score
def xml_attribute_score(xml_text):
    root = ET.fromstring(xml_text)

    def score(node):
        return len(node.attrib) + sum(score(child) for child in node)

    return score(root)


# 2. XML2 - Find the Maximum Depth
def xml_maximum_depth(xml_text):
    root = ET.fromstring(xml_text)

    def depth(node):
        return 1 + max((depth(child) for child in node), default=0)

    return depth(root) - 1


# Closures and Decorators

# 1. Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(numbers):
        f(["+91 " + number[-10:-5] + " " + number[-5:]
           for number in sorted(numbers, key=lambda item: item[-10:])])
    return fun


@wrapper
def sort_phone(numbers):
    print(*numbers, sep="\n")


# 2. Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda person: int(person[2]))]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


# NumPy

# 1. NumPy Arrays
def numpy_arrays(values):
    return np.array(values, dtype=float)[::-1]


# 2. NumPy Shape and Reshape
def numpy_shape_reshape(values):
    return np.array(values, dtype=int).reshape(3, 3)


# 3. NumPy Transpose and Flatten
def numpy_transpose_and_flatten(rows):
    array = np.array(rows, dtype=int)
    print(array.T)
    print(array.flatten())


# 4. NumPy Concatenate
def numpy_concatenate(first, second):
    print(np.concatenate((np.array(first, dtype=int), np.array(second, dtype=int)), axis=0))


# 5. NumPy Zeros and Ones
def numpy_zeros_and_ones(shape):
    print(np.zeros(shape, dtype=int))
    print(np.ones(shape, dtype=int))


# 6. NumPy Eye and Identity
def numpy_eye(rows, columns):
    with np.printoptions(legacy="1.13"):
        print(np.eye(rows, columns))


# 7. NumPy Array Mathematics
def numpy_array_mathematics(first, second):
    a = np.array(first, dtype=int)
    b = np.array(second, dtype=int)
    for operation in (np.add, np.subtract, np.multiply, np.floor_divide, np.mod, np.power):
        print(operation(a, b))


# 8. NumPy Floor, Ceil and Rint
def numpy_floor_ceil_rint(values):
    array = np.array(values, dtype=float)
    with np.printoptions(legacy="1.13"):
        print(np.floor(array))
        print(np.ceil(array))
        print(np.rint(array))


# 9. NumPy Sum and Prod
def numpy_sum_and_prod(rows):
    array = np.array(rows, dtype=int)
    print(np.prod(np.sum(array, axis=0)))


# 10. NumPy Min and Max
def numpy_min_max(rows):
    array = np.array(rows, dtype=int)
    print(np.max(np.min(array, axis=1)))


# 11. NumPy Mean, Var, and Std
def numpy_mean_var_std(rows):
    array = np.array(rows, dtype=int)
    print(np.mean(array, axis=1))
    print(np.var(array, axis=0))
    print(np.round(np.std(array), 11))


# 12. NumPy Dot and Cross
def numpy_dot_and_cross(first, second):
    a = np.array(first, dtype=int)
    b = np.array(second, dtype=int)
    print(np.dot(a, b))


# 13. NumPy Inner and Outer
def numpy_inner_and_outer(first, second):
    a = np.array(first, dtype=int)
    b = np.array(second, dtype=int)
    print(np.inner(a, b))
    print(np.outer(a, b))


# 14. NumPy Polynomials
def numpy_polynomials(coefficients, x):
    print(np.polyval(np.array(coefficients, dtype=float), x))


# 15. NumPy Linear Algebra
def numpy_linear_algebra(rows):
    array = np.array(rows, dtype=float)
    print(round(np.linalg.det(array), 2))


# Problem 2 - Algorithms (Problem Solving)

# 1. Birthday Cake Candles
def birthday_cake_candles(candles):
    return candles.count(max(candles))


# 2. Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    distance = x2 - x1
    speed = v1 - v2
    if speed == 0:
        return "YES" if distance == 0 else "NO"
    return "YES" if distance % speed == 0 and distance // speed >= 0 else "NO"


# 3. Viral Advertising
def viral_advertising(days):
    shared = 5
    cumulative_likes = 0
    for _ in range(days):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
    return cumulative_likes


# 4. Recursive Digit Sum
def recursive_digit_sum(n, k):
    value = sum(map(int, n)) * k
    while value >= 10:
        value = sum(map(int, str(value)))
    return value


# 5. Insertion Sort - Part 1
def insertion_sort_part_1(values):
    arr = list(values)
    value = arr[-1]
    i = len(arr) - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = value
    print(*arr)


# 6. Insertion Sort - Part 2
def insertion_sort_part_2(values):
    arr = list(values)
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
        print(*arr)
