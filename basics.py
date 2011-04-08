# primitives

my_string = "..." # can also be enclosed in single quotes
my_multiline_string = """
lorem ipsum
dolor sit amet
"""
my_unicode_string = u"..."
my_raw_string = r"..." # e.g. for RegEx patterns
my_int = 1
my_float = 1.0 # NB: `1 / 2` != `1.0 / 2`
success, failure = True, False


# lists

my_list = ["foo", "bar", "baz"]
my_list = my_list + ["lorem", "ipsum", "dolor", "sit", "amet"]
my_list.append("...")
print len(my_list) # 9

first = my_list[0]
last = my_list[-1]
my_slice = my_list[2:7:2] # ['baz', 'ipsum', 'sit']
print my_slice
my_selection = [item.upper() for item in my_list if item.endswith("r")] # ['BAR', 'DOLOR']
print my_selection
# slicing works for strings too
my_slice = my_list[1:] # ['baz', 'ipsum', 'sit']
print my_slice


# tuples: like lists, but immutable

my_tuple = ("foo", "bar")
#my_tuple[2] = "baz" # TypeError exception
my_tuple = tuple(my_list) # cf. list, dict etc.


# sets: unordered sequence, contains no duplicates - cf. frozenset (immutable)

my_set = set(my_list)
# mathematical operations: intersection, union, difference etc.


# generators: lazy sequence

my_gen = (item for item in my_list)
#print my_gen[0] # TypeError: unsubscriptable


# dictionaries

my_dict = {
    "foo": "lorem ipsum",
    "bar": "dolor sit amet"
}

print my_dict.keys(), my_dict.values(), my_dict.items()

for key, value in my_dict.items():
    print "%s: %s" % (key, value)

my_dict = dict([
    ('foo', 'lorem ipsum'),
    ('bar', 'dolor sit amet')
])


# functions

def do_something(foo, bar=None): # supports *args & **kwargs -- NB: beware of mutable defaults
    """
    description
    """
    return foo

sqr = lambda x: x * x # anonymous function
print sqr(3)

def my_wrapper(msg):
    prefix = "XXX"

    def my_closure(item): # LEGB: local, enclosing, global, built-in
        return prefix, item

    return my_closure(msg)

print my_wrapper("foo")


# classes

class FooBar(object): # supports multiple base classes
    """
    description
    """

    def __init__(self, name): # cf. __{repr,str,call,...}__
        self.name = name

    def do_something(self): # NB: `self` always first argument
        print self.name

my_instance = FooBar("...")
my_instance.do_something()


# exceptions - "ask for forgiveness, not permission"

try:
    [][0]
    {}["foo"]
except (IndexError, ValueError), exc:
    pass


# conditionals
if not True: # NB: truthiness; 0 and "" evaluate to False
    print "..."


# loops

while False:
    print "..."

for item in ["foo", "bar", "baz"]:
    print item

for i, item in enumerate(["foo", "bar", "baz"]):
    print "%s [#%s]" % (item, i)


# utilities

print dir(my_list)
help(my_dict) # ~ pydoc
print do_something.__doc__

# misc
# * `pass`
# * line continuation
