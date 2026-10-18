# Algorithmic Methods of Data Mining - Homework 1
# Combined HackerRank solutions
# Each original solution is separated below by its source path.


# ============================================================================
# Solution: Problem1/CH1/arithmetic_operators.py
# ============================================================================

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# ============================================================================
# Solution: Problem1/CH1/division.py
# ============================================================================

# Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# ============================================================================
# Solution: Problem1/CH1/hello_world.py
# ============================================================================

if __name__ == '__main__':
    print("Hello, World!")


# ============================================================================
# Solution: Problem1/CH1/loops.py
# ============================================================================

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i**2)

# ============================================================================
# Solution: Problem1/CH1/print_function.py
# ============================================================================

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")

# ============================================================================
# Solution: Problem1/CH1/python_if_else.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# ============================================================================
# Solution: Problem1/CH1/write_a_function.py
# ============================================================================

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    else:
        if year % 100 == 0:
            leap = False
        else:
            if year % 4 == 0:
                leap = True
            else:
                leap = False
    return leap

year = int(input())
print(is_leap(year))

# ============================================================================
# Solution: Problem1/CH10/HTML_parser_p1.py
# ============================================================================

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"{'Start':<6}: {tag}")
        if attrs:
            for attr in attrs:
                print("->",attr[0],">",attr[1])

    def handle_endtag(self, tag):
        print(f"{'End':<6}: {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"{'Empty':<6}: {tag}")
        if attrs:
            for attr in attrs:
                print("->",attr[0],">",attr[1])


parser = MyHTMLParser()

n = int(input())

for _ in range(n):
    parser.feed(input())

# ============================================================================
# Solution: Problem1/CH10/HTML_parser_p2.py
# ============================================================================

from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if re.search(r'\n', data):
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


if __name__ == '__main__':
    n = int(input())

    html = ''
    for _ in range(n):
        html += input() + '\n'

    parser = MyHTMLParser()
    parser.feed(html)

# ============================================================================
# Solution: Problem1/CH10/detect_floating_point_number.py
# ============================================================================

import re
T = int(input())

for _ in range(T):
    S = input()

    try:
        #if the string contains exactly one decimal point
        if bool(re.fullmatch(r"[^.]*\.[^.]*", S)):
        # Check if there is at least one digit after the decimal point
            if bool(re.search(r"\.\d+", S)):
        # Check if the format is valid (+, -, digits, decimal point)
                if bool(re.fullmatch(r"^[+-]?\d*(\.\d+)?$", S)):
                    print("True")
                else:
                    print("False")
            else:
                print("False")
        else:
            print("False")

    except ValueError:
        print("False")


# ============================================================================
# Solution: Problem1/CH10/detect_html_tags_attrs.py
# ============================================================================

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->",attr[0],">",attr[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->",attr[0],">",attr[1])


if __name__ == '__main__':
    n = int(input())

    html = ''
    for _ in range(n):
        html += input() + '\n'

    parser = MyHTMLParser()
    parser.feed(html)

# ============================================================================
# Solution: Problem1/CH10/findall_finditer.py
# ============================================================================

import re

S = input()

regex_pattern = r"(?i)(?<=[qwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnm])"

matches = re.findall(regex_pattern, S)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)

# ============================================================================
# Solution: Problem1/CH10/groups.py
# ============================================================================

import re

S = input()

regex_pattern = r"([a-zA-Z0-9])\1"

match = re.search(regex_pattern, S)
if match:
    print(match.group(1))
else:
    print(-1)

# ============================================================================
# Solution: Problem1/CH10/hex_color_code.py
# ============================================================================

import re

def extract_hex_colors(line):
    regex_pattern = r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?!\w)"
    return re.findall(regex_pattern, line)

n = int(input())

inside_block = False

for _ in range(n):
    line = input()

    for part in re.split(r"([{}])", line):
        if part == "{":
            inside_block = True

        elif part == "}":
            inside_block = False

        elif inside_block:
            colors = extract_hex_colors(part)

            for color in colors:
                print(color)

# ============================================================================
# Solution: Problem1/CH10/matrix_script.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''.join(char for column in zip(*matrix) for char in column)
result=re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded)
print(result)

# ============================================================================
# Solution: Problem1/CH10/re_split.py
# ============================================================================

regex_pattern = r"[.,]"

import re
print("\n".join(re.split(regex_pattern, input())))

# ============================================================================
# Solution: Problem1/CH10/re_start_end.py
# ============================================================================

import re

S = input()
K = input()

regex_pattern = r'(?={})'.format(re.escape(K))
matches = list(re.finditer(regex_pattern, S))
found = False

