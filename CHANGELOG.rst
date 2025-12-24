Changelog
=========

[2.1.0] - 2025-12-24
--------------------

Changed
^^^^^^^

- Compatibility with DataMall API v6.5:
    - **Breaking:** Updates Facilities Management endpoint to v2, and Traffic Flow Speed Bands endpoint to v4.
    - Includes the Planned Bus Routes and EV Charging Points endpoints.
- Type hints for input parameters using `Unpack` and type classes.
- Updated minimum Python version to v3.13.

[2.0.0] - 2024-12-11
--------------------

Added
^^^^^

- Type hints for input parameters and output responses.
    -  Type check performed by typeguard_.

.. _typeguard: https://typeguard.readthedocs.io/en/latest/

Changed
^^^^^^^

- Compatibility with DataMall API v6.1.1:
    - Includes the Bus Arrival v3, Platform Crowd Density endpoints.
- Updated minimum Python version to v3.10.

Deprecated
^^^^^^^^^^

- ``Traffic`` client's ``erp_rates()``.
    - The corresponding endpoint was removed in LTA DataMall v6.1 on 30 September 2024.
    - Using this method logs a ``DeprecationWarning`` warning.
    - This method will be removed in the next major release of this package or at the end of 2025, whichever is earlier.

[1.3.0] - 2020-05-31
--------------------

Changed
^^^^^^^

- Compatibility with DataMall API v5.2:
    - Includes the Facilities Maintenance endpoint.
- Refactored handling responses that return a downloadable link.
- Updated tests to use mocked responses as much as possible.

[1.2.1] - 2020-05-03
--------------------

Changed
^^^^^^^

- Compatibility with DataMall API v5.1:
    - Updates the Traffic Images duration validity.
    - Includes the Geospatial Whole Island endpoint.
- Improved testing of PublicTransport client.

[1.2.0] - 2020-05-03
--------------------

**Alert!** This version was deleted wrongly in PyPi.

[1.1.1] - 2020-01-19
--------------------

Changed
^^^^^^^

- Updated ``pytest`` requirement.

[1.1.0] - 2020-01-13
--------------------

Changed
^^^^^^^

- Compatibility with DataMall API v5:
    - Includes the Taxi Stands endpoint.

[1.0.0] - 2019-09-07
--------------------

Added
^^^^^

- Initial version to interact with LTA DataMall's documented API endpoints as of September 2019.
