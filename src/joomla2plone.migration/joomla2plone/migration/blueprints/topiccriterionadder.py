import pprint
from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection

class TopicCriterionAdder(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.items = []
        item = {}

        '''
        >>> items = []
        >>>
        >>> item = {'_path':'/organizacion'}
        >>> item['_field'] = 'Type'
        >>> item['_criterion'] = 'ATPortalTypeCriterion'
        >>> items.append(item)
        >>> items
        [{'_criterion': 'ATPortalTypeCriterion', '_field': 'Type', '_path': '/organizacion'}]
        '''
        # _path=bar/baz
        # item = {'_path':item['_path']}
        # item = {'_path':'articulos/la-fundacion-macagua'}
        # _field=Type
        item['_field'] = 'News Item'
        # _criterion=ATFriendlyDateCriteria
        item['_criterion'] = 'ATPortalTypeCriterion'
        self.items.append(item)

    def __iter__(self):
        for item in self.previous:
            yield item

        for item in self.items:
            yield item

#class PrettyPrinter(object):
#    classProvides(ISectionBlueprint)
#    implements(ISection)

#    def __init__(self, transmogrifier, name, options, previous):
#        self.previous = previous
#        self.pprint = pprint.PrettyPrinter().pprint

#    def __iter__(self):
#        for item in self.previous:
#            self.pprint(sorted(item.items()))
##            type(item)
#            yield item
