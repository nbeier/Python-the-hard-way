# means that the formater for 4 items in a row is to put space between them
formatter = "%s %s %s %s"
# prints 1 2 3 4 with spaces, using the format defined above
print formatter % (1, 2, 3, 4)
# prints one two three four with spaces
print formatter % ("one", "two", "three", "four")
# prints with spaces
print formatter % (True, False, False, True)
# prints the formatter string, the % tells to print exactly what is in the string
print formatter % (formatter, formatter, formatter, formatter)
# prints the four sentences with spaces in between in a single line.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
