
# problem 1:
# Write a Python function only_truthy, which is only capable of accepting keyword arguments (but no positional arguments), and
# returns a dictionary whose keys are the names of any specified keyword arguments (each preceded by an underscore character: _),
# and whose values are the values of those same arguments. Notably, though, any argument whose value is considered falsy is left out of the result.


def only_truthy(**kwargs):
    only_dic = {}
    for key, value in kwargs.items():
        if value:
            only_dic["_" + key] = value
    return only_dic

