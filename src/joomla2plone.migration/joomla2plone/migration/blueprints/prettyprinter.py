import pprint
from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection

class PrettyPrinter(object):
    """ A PrettyPrinter is a blueprint for pprint library
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.pprint = pprint.PrettyPrinter().pprint

    def __iter__(self):
        for item in self.previous:
            self.pprint(sorted(item.items()))
#            type(item)
            yield item
