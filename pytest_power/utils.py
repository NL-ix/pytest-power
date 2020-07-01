# -*- coding: utf-8 -*-
class Utils:
    @staticmethod
    def patchable_attributes(item, excludes=None, includes=None):
        """
        Patches all attributes of the given item, except magic methods other
        than __init__. The includes and excludes parameters can be used to
        customize attributes included or excluded from patching.
        """
        attributes = item.__dict__.keys()
        if includes is None:
            includes = ['__init__']

        patchables = filter(lambda x: x in includes or not x.startswith('__'),
                            attributes)
        if excludes:
            return filter(lambda x: x not in excludes, patchables)
        return patchables
