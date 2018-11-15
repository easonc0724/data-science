# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 6.5.0 -- An enhanced Interactive Python.
C:\Users\Eason\Anaconda3\lib\site-packages\ipykernel\parentpoller.py:116: UserWarning: Parent poll failed.  If the frontend dies,
                the kernel may be left running.  Please let us know
                about your system (bitness, Python, etc.) at
                ipython-dev@scipy.org
  ipython-dev@scipy.org""")

my_int = 87
my_float = 8.7
my_complex = 8 + 7j
my_bool = True
my_str = "Introduction to Python Data Science"
type(87)
type(8.7)
type(8 + 7j)
type(True)
type(False)
type("Introduction to Python Data Science")

Out[1]: str

print 42.195 * 0.62137
  File "<ipython-input-2-3bea2c6b1da6>", line 1
    print 42.195 * 0.62137
               ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(42.195 * 0.62137)?




print(42.195 * 0.62137)
26.21870715

my_height =169
print my_height
  File "<ipython-input-4-b5b7ae73f1a4>", line 2
    print my_height
                  ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(my_height)?




my_weight = 52
print my_weight
  File "<ipython-input-5-780163f22c66>", line 2
    print my_weight
                  ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(my_weight)?




my_height = 169
my_weight = 52
bmi = 52/ (169/ 100)**2



genre = "SitCom"
seasons = 10
episodes = 236
stars = ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow",
"Matt LeBlanc", "Matthew Perry", "David Schwimmer"]

characters = ["Rachel Green", "Monica Geller", "Phoebe Buffay", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
print characters[3]
  File "<ipython-input-8-15cac104ae23>", line 2
    print characters[3]
                   ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(characters[3])?




characters = ["Rachel Green", "Monica Geller", "Phoebe Buffay", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
   ...:print(characters[3]
  File "<ipython-input-9-cada81e566d3>", line 2
    print(characters[3]
                       ^
SyntaxError: unexpected EOF while parsing




friends_dict = {
 "genre": "sitcom",
 "seasons": 10,
 "episodes": 236,
 "starrings": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}
friends_dict["genre"]
friends_dict["seasons"]
friends_dict["episodes"]
friends_dict["starrings"]
Out[10]: 
['Jennifer Aniston',
 'Courteney Cox',
 'Lisa Kudrow',
 'Matt LeBlanc',
 'Matthew Perry',
 'David Schwimmer']

friends_dict = {
 "genre": "sitcom",
 "seasons": 10,
 "episodes": 236,
 "starrings": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}
print friends_dict[episodes][starrings]
  File "<ipython-input-11-000c5c9b64a3>", line 7
    print friends_dict[episodes][starrings]
                     ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(friends_dict[episodes][starrings])?




friends_dict = {
 "genre": "sitcom",
 "seasons": 10,
 "episodes": 236,
 "starrings": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}
print(friends_dict[episodes][starrings])
Traceback (most recent call last):

  File "<ipython-input-12-b2774f366f99>", line 7, in <module>
    print(friends_dict[episodes][starrings])

KeyError: 236




friends_dict = {
 "genre": "sitcom",
 "seasons": 10,
 "episodes": 236,
 "starrings": ["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matt LeBlanc", "Matthew Perry", "David Schwimmer"]
}
friends_dict["genre"]
friends_dict["seasons"]
friends_dict["episodes"]
friends_dict["starrings"]
Out[13]: 
['Jennifer Aniston',
 'Courteney Cox',
 'Lisa Kudrow',
 'Matt LeBlanc',
 'Matthew Perry',
 'David Schwimmer']
