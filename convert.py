#!/usr/bin/python

from __future__ import print_function
from string import printable
import sys, locale

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Converts IPA input to SAMPA output. Does not handle certain cases: nasals, tones, syllabic consonants, and non-SAMPA representable phonetic symbols. Writes to stdout.')
    parser.add_argument('-c','--config',help='Name of the configuration table. Defaults to "table.cfg" in the working directory.',default='table.cfg')
    parser.add_argument('source',help='IPA symbols to convert to SAMPA.')
    args = parser.parse_args(sys.argv[1:])
    config = args.config
    source = args.source.decode(locale.getpreferredencoding())
    print(source)

    config = open(config,'r')
    table = {}
    for line in config:
        line=line.strip()
        if line == '': continue
        row = line.split()
        sampa_symb = row[0].decode('utf-8')
        ipa_symb = row[1].decode('utf-8')
        table[ipa_symb] = sampa_symb

    out = []
    for c in source:
        if c in table: c = table[c]
        elif c not in printable: c = ''
        out.append(c)
    print(''.join(out))
