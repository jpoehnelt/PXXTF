#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import os, sys
class dnslookup:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib.request, urllib.parse, urllib.error
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('api.hackertarget.com/dnslookup'):

            wread = urllib.request.urlopen(
                'https://api.hackertarget.com/dnslookup/?q=' + host).read()
            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dnslookup"+G+"(set target)"+N+"): "))
            print()
            print(('target =>', host))
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] Error Input")
                continue

            PTF = fsave(host, 'dnslookup', wread).pansor()
            print(('Open faile save with Browser ' + PTF))
            print((""+G+""))
            os.system('firefox log/')
            break
