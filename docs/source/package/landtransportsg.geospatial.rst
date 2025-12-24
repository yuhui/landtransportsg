landtransportsg.geospatial
==========================

.. automodule:: landtransportsg.geospatial

Example usage:

.. code-block:: python

    # get a geospatial whole island layer
    from landtransportsg import Geospatial
    client = Geospatial(API_KEY)
    geospatial_whole_island = client.geospatial_whole_island('ArrowMarking')

Methods
-------

.. autoclass:: Client
   :members:
   :show-inheritance:

Argument Types
--------------
.. autoclass:: GeospatiaWholeIslandArgsDict
   :members:
   :member-order: bysource
   :show-inheritance:

Types
-----
.. autoclass:: Url
   :members:
   :member-order: bysource
   :show-inheritance:
