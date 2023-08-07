# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class SpecialLocations(object):
    """Defines locations of special significance to SARIF consumers."""

    display_base = attr.ib(default=None, metadata={"schema_property_name": "displayBase"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
