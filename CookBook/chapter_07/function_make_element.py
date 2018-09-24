"""
To accept any number of keyword argument use an argument with **.
"""
import html


def make_element(name, value, **attrs):
    key_vals = ['%s = "%s"' % item for item in attrs.items()]
    attr_str = ''.join(key_vals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element


print(make_element('item', 'Albatross', size='large', quantity=6), end='\n')
print(make_element('p', '<spam>'))

