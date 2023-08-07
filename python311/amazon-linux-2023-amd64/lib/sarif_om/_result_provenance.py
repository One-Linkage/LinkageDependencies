# This file was generated by jschema_to_python version 1.2.3.

import attr


@attr.s
class ResultProvenance(object):
    """Contains information about how and when a result was detected."""

    conversion_sources = attr.ib(default=None, metadata={"schema_property_name": "conversionSources"})
    first_detection_run_guid = attr.ib(default=None, metadata={"schema_property_name": "firstDetectionRunGuid"})
    first_detection_time_utc = attr.ib(default=None, metadata={"schema_property_name": "firstDetectionTimeUtc"})
    invocation_index = attr.ib(default=-1, metadata={"schema_property_name": "invocationIndex"})
    last_detection_run_guid = attr.ib(default=None, metadata={"schema_property_name": "lastDetectionRunGuid"})
    last_detection_time_utc = attr.ib(default=None, metadata={"schema_property_name": "lastDetectionTimeUtc"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
