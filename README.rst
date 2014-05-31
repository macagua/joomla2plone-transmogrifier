joomla2plone-transmogrifier
===========================

Let you migrate data from Joomla! to Plone using Transmogrifier.

This is the buildout is ispiraded from the Plone Symposium East 2011
`Clayton Parker`_ talk, `Migrating From Drupal to Plone with Transmogrifier`_.
You can see the `video here`_.

The main gol is migrate data from Joomla! to Plone using Transmogrifier

Pinning info
------------

The buildout has its versions pinned, the most important pinnings are
noted here.

The `transmogrify.sqlalchemy`_ blueprint, as of this writing does not
support `SQLAlchemy 0.7`. ::

    SQLAlchemy = 0.6.7

We are running Plone 4.0, so we need to pin this to work properly. ::

    plone.app.discussion = 1.0

Install instructions
--------------------

Joomla! Install
...............

First you should create a Joomla! site. The demo was created using
Joomla! 1.5.23, but should work fine with any Joomla! 1.5.x install.
The queries are all written in MySQL, so you'll need to set up Joomla!
using MySQL. See the Joomla! docs for more details.

In `joomla2plone.migration.config.base`, you can change the `dsn` to
match your settings. The default is to connect with the `root` user
with no password set. The default database name is `joomla-transmog`. ::

    [joomla]
    blueprint = transmogrify.sqlalchemy
    dsn = mysql://root@localhost/joomla-transmog

Running the Buildout
....................

First, get the source. ::

    $ git clone git://github.com/macagua/joomla2plone-transmogrifier.git

Now run the buildout (making sure the joomla site is up and running). ::

    $ cd joomla2plone-transmogrifier
    $ python2.7 bootstrap.py
    $ bin/buildout

Buildout will utilize the `collective.recipe.plonesite`_ recipe
to start up Zope and apply the profiles from `joomla2plone.policy`.
When it is finished the content from joomla should appear in your site.

Alternatively you can run this Buildout via CLI with parameters,
with executing this command: ::

    $ ./bin/buildout -Nvo plonesite:site-replace=true install plonesite

You can create other Plone site with the Data Joomla migrated,with executing
this command: ::

    $ ./bin/buildout -Nvo plonesite:site-replace=true plonesite:site-id=Plone1 install plonesite

Running the Joomla
------------------
Once the Joomla `install`_ and `configure`_ has finished, you can access the
site by starting up Joomla. ::

    # /etc/init.d/apache2 start
    # /etc/init.d/mysql start

Then go to the site in your browser: http://localhost/joomla/administrator/

Running the site
----------------
Once the buildout has finished, you can access the site by starting up
Plone. ::

    $ bin/zeoserver start
    $ bin/instance fg

Then go to the site in your browser: http://localhost:8080/Plone

The folders aren't currently published, so you'll have to login to see
the content. ::

    username: admin
    password: admin

Support
========

If you run into any issues trying to get this to work, please, add an
issue to the `tracker here`_ on this github project.

Collaborations
==============

Really thanks to :

Original concept
----------------

* Clayton Parker aka claytron

Original Author
----------------

* Leonardo J .Caballero G. aka macagua

Impressive collaborations
-------------------------

* Full name aka username

For an updated list of all contributors visit the following URL: https://github.com/macagua/joomla2plone-transmogrifier/contributors

.. _Migrating From Drupal to Plone with Transmogrifier: http://weblion.psu.edu/symposium/talks/migrating-from-drupal-to-plone-with-transmogrifier
.. _video here: https://streaming.psu.edu/media/?movieId=13401
.. _Clayton Parker: https://github.com/claytron
.. _transmogrify.sqlalchemy: http://pypi.python.org/pypi/transmogrify.sqlalchemy
.. _collective.recipe.plonesite: http://pypi.python.org/pypi/collective.recipe.plonesite
.. _install: http://docs.joomla.org/J3.x:Installing_Joomla!
.. _configure: http://docs.joomla.org/J3.x:Global_configuration!
.. _tracker here: https://github.com/macagua/joomla2plone-transmogrifier/issues