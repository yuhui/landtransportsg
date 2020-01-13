landtransportsg.public_transport
================================

.. automodule:: landtransportsg.public_transport.client

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
