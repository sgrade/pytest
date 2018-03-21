# some code from NAPALM


# python2/3 support
try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest


def list_dicts_diff(prv, nxt):
    """Compare two lists of dicts."""
    result = []
    for prv_element, nxt_element in zip_longest(prv, nxt, fillvalue={}):
        intermediate_result = dict_diff(prv_element, nxt_element)
        if intermediate_result:
            result.append(intermediate_result)
    return result


def dict_diff(prv, nxt):
    """Return a dict of keys that differ with another config object."""
    keys = set(list(prv.keys()) + list(nxt.keys()))
    result = {}

    for k in keys:
        if isinstance(prv.get(k), dict):
            if isinstance(nxt.get(k), dict):
                "If both are dicts we do a recursive call."
                diff = dict_diff(prv.get(k), nxt.get(k))
                if diff:
                    result[k] = diff
            else:
                "If only one is a dict they are clearly different"
                result[k] = {'result': prv.get(k), 'expected': nxt.get(k)}
        else:
            "Ellipsis is a wildcard."""
            if prv.get(k) != nxt.get(k) and nxt.get(k) != "...":
                result[k] = {'result': prv.get(k), 'expected': nxt.get(k)}
    return result


prv = {'routers': 'bgp', 'switches': 'ex'}
nxt = {'routers': 'bgp', 'switches': 'qfx', 'firewalls': 'palo-alto'}

print(dict_diff(prv, nxt))

#
# list_dicts_diff(prv, nxt)

