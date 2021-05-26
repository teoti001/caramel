#! /usr/bin/env python
# vim: expandtab shiftwidth=4 softtabstop=4 tabstop=17 filetype=python :
"""tests"""
import os
import unittest

from pyramid.scripts import pserve

from caramel.scripts.generate_ca import main as generate_ca
from caramel.scripts.initializedb import main as init_db


class TestServer(unittest.TestCase):
    ENV_VARIABLES = {
        "CARAMEL_INI": "asd",
        "CARAMEL_DB_URL": "ASDASD",
        "CARAMEL_CA_CERT": "ASDASD",
        "CARAMEL_CA_KEY": "ASDASD",
        "CARAMEL_LOG_LEVEL": "ASDASD",
    }

    def test_conf_via_env(self):
        for variable, value in TestServer.ENV_VARIABLES.items():
            os.environ[variable] = value
        generate_ca([""])
        # checky-checky key and cert files
        init_db([""])
        # checky-checky db finns på rätt ställe och sånt?
        # vill man egentligen ha fixtures här som själva kör init_db och generate_ca
        # och kollar att de funkar, för man vill väl veta vilket steg som failar?
        server = pserve.PServeCommand(["pserve", "development.ini"])
        server.run()
        # testa att hämta något och ladda upp något typ, och göra asserts på det?
