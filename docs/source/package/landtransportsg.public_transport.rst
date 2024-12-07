landtransportsg.public_transport
================================

.. automodule:: landtransportsg.public_transport

Example usage:

.. code-block:: python

    # get the bus arrival information at a bus stop
    from landtransportsg import PublicTransport
    client = PublicTransport(API_KEY)
    bus_arrival = client.bus_arrival('83139')

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----
.. autoclass:: BusArrivalDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _NextBusDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: BusServicesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: BusRoutesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: BusStopsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: PlatformCrowdDensityRealTimeDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: PlatformCrowdDensityForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _PlatformCrowdDensityForecastStationDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _PlatformCrowdDensityForecastStationIntervalDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TaxiAvailabilityDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TaxiStandsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TrainServiceAlertsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: Url
   :members:
   :member-order: bysource
   :show-inheritance:
