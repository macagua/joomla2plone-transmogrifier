# -*- coding: utf-8 -*-

import logging

from plone.i18n.normalizer import idnormalizer
from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id

logger = logging.getLogger('joomla2plone.policy')

def set_workflow_policy(obj):
    """Cambiar el workflow del objeto utilizando CMFPlacefulWorkflow.
    """
    product = 'CMFPlacefulWorkflow'
    obj.manage_addProduct[product].manage_addWorkflowPolicyConfig()
    pc = getattr(obj, WorkflowPolicyConfig_id)
    pc.setPolicyIn(policy='one-state')
    logger.info('Workflow changed for element %s' % obj.getId())

def createFolder(context, title, allowed_types=['Topic', 'Folder', 'Document'],
                 exclude_from_nav=False):
    """Crea una carpeta en el contexto especificado y modifica su política de
    workflows; por omisión, la carpeta contiene colecciones (Topic) y no
    modifica la política de workflow del contenido creado dentro de ella.
    """
    oid = idnormalizer.normalize(title, 'es')
    if not hasattr(context, oid):
        context.invokeFactory('Folder', id=oid, title=title)
        folder = context[oid]
        folder.setConstrainTypesMode(constraintypes.ENABLED)
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        set_workflow_policy(folder)
        if exclude_from_nav:
            folder.setExcludeFromNav(True)
        folder.reindexObject()
    else:
        folder = context[oid]
        folder.setLocallyAllowedTypes(allowed_types)
        folder.setImmediatelyAddableTypes(allowed_types)
        # reindexamos para que el catálogo se entere de los cambios
        folder.reindexObject()