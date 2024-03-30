# SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
# SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

import sys
from pathlib import Path
from Cython.Tempita import sub

template = Path(sys.argv[1]).read_text('utf8')
output = sub(template)
Path(sys.argv[2]).write_text(output, 'utf8')
