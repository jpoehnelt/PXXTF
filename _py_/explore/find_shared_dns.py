#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import sys,os
class find_shared_dns:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor(
                'api.hackertarget.com/findshareddns'):

            wread = urllib.urlopen(
                'https://api.hackertarget.com/findshareddns/?q=' + host).read()
            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = raw_input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/find_shared_dns"+G+"(set target)"+N+"): ")
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] Error Input")
                continue

            saved = fsave(host, 'find_shared_dns', wread).pansor()
            print('Open faile save with Browser ' + saved)
            print ""+G+""
            os.system('firefox log/ ')
            break
