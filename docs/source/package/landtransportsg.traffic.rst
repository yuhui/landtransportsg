landtransportsg.traffic
=======================

.. automodule:: landtransportsg.traffic

Example usage:

.. code-block:: python

    # get the list of available car park spaces
    from landtransportsg import Traffic
    client = Traffic(API_KEY)
    patents = client.carpark_availability()

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Types
-----

.. autoclass:: CarParkAvailabilityDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: EstimatedTravelTimesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: FaultyTrafficLightsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: RoadOpeningsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: RoadWorksDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TrafficImagesDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TrafficIncidentsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: TrafficSpeedBandsDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: VMSDict
   :members:
   :member-order: bysource
   :show-inheritance:

.. autoclass:: Url
   :members:
   :member-order: bysource
   :show-inheritance:
