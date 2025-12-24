landtransportsg.electric_vehicle
================================

.. automodule:: landtransportsg.electric_vehicle

Example usage:

.. code-block:: python

    # get the EV charging points
    from landtransportsg import ElectricVehicle
    client = ElectricVehicle(API_KEY)
    ev_charging_points = client.ev_charging_points('219428')

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Argument Types
--------------
.. autoclass:: EVChargingPointsArgsDict
   :members:
   :member-order: bysource
   :show-inheritance:

Types
-----
.. autoclass:: EVChargingPointsDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _EVChargingPointsLocationDataDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _EVChargingPointsLocationDataChargingPointDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _EVChargingPointsLocationDataChargingPointPlugTypeDict
   :members:
   :member-order: bysource
   :show-inheritance:
.. autoclass:: _EVChargingPointsLocationDataChargingPointPlugTypeEVIdDict
   :members:
   :member-order: bysource
   :show-inheritance:
