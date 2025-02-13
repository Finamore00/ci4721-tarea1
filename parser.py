import re
from parsec import *

whitespace = regex(r'\s*', re.MULTILINE)

lexeme = lambda p: p << whitespace

# Atomic stuff
lbrace = lexeme(string('{'))
rbrace = lexeme(string('}'))
lbrack = lexeme(string('['))
rbrack = lexeme(string(']'))
colon = lexeme(string(':'))
comma = lexeme(string(','))
true = lexeme(string("true"))
false = lexeme(string("false"))
null = lexeme(string("null"))

# Numbers (We're only implementing integers for now)
def number():
    return lexeme(
        regex(r'-?(0|[1-9][0-9]*)')
    )

# Parse strings (We're not including escape sequences)
def string_contents():
    return regex(r'[^"\\]')

@lexeme
@generate
def quoted_string():
    yield string('"')
    body = yield many(string_contents())
    yield string('"')

# Key Value pair lists via separated commas
@generate
def key_value_pair_list():
    yield quoted_string
    yield colon
    yield value
    yield key_value_list_cont

@generate
def key_value_list_cont_exists():
    yield comma
    yield key_value_pair_list

@generate
def key_value_list_cont():
    yield key_value_list_cont_exists | whitespace

#Value list via separated commas
@generate
def value_list():
    yield value
    yield value_list_cont

@generate
def value_list_cont():
    yield value_list_cont_exists | whitespace

@generate
def value_list_cont_exists():
    yield comma
    yield value_list

# Arrays
@generate
def array():
    yield lbrack
    yield value_list | whitespace
    yield rbrack

# JSON object
@generate
def j_object():
    yield lbrace
    yield (key_value_pair_list | whitespace)
    yield rbrace

# Productions for values
boolean = true | false
value = boolean | number() | quoted_string | j_object | array   #For some reason number has to be called. Don't ask me why the docs suck.

# Extra thing to skip starting whitespace idk
json = whitespace >> j_object


# Test
example = '''
{
    "person": {
        "name": "Bob",
        "age": 25
    },
    "isStudent": true,
    "scores": [90, 85, 92]
}
'''

try:
    json.parse(example)
    print("JSON object parsed successfully!")
except:
    print("Failed to parse JSON object.")