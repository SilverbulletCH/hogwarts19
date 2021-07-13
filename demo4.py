import time

print(time.strftime("%y%m%d %H:%M:%S", time.localtime()))

print(time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒'))