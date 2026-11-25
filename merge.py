import urllib.request
URL="https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/doh-vpn-proxy-bypass-onlydomains.txt"
def clean(lines): return {l.strip().lower() for l in lines if l.strip() and not l.strip().startswith('#')}
hz=clean(urllib.request.urlopen(URL,timeout=60).read().decode().splitlines())
if len(hz)<10000: raise SystemExit("HaGeZi list looks broken, keeping old file")
ex=clean(open('extras.txt'))
allset=hz|ex
open('blocklist.txt','w').write('\n'.join(sorted(allset))+'\n')
print(len(hz),len(ex),len(allset))
