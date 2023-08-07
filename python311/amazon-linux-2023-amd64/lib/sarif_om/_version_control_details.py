# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class VersionControlDetails(object):
    """Specifies the information necessary to retrieve a desired revision from a version control system."""

    repository_uri = attr.ib(metadata={"schema_property_name": "repositoryUri"})
    as_of_time_utc = attr.ib(default=None, metadata={"schema_property_name": "asOfTimeUtc"})
    branch = attr.ib(default=None, metadata={"schema_property_name": "branch"})
    mapped_to = attr.ib(default=None, metadata={"schema_property_name": "mappedTo"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    revision_id = attr.ib(default=None, metadata={"schema_property_name": "revisionId"})
    revision_tag = attr.ib(default=None, metadata={"schema_property_name": "revisionTag"})
