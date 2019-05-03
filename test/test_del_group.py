import random
import string

def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group(random_string("group_", 10))
        old_list = app.groups.get_group_list()
    group_to_del = random.choice(old_list)
    app.groups.del_group(group_to_del)
    old_list.remove(group_to_del)
    new_list = app.groups.get_group_list()
    assert sorted(old_list) == sorted(new_list)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])