# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class Address(object):
    """A physical or virtual address, or a range of addresses, in an 'addressable region' (memory or a binary file)."""

    absolute_address = attr.ib(default=-1, metadata={"schema_property_name": "absoluteAddress"})
    fully_qualified_name = attr.ib(default=None, metadata={"schema_property_name": "fullyQualifiedName"})
    index = attr.ib(default=-1, metadata={"schema_property_name": "index"})
    kind = attr.ib(default=None, metadata={"schema_property_name": "kind"})
    length = attr.ib(default=None, metadata={"schema_property_name": "length"})
    name = attr.ib(default=None, metadata={"schema_property_name": "name"})
    offset_from_parent = attr.ib(default=None, metadata={"schema_property_name": "offsetFromParent"})
    parent_index = attr.ib(default=-1, metadata={"schema_property_name": "parentIndex"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    relative_address = attr.ib(default=None, metadata={"schema_property_name": "relativeAddress"})
