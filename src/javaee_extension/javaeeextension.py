##############################################################################
# COPYRIGHT Ericsson AB 2014
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from litp.core.model_type import ItemType, Collection
from litp.core.extension import ModelExtension

from litp.core.litp_logging import LitpLogger
log = LitpLogger()


class JavaEEExtension(ModelExtension):
    """
    The JavaEE Model Extension allows for the modelling of items to facilitate
    the install and configuration of JavaEE software and deployables.
    """

    def define_property_types(self):
        property_types = []
        return property_types

    def define_item_types(self):
        item_types = [
            ItemType(
                "jboss-container",
                extend_item="service",
                item_description="A JBoss container",
                deployables=Collection("deployable-entity"),
            ),
        ]
        return item_types
