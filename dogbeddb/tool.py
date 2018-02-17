
import sys

import dogbeddb

OK = 0
BAD_ARGS = 1
BAD_VERBS = 2
BAD_KEY = 3

def usage():
    print('Usage:', file=sys.stderr)
    print('\tpython -m dogbeddb.tool DBNAME get KEY', file=sys.stderr)
    print('\tpython -m dogbeddb.tool DBNAME set KEY VALUE', file=sys.stderr)
    print('\tpython -m dogbed.tool DBNAME delete KEY', file=sys.stderr)

def main(argv):
    if not (4 <= len(argv) <= 5):
        print('oohh bad args', len(argv))
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (argv[1:] + [None])[:4]
    if verb not in {'get', 'set', 'delete'}:
        usage()
        return BAD_VERB
    db = dogbeddb.connect(dbname)
    try:
        if verb == 'get':
            sys.stdout.write(db[key])
        elif verb == 'set':
            db[key] = value
            db.commit()
        else:
            del db[key]
            db.commit()
    except KeyError:
        print("Key not found", file=sys.stderr)
        return BAD_KEY
    return OK


if __name__ == '__main__':
    sys.exit(main(sys.argv))