for match in matches:
    found = True
    start = match.start()
    end = match.start() + len(K) - 1
    print((start, end))

if not found:
    print((-1, -1))

# ============================================================================
# Solution: Problem1/CH10/regex_sub.py
# ============================================================================

import re

def replace(match):
    if match.group(0)=='&&':
        return "and"
    else:
        return "or"

n = int(input())

for _ in range(n):
    line = input()
    result = re.sub(r'(?<= )(&&|\|\|)(?= )', replace, line)
    print(result)

# ============================================================================
# Solution: Problem1/CH10/roman_numerals.py
# ============================================================================

regex_pattern = r"^(?=.)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# ============================================================================
# Solution: Problem1/CH10/validating_UID.py
# ============================================================================

import re

def validate_uid(uid):
    if len(uid)==10:
        if uid.isalnum():
            if len(re.findall(r'[A-Z]', uid)) >= 2:
                if len(re.findall(r'[0-9]', uid)) >= 3:
                    if len(uid)==len(set(uid)):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        uid = input().strip()

        if validate_uid(uid):
            print("Valid")
        else:
            print("Invalid")

# ============================================================================
# Solution: Problem1/CH10/validating_card_number.py
# ============================================================================

import re

def validate_card(card):
        if re.fullmatch(r'([0-9]{16}|[0-9]{4}(-[0-9]{4}){3})', card):
            if re.fullmatch(r'[4-6].*', card):
                if re.search(r'([0-9])\1{3,}', card.replace('-', '')):
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        card = input().strip()

        if validate_card(card):
            print("Valid")
        else:
            print("Invalid")

# ============================================================================
# Solution: Problem1/CH10/validating_email.py
# ============================================================================

import re
import email.utils

def is_valid_email(email_address):
    regex_pattern = r"[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}" 
    return bool(re.fullmatch(regex_pattern, email_address))

n = int(input())

for _ in range(n):
    line = input()

    # Extract the name and email address
    name, email_address = email.utils.parseaddr(line)

    # Validate the email address
    if is_valid_email(email_address):
        print(email.utils.formataddr((name, email_address)))

# ============================================================================
# Solution: Problem1/CH10/validating_phone_number.py
# ============================================================================

import re

def is_valid_mobile(number):
    regex_pattern = r"([789])([0-9]{9})"  # Write your regex here
    return bool(re.fullmatch(regex_pattern, number))

n = int(input())

for _ in range(n):
    number = input()
    
    if is_valid_mobile(number):
        print("YES")
    else:
        print("NO")

# ============================================================================
# Solution: Problem1/CH10/validating_postal_code.py
# ============================================================================

regex_integer_in_range = r'^[1-9][0-9]{5}$'	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(?=([0-9])[0-9]\1)'	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# ============================================================================
# Solution: Problem1/CH11/XML_find_max_depth.py
# ============================================================================

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child,level)
    pass
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# ============================================================================
# Solution: Problem1/CH11/XML_find_score.py
# ============================================================================

import xml.etree.ElementTree as etree

def get_attr_number(node):
    attrbs=0
    attrbs+=len(node.attrib)
    for child in node:
        attrbs+=get_attr_number(child)
    return attrbs
if __name__ == '__main__':  
    n = int(input())
    xml = '\n'.join(input() for _ in range(n))
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# ============================================================================
# Solution: Problem1/CH12/name_dir.py
# ============================================================================

import operator

def person_lister(f):
    def inner(people):
        sorted_people = sorted(people, key=lambda person: int(person[2]))
        return [f(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# ============================================================================
# Solution: Problem1/CH12/std_phone_number_decorator.py
# ============================================================================

def wrapper(f):
    def fun(l):
        numbers = [number[-10:] for number in l]
        formatted = [f"+91 {number[:5]} {number[5:]}" for number in numbers]
        return f(formatted)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# ============================================================================
# Solution: Problem1/CH13/array_maths.py
# ============================================================================

import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

# ============================================================================
# Solution: Problem1/CH13/arrays.py
# ============================================================================

import numpy

def arrays(arr):
    nparr=numpy.array(arr, float)
    return numpy.flip(nparr)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# ============================================================================
# Solution: Problem1/CH13/concat.py
# ============================================================================

import numpy as np

n, m, p = map(int, input().split())

array_1 = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

array_2 = np.array(
    [input().split() for _ in range(m)],
    dtype=int
)

print(np.concatenate((array_1, array_2)))

# ============================================================================
# Solution: Problem1/CH13/dot.py
# ============================================================================

import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.dot(a, b))

# ============================================================================
# Solution: Problem1/CH13/eye_identity.py
# ============================================================================

import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m))

