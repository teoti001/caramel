#! /usr/bin/env python
# vim: expandtab shiftwidth=4 softtabstop=4 tabstop=17 filetype=python :
import argparse

from sqlalchemy import create_engine

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

import caramel.config as config
from caramel.models import init_session


def cmdline(args):
    parser = argparse.ArgumentParser()
    config.add_inifile_argument(parser)
    config.add_db_url_argument(parser)
    parsed_args = parser.parse_args(args)
    return parsed_args


def main(args):
    parsed_args = cmdline(args)
    config_uri = parsed_args.inifile
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    db_url = config.get_db_url(parsed_args, settings)
    engine = create_engine(db_url)
    init_session(engine, create=True)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
