import os, hashlib

checksums = {}

for root, dirs, files in os.walk('/'):
    for name in files:
        full_path = os.path.join(root, name)
        try:
            checksum = hashlib.md5(open(full_path, 'rb').read()).hexdigest()
            if checksum in checksums and os.path.getsize(full_path) > 100000000:
                print checksum
                print full_path 
                print checksums[checksum]
                print '\n'
            else:
                checksums[checksum] = full_path
        except:
            pass
