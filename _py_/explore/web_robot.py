#!/usr/bin/env python

R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import sys,os
class web_robot:
    def __init__(self):
        pass

    def atom(self, host, tag):
        from urllib.request import urlopen
        from urllib.parse import unquote
        from bs4 import BeautifulSoup
        from core.urli import sansor

        def _reading(html, tag):
            soup = BeautifulSoup(html, 'html.parser').find_all(tag)
            if soup == []:
                soup.append('none')
            else:
                return soup

        def _script(html):
            soup = BeautifulSoup(
                html, 'html.parser').find_all(
                'script', src=True)

            if soup == []:
                soup.append('none')
            else:
                script = []
                for link in soup:
                    link = link.get('src')
                    script.append(unquote(link))
                return script

        def _link(html):
            soup = BeautifulSoup(
                html, 'html.parser').find_all(
                'link', href=True)

            if soup == []:
                soup.append('none')
            else:
                link = []
                for key in soup:
                    key = key.get('href')
                    link.append(unquote(key))
                return link

        def _img(html):
            soup = BeautifulSoup(html, 'html.parser').find_all('img', src=True)

            if soup == []:
                soup.append('none')
            else:
                img = []
                for key in soup:
                    key = key.get('src')
                    img.append(unquote(key))
                return img

        host = sansor().pransor(host)
        if sansor().cransor(host):
            html = urlopen('http://' + host).read()
            if tag == 'img':
                wread = _img(html)
            elif tag == 'link':
                wread = _link(html)
            elif tag == 'script':
                wread = _script(html)
            else:
                wread = _reading(html, tag)

            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/web_robot "+G+"(set target)"+N+"): "))

            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            option = '''\n1> a\n2> meta tag\n3> input \n4> form\n5> iframe\n6> h1\n7>script\n8> img\n9> all photo link\n10> all script page link\n11>all css page link\n'''

            while True:
                print(option)
                lnx = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/web_robot "+G+"(set target)"+N+"): "))
                if host == 'exit':
                    sys.exit()
                elif host == 'back':
                    break
                elif lnx == '1':
                    recv = self.atom(host, 'a')
                elif lnx == '2':
                    recv = self.atom(host, 'meta')
                elif lnx == '3':
                    recv = self.atom(host, 'input')
                elif lnx == '4':
                    recv = self.atom(host, 'form')
                elif lnx == '5':
                    recv = self.atom(host, 'iframe')
                elif lnx == '6':
                    recv = self.atom(host, 'h1')
                elif lnx == '7':
                    recv = self.atom(host, 'script')
                elif lnx == '8':
                    recv = self.atom(host, 'img')
                elif lnx == '9':
                    recv = self.atom(host, 'img')
                elif lnx == '10':
                    recv = self.atom(host, 'script')
                elif lnx == '11':
                    recv = self.atom(host, 'link')
                elif lnx == 'exit':
                    sys.exit()
                elif lnx == '':
                    continue
                else:
                    continue
                break

            if recv is None:
                print("\t[-] Error Input")
                continue

            length = "all : " + str(len(recv)) + "<br>"
            wread = str(recv).replace('<', '')
            wread = wread.replace(',', '<br>')
            wread = fsave(host, 'web_robot', length + wread).pansor()
            print(('Open faile save with Browser ' + wread))
            print((""+G+""))
            os.system('firefox log/ ')
            break
