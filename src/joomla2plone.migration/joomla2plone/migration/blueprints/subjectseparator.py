from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection

class SubjectReplaceSeparator(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.items = []

        item['subject'] = item['subject'].replace(',', '\n')
        self.items.append(item)

    def __iter__(self):
        for item in self.previous:
            yield item

        for item in self.items:
            yield item
