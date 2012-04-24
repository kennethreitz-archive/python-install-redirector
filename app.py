#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
Python-Guide Installer
~~~~~~~~~~~~~~~~~~~~~~

This module provides the core redirector experience.

Doesn't really get much simpler than this.

"""

import httpagentparser

from werkzeug.wsgi import responder
from werkzeug.utils import redirect


LOCATIONS = {
    'linux': 'http://docs.python-guide.org/en/latest/starting/install/linux/',
    'windows': 'http://docs.python-guide.org/en/latest/starting/install/win/',
    'macintosh': 'http://docs.python-guide.org/en/latest/starting/install/osx/',
    'default': 'http://docs.python-guide.org/en/latest/index.html'
}

@responder
def app(request, *args):
    agent = httpagentparser.detect(request['HTTP_USER_AGENT'])['os']['name'].lower()
    url = LOCATIONS.get(agent, LOCATIONS.get('default'))

    return redirect(url)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, app)