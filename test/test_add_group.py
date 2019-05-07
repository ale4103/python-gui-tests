import random
import string
from generator import gengroups

def test_add_group(app):
    old_list = app.groups.get_group_list()
    #new_group = random_string("group_", 10)
    new_group = app.gengroups.read_excel()
    app.groups.add_new_group(new_group)
    new_list = app.groups.get_group_list()
    old_list.append(new_group)
    assert sorted(old_list) == sorted(new_list)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])