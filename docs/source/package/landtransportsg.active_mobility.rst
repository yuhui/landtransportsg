landtransportsg.active_mobility
===============================

.. automodule:: landtransportsg.active_mobility.client

Example usage:

.. code-block:: python

    # get the bicycle parking locations
    from landtransportsg import ActiveMobility
    client = ActiveMobility(API_KEY)
    bicycle_parking_locations = client.bicycle_parking(1.364897, 103.766094)

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:
