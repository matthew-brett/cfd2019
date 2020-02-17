with open('nasty_stuff.csv.utf-8', 'rt') as fobj:
    contents = fobj.read()
with open('nasty_stuff.csv', 'wb') as fobj:
    fobj.write(contents.encode('latin1'))
