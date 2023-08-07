# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class WebRequest(object):
    """Describes an HTTP request."""

    body = attr.ib(default=None, metadata={"schema_property_name": "body"})
    headers = attr.ib(default=None, metadata={"schema_property_name": "headers"})
    index = attr.ib(default=-1, metadata={"schema_property_name": "index"})
    method = attr.ib(default=None, metadata={"schema_property_name": "method"})
    parameters = attr.ib(default=None, metadata={"schema_property_name": "parameters"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    protocol = attr.ib(default=None, metadata={"schema_property_name": "protocol"})
    target = attr.ib(default=None, metadata={"schema_property_name": "target"})
    version = attr.ib(default=None, metadata={"schema_property_name": "version"})
