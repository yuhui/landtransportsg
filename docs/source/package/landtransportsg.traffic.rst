landtransportsg.traffic
=======================

.. automodule:: landtransportsg.traffic.client

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
