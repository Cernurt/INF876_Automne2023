# Parse BibTex entries from input file and render them in IEEEtran.cls format
# http://www.michaelshell.org/tex/ieeetran/
# Usage: python bibtexconverter.py [bibtex file]
#
# BibTex example (input):
# @article{lecun2015deep,
#   title={Deep learning},
#   author={LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey},
#   journal={Nature},
#   volume={521},
#   number={7553},
#   pages={436--444},
#   year={2015},
#   publisher={Nature Publishing Group}
# }
#
# IEEETran example (output):
# \bibitem{lecun2015deep} Y.~LeCun and Y.~Bengio and G.~Hinton, \emph{Deep learning}.\hskip 1em plus 0.5em minus 0.4em\relax Nature, Nature Publishing Group, 2015.


import re
import sys
from pprint import pprint


def ieee(refs):
    print '\n'
    for ref in refs:
        print _ieee(ref) + '\n'


def _ieee(dic):
    return """\\bibitem{{{}}} {}, \\emph{{{}}}.\\hskip 1em plus 0.5em minus 0.4em\\relax {}, {}.""".format(
        dic['refcode'],
        _ieee_author(dic['author']),
        dic['title'],
        _ieee_publisher(dic),
        dic['year']
    )


def _ieee_publisher(dic):
    publisher = []
    keys = ['journal', 'booktitle', 'publisher', 'organization']
    for key in keys:
        if key in dic:
            publisher.append(dic[key])
    return ', '.join(publisher)


def _ieee_author(text):
    formatted = []
    authors = text.split(' and ')
    for a in authors:
        names = a.split(', ')
        if len(names) >= 2:
            last, first = names[0], names[1]
            formatted.append(first[0].upper() + '.~' + last)
        else:
            formatted.append(names[0])
    return ' and '.join(formatted)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python bibtexconverter.py [bibtex file]'
        exit()

    filename = sys.argv[1]

    # collect BibTex entries from input file
    # separated by blank line
    entries = []
    with open(filename) as f:
        entry = []
        for line in f:
            line = line.strip()
            if len(line) > 0:
                # save line
                entry.append(line)
            elif len(entry) > 0:
                # blank line
                entries.append(entry)
                entry = []
        # last entry
        if len(entry) > 0:
            entries.append(entry)

    # parse BibTex entries
    references = []
    for entry in entries:
        dic = {}
        dic['refcode'] = re.search(r'@(article|inproceedings|thesis){([\w\d]*),', entry[0], re.M | re.I).group(2)
        for i in range(1, (len(entry) - 1)):
            key, value = entry[i].split('=')
            value = re.search(r'{([^{}]*)}', value, re.M | re.I).group(1)
            dic[key] = value
        references.append(dic)

    # render entries in IEEEtran.cls format
    # http://www.michaelshell.org/tex/ieeetran/
    ieee(references)