# ============================================================================
# Solution: Problem1/CH13/floor_ceil.py
# ============================================================================

import numpy as np

np.set_printoptions(legacy='1.13')

a = np.array(input().split(), float)

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

# ============================================================================
# Solution: Problem1/CH13/inner_outer.py
# ============================================================================

import numpy as np

a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.inner(a, b))
print(np.outer(a, b))

# ============================================================================
# Solution: Problem1/CH13/linear_algebra.py
# ============================================================================

import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(a), 2))

# ============================================================================
# Solution: Problem1/CH13/mean_var_std.py
# ============================================================================

import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)

print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(round(np.std(a), 11))

# ============================================================================
# Solution: Problem1/CH13/min_and_max.py
# ============================================================================

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(a, axis=1)))

# ============================================================================
# Solution: Problem1/CH13/poly.py
# ============================================================================

import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

print(np.polyval(coefficients, x))

# ============================================================================
# Solution: Problem1/CH13/shape_reshape.py
# ============================================================================

import numpy as np

numbers = np.array(input().split(), dtype=int)

print(numbers.reshape(3, 3))

# ============================================================================
# Solution: Problem1/CH13/sum_and_prod.py
# ============================================================================

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.prod(np.sum(a, axis=0)))

# ============================================================================
# Solution: Problem1/CH13/transpose_flatten.py
# ============================================================================

import numpy as np

n, m = map(int, input().split())

matrix = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)
print(np.transpose(matrix))
print(matrix.flatten())

# ============================================================================
# Solution: Problem1/CH13/zeros_ones.py
# ============================================================================

import numpy as np

shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))

# ============================================================================
# Solution: Problem1/CH2/find_runner_up_score.py
# ============================================================================

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))
    unique_scores.sort()
    runner_up_score = unique_scores[-2]
    print(runner_up_score)

# ============================================================================
# Solution: Problem1/CH2/finding_percentage.py
# ============================================================================

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    queried_scores = student_marks[query_name]
    queried_mean = sum(queried_scores) / len(queried_scores)
    print(f"{queried_mean:.2f}")

# ============================================================================
# Solution: Problem1/CH2/list_comprehensions.py
# ============================================================================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result=[]
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i + j + k != n:
                    result.append([i, j, k])
    print(result)

# ============================================================================
# Solution: Problem1/CH2/nested_lists.py
# ============================================================================

if __name__ == '__main__':
    records = []
    scores =set()
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)
    second_worst_score = sorted(scores)[1]
    for record in records:
        if record[1] == second_worst_score:
            names.append(record[0])
    names.sort()
    for name in names:
        print(name)

# ============================================================================
# Solution: Problem1/CH2/tuples.py
# ============================================================================

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    the_tuple = tuple(integer_list)
    print(hash(the_tuple))

# ============================================================================
# Solution: Problem1/CH3/alphabet_rangoli.py
# ============================================================================

def print_rangoli(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    width = 4 * n - 3
    lines = []

    for i in range(n):
        left = alphabet[n - 1:i:-1]
        right = alphabet[i:n]
        row = '-'.join(left + right)
        lines.append(row.center(width, '-'))

    for line in reversed(lines):
        print(line)

    for line in lines[1:]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# ============================================================================
# Solution: Problem1/CH3/capitalize.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ============================================================================
# Solution: Problem1/CH3/desinger_door_mat.py
# ============================================================================

N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N - 2, 0, -2):
    print(('.|.' * i).center(M, '-'))

# ============================================================================
# Solution: Problem1/CH3/merge_tools.py
# ============================================================================

def merge_the_tools(string, k):
     subs = [string[i:i+k] for i in range(0, len(string), k)]
     for s in subs:
        print(''.join(dict.fromkeys(s)))        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# ============================================================================
# Solution: Problem1/CH3/minion_game.py
# ============================================================================

