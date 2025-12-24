landtransportsg
===============

|pyversions| |pypi| |status| |codecov| |downloads| |license| |readthedocs|

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/landtransportsg
   :alt: Python 3.10
.. |pypi| image:: https://img.shields.io/pypi/v/landtransportsg
   :alt: PyPi
   :target: https://pypi.org/project/landtransportsg
.. |status| image:: https://img.shields.io/pypi/status/landtransportsg
   :alt: PyPi status
.. |codecov| image:: https://codecov.io/github/yuhui/landtransportsg/graph/badge.svg?token=nBlQ5KI6Ly
   :target: https://codecov.io/github/yuhui/landtransportsg
   :alt: CodeCov coverage
.. |downloads| image:: https://img.shields.io/pypi/dm/landtransportsg
.. |license| image:: https://img.shields.io/github/license/yuhui/landtransportsg
   :alt: GNU General Public License v3.0
   :target: https://www.gnu.org/licenses/gpl-3.0.html
.. |readthedocs| image:: https://readthedocs.org/projects/landtransportsg/badge/?version=latest
   :alt: Documentation Status
   :target: https://landtransportsg.readthedocs.io/en/latest/?badge=latest

This is an unofficial Python package for interacting with APIs available at
`LTA DataMall`_.

.. _LTA DataMall: https://datamall.lta.gov.sg/content/datamall/en.html

Installing the package
----------------------

Install the package using ``pip``::

    pip install landtransportsg

Using the package
-----------------

Pre-requisite:

- API key from LTA. `Request for API access`_.

.. _Request for API access: https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html

The main steps are:

1. Import a client class.
2. Instantiate an object from the client class.
3. Call a function on that object.

For more information, `refer to the documentation`_.

.. _refer to the documentation: https://landtransportsg.readthedocs.io/

Usage overview
^^^^^^^^^^^^^^

Interacting with `LTA DataMall`_'s API is done through one of four clients,
where each client corresponds with a set of endpoints.

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

Reference
---------

`LTA DataMall's Developer Guide`_

.. _LTA DataMall's Developer Guide: https://www.mytransport.sg/content/mytransport/home/dataMall/dynamic-data.html

Other Packages Built by Me
--------------------------

If you like this package, you may be interested in these packages that I have
built to work with other Government of Singapore APIs:

- `datagovsg`_: for interacting with APIs available at Data.gov.sg.
- `singstat`_: for interacting with APIs available at SingStat.gov.sg.

.. _datagovsg: https://pypi.org/project/datagovsg/
.. _singstat: https://pypi.org/project/singstat/
