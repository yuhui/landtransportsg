Package Overview
================

Interacting with `LTA DataMall`_'s API is done through one of four clients,
where each client corresponds with a set of endpoints.

.. _LTA DataMall: https://www.mytransport.sg/content/mytransport/home/dataMall.html

The five clients are:

1. ``ActiveMobility``
2. ``ElectricVehicle``
3. ``Geospatial``
4. ``PublicTransport``
5. ``Traffic``

Each client contains several public functions, one function per endpoint. A
function's name is the same as its corresponding endpoint's ending path.

Some functions accept named arguments, where an argument corresponds with a
parameter that the endpoint accepts.

    *Why have separate clients instead of one single client?*

    Without knowing how `LTA DataMall`_'s API will evolve, and noticing that
    the endpoints were themselves already partitioned into sets, it seemed like
    a good idea to keep each set of endpoints in its own contextual client. This
    allows for each set of endpoints to be customised on their own, e.g. the
    ``PublicTransport`` passenger volume-related endpoints allow for a string
    to be returned, whereas the other endpoints return a list.