def minion_game(string):
  
    v_score = 0
    c_score = 0
    vowels = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] in vowels:
            v_score += len(string) - i
        else:
            c_score += len(string) - i
    if v_score > c_score:
        print("Kevin", v_score)
    elif c_score > v_score:
        print("Stuart", c_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# ============================================================================
# Solution: Problem1/CH3/number_formatting.py
# ============================================================================

def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# ============================================================================
# Solution: Problem1/CH3/string_validators.py
# ============================================================================

print("1".isupper())

# ============================================================================
# Solution: Problem1/CH3/text_alignment.py
# ============================================================================

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# ============================================================================
# Solution: Problem1/CH4/captain_room.py
# ============================================================================

k = int(input())
rooms = list(map(int, input().split()))

captain = (k * sum(set(rooms)) - sum(rooms)) // (k - 1)
print(captain)

# ============================================================================
# Solution: Problem1/CH4/check_subset.py
# ============================================================================

T = int(input())

for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    if len(A.difference(B))==0:
        print("True")
    else:
        print("False")

# ============================================================================
# Solution: Problem1/CH4/introduction_to_sets.py
# ============================================================================

def average(array,n):
    distinct_heights=set(array)
    return sum(distinct_heights)/len(distinct_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr,n)
    print(result)

# ============================================================================
# Solution: Problem1/CH4/no_idea.py
# ============================================================================

n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for num in arr:
    if num in A:
        happiness+=1
    elif num in B:
        happiness-=1

print(happiness)

# ============================================================================
# Solution: Problem1/CH4/set_add.py
# ============================================================================

n = int(input())
countries=set()
for _ in range(n):
    country = input()
    countries.add(country)
print(len(countries))

# ============================================================================
# Solution: Problem1/CH4/set_difference.py
# ============================================================================

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))
eng_diff=english.difference(french)
print(len(eng_diff))

# ============================================================================
# Solution: Problem1/CH4/set_discard_remove_pop.py
# ============================================================================

def operation(s, command):
    if command.startswith('pop'):
        s.pop()
    elif command.startswith('remove'):
        number_to_remove=int(command.split(" ")[1])
        s.remove(number_to_remove)
    elif command.startswith('discard'):
        number_to_discard=int(command.split(" ")[1])
        s.discard(number_to_discard)
    return s
        

n = int(input())
s = set(map(int, input().split()))
num_of_commands=int(input())
for _ in range(num_of_commands):
    command=input()
    operation(s, command)

print(sum(s))

# ============================================================================
# Solution: Problem1/CH4/set_intersection.py
# ============================================================================

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))
intersect=english.intersection(french)
print(len(intersect))

# ============================================================================
# Solution: Problem1/CH4/set_mutations.py
# ============================================================================

def operation(s, command,other_set):
    if command=='intersection_update':
        s.intersection_update(other_set)
    elif command=='update':
        s.update(other_set)
    elif command=='symmetric_difference_update':
        s.symmetric_difference_update(other_set)
    elif command=='difference_update':
        s.difference_update(other_set)
    return s

n = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command, length = input().split()
    other_set = set(map(int, input().split()))
    operation(A, command,other_set)
print(sum(A))

# ============================================================================
# Solution: Problem1/CH4/set_sym_diff.py
# ============================================================================

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))
eng_diff=english.difference(french)
fr_diff=french.difference(english)
print(len(eng_diff)+len(fr_diff))

# ============================================================================
# Solution: Problem1/CH4/set_union.py
# ============================================================================

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))
union=english.union(french)
print(len(union))

# ============================================================================
# Solution: Problem1/CH4/strict_super_set.py
# ============================================================================

A = set(map(int, input().split()))

n = int(input())
final_res=True

for _ in range(n):
    B = set(map(int, input().split()))
    if len(B.difference(A))==0 and len(A.difference(B))!=0:
        final_res=True and final_res
    else:
        final_res=False and final_res
print(final_res)

# ============================================================================
# Solution: Problem1/CH4/symmetric_difference.py
# ============================================================================

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

a_b_b_a=list((b.difference(a)).union(a.difference(b)))
a_b_b_a.sort()
for i in a_b_b_a:
    print(i)

# ============================================================================
# Solution: Problem1/CH5/collections_counter.py
# ============================================================================

from collections import Counter

n = int(input())
shoes = list(map(int, input().split()))
shoe_counter=Counter(shoes)

customers = int(input())

total_earned = 0

for _ in range(customers):
    size, price = map(int, input().split())
    size_num=shoe_counter[size]
    if size_num>0:
        total_earned+=price
        shoe_counter[size]-=1
    else:
        continue
print(total_earned)

# ============================================================================
# Solution: Problem1/CH5/company_logo.py
# ============================================================================

from collections import Counter

s = input()
char_counts = Counter(s)
result = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))

for char, count in result[:3]:
    print(char, count)

# ============================================================================
# Solution: Problem1/CH5/default_dict.py
# ============================================================================

from collections import defaultdict

n, m = map(int, input().split())

group_a = []
group_b = []
positions=defaultdict(list)

for i in range(1, n+1):
    word = input()
    group_a.append(word)
    positions[word].append(i)

for _ in range(m):
    word = input()
    if word in positions:
        print(*positions[word])
    else:
        print(-1)


# ============================================================================
# Solution: Problem1/CH5/deque.py
# ============================================================================

