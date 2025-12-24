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

Argument Types
--------------
.. autoclass:: BusArrivalArgsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: PassengerVolumeArgsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: StationCrowdDensityArgsDict
   :members:
   :member-order: bysource
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

.. autoclass:: BusRoutesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: BusServicesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: BusStopsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: FacilitiesMaintenanceDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: PlannedBusRoutesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: StationCrowdDensityRealTimeDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: StationCrowdDensityForecastDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _StationCrowdDensityForecastStationDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _StationCrowdDensityForecastStationIntervalDict
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
