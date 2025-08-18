import hmac,hashlib

key = b"jlebedev"
msg = b"smashthestate"
digest=hmac.new(key,msg,hashlib.md5).hexdigest()
print(digest[:8])

'''
The VNC login is the following message, 'smashthestate', hmac'ed with my username from the 'bad actors' list (lol).
Use md5 for the hmac hashing algo. The first 8 characters of the final hash is the VNC password. - JL
For THM Box DX1-Liberty-Island
'''