from collections import deque

def operation(d, command):
    if command.startswith('popleft'):
        d.popleft()
    elif command.startswith('pop'):
        d.pop()
    elif command.startswith('appendleft'):
        num_to_append=int(command.split(" ")[1])
        d.appendleft(num_to_append)
    elif command.startswith('append'):
        num_to_append=int(command.split(" ")[1])
        d.append(num_to_append)
    return d

n = int(input())
d = deque()

for _ in range(n):
    command = input()
    operation(d, command)
print(' '.join(map(str, d)))

# ============================================================================
# Solution: Problem1/CH5/named_tuple.py
# ============================================================================

from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total_marks = 0

for _ in range(n):
    student = Student(*input().split())
    total_marks+=int(student.MARKS)
print(f"{total_marks/n:.2f}")

# ============================================================================
# Solution: Problem1/CH5/ordered_dict.py
# ============================================================================

from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    *name, price = input().split()
    item_name = " ".join(name)
    price = int(price)
    if item_name in items:
        items[item_name]+=price
    else:
        items[item_name]=price

for item_name, net_price in items.items():
    print(item_name, net_price)

# ============================================================================
# Solution: Problem1/CH5/piling_up.py
# ============================================================================

from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    possible = True
    top = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()

        if cube > top:
            possible = False
            break

        top = cube

    print("Yes" if possible else "No")

# ============================================================================
# Solution: Problem1/CH5/word_order.py
# ============================================================================

from collections import OrderedDict

n = int(input())

words = OrderedDict()

for _ in range(n):
    word = input()
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(len(words.keys()))
print(' '.join(map(str, words.values())))


# ============================================================================
# Solution: Problem1/CH6/calendar_module.py
# ============================================================================

import calendar

month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())

# ============================================================================
# Solution: Problem1/CH6/time_delta.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
import calendar


# Complete the time_delta function below.
def time_delta(t1, t2):
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    seconds1 = calendar.timegm(date1.utctimetuple())
    seconds2 = calendar.timegm(date2.utctimetuple())
    return str(abs(seconds1 - seconds2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# ============================================================================
# Solution: Problem1/CH7/exceptions.py
# ============================================================================

T = int(input())

for _ in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# ============================================================================
# Solution: Problem1/CH8/athlete_sort.py
# ============================================================================

from collections import OrderedDict

N, M = map(int, input().split())

athletes = OrderedDict()

for i in range(N):
    row = list(map(int, input().split()))
    athletes[i]=row

K = int(input())
sorted_athletes=sorted(athletes.items(), key=lambda x: x[1][K])

for athlete in sorted_athletes:
    print(' '.join(map(str, athlete[1])))

# ============================================================================
# Solution: Problem1/CH8/ginortS.py
# ============================================================================

S = input()

lowercase = []
uppercase = []
odd_digits = []
even_digits = []

for char in S:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    elif char.isdigit():
        if int(char)%2==0:
            even_digits.append(char)
        else:
            odd_digits.append(char)

lowercase.sort()
uppercase.sort()
even_digits.sort()
odd_digits.sort()
result = ''.join(lowercase+uppercase+odd_digits+even_digits)

print(result)

# ============================================================================
# Solution: Problem1/CH8/zipped.py
# ============================================================================

N, X = map(int, input().split())

marks = []
for i in range(X):
    marks.append(list(map(float, input().split())))

students = zip(*marks)

for student in students:
    avg=sum(student)/X
    print(f"{avg:.1f}")

# ============================================================================
# Solution: Problem1/CH9/map_lambda.py
# ============================================================================

cube = lambda x: x**3

def fibonacci(n):
    first=0
    second=1
    if n==0:
        return [0]
    elif n==1:
        return [0, 1]
    else:
        fib=[0, 1]
        for i in range(2, n):
            fib.append(fib[-1]+fib[-2])
        return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# ============================================================================
# Solution: Problem2/birthday_candles.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# ============================================================================
# Solution: Problem2/insertion_sort1.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# ============================================================================
# Solution: Problem2/insertion_sort2.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# ============================================================================
# Solution: Problem2/kangroo.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1==x2:
            return "YES"
        else:
            return"NO"
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# ============================================================================
# Solution: Problem2/strange_advertising.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    total_likes = 0

    for _ in range(n):
        liked = shared // 2
        total_likes += liked
        shared = liked * 3

    return total_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# ============================================================================
# Solution: Problem2/super_digit.py
# ============================================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if n < 10:
        return n
    return superDigit(sum(int(d) for d in str(n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# ============================================================================
# Solution: challenge1.py
# ============================================================================

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
