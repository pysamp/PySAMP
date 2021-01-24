#!python3
import sys, os, random, string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error, missing argument for server.cfg path")
        exit(1)
    updated_config = ''
    added_plugins = False
    with open(os.path.join(sys.argv[1], 'server.cfg')) as f:
        for line in f:
            if line.lstrip()[0] == '#':
                continue
            line = line.rstrip(' \r\n')
            k,v = line.split(' ', 1)
            
            if k == 'gamemode0' and v == 'grandlarc 1':
                v = 'empty 1'
            if k == 'filterscripts' and 'empty' not in v:
                v = 'empty'
            if k == 'plugins' and 'crashdetect.so' not in v:
                added_plugins = True
                v = 'crashdetect.so ' + v
            if k == 'plugins' and 'PySAMP.so' not in v:
                added_plugins = True
                v += ' PySAMP.so'
            elif k == 'plugins' and 'PySAMP.so' in v:
                added_plugins = True
            if k == 'rcon_password' and v == 'changeme':
                print("Changed default password!")
                v = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
            updated_config += '%s %s\n' % (k, v)

        if not added_plugins:
            updated_config += 'plugins crashdetect.so PySAMP.so\n'

    with open(os.path.join(sys.argv[1], 'server.cfg'), 'w') as f:
        f.write(updated_config)
        
        