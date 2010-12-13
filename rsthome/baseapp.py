# -*- coding: utf-8 -*-
"""
Base application class.
"""

from __future__ import with_statement
import os
import sys
import ConfigParser
import jinja2
import pygsetup
from docutils.core import publish_parts


class BaseApp(object):

    """
    Base application on which all the building script should depend. It
    takes care of all the configuration and all the core level rendering.
    """
 
    def __init__(self, config_filename):
        self.basedir = os.path.dirname(config_filename)
        if not self.basedir:
            self.basedir = "."

        cp = ConfigParser.ConfigParser({"here": self.basedir})
        with open(config_filename) as fp:
            cp.readfp(fp)
        self.config = dict(cp.items("general"))

    def render_template(self, filename, parts):
        """Render the given template using the given variables.

        :param filename: File path to read.
        :param parts: Variables replaced in the template.
        """

        searchpath = os.path.join(self.basedir, "templates")

        env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath))

        tmpl = env.get_template(filename)


        # Update the namespace with all the global definitions from the
        # configuration file. This is typically done for site name, 
        # copyright information, etc.
        for key in self.config:
            if key.startswith("namespace."):
                parts[key[4:]] = self.config[key]

        return tmpl.render(parts)

    def render_rst(self, filename):
        """Render an RST file, returns the parts.

        :param filename: Path to an RST file.
        """
        with open(filename) as fp:
            parts = publish_parts(source=fp.read(), writer_name="html4css1")
        return parts

