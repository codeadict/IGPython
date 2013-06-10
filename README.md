Open Weigh
==========

Software for Weighting Devices

![Image](igpython/static/img/reporting-img.jpg)

Contributing
------------

Consider any moment in life that you could have been writing **unit tests**.

The easiest way to add features is to write a plugin. Please create an issue to discuss whether your plugin idea is a core plugin (`plugins.*`) or external plugin. If there are additions needed to the plugin API, we can discuss that as well!


Manifesto
---------

Create a mature software for weigh in Devices based on Python and Django following this principles:

 * **Be pluggable and light-weight.** Don't integrate optional features in the core.
 * **Be open.** Make an extension API that allows the ecology of the software to grow.
 * **Be simple.** The source code should *almost* explain itself.

Installing
----------

### Pre-requisites

OpenWeigh uses the [PIL library](http://www.pythonware.com/products/pil/) for image processing. The preferred method should be to get a system-wide version of PIL, for instance by getting the binaries from your Linux distribution repos.

**PIL Directly from repository: Debian-based Linux Distros**

    sudo apt-get install python-imaging

**PIL/Pillow for Pypi**

Firstly, you need to get development libraries that PIP needs before compiling. For instance on Debian/Ubuntu:

    sudo apt-get install libjpeg8 libjpeg-dev libpng libpng-dev

After that, choose either `pip install PIL` or `pip install Pillow`. Pillow is the pip-friendly version of PIL. You might as well install PIL system-wide, because there are little version-specific dependencies in Django applications when it comes to PIL.

### Downloading the source code

To get the latest Source Code clone this repository by running:

	git clone git@github.com:codeadict/IGPython.git

    Be sure to have git installed on your system.

## Create Database

After configuring OpenWeigh the next step is to create the database used by it by running: 

    python manage.py syncdb

    

