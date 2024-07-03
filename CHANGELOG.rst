.. SPDX-FileCopyrightText: Daniele Nicolodi <daniele@grinta.net>
.. SPDX-License-Identifier: Apache-2.0 OR LGPL-2.1-or-later

1.6
---

- For consistency with the ``hashlib`` module, ``hexdisted()`` returns
  a string object, not bytes.

Released 03-07-2024.

1.5
---

- Update dependencies to latest released versions.
- Add SPDX headers to all source files and add licenses text in
  ``LICENSES`` directory.

Released 30-03-2024.

1.4
---

- Update build dependencies.
- Set default buildtype to release.
- Build wheels for Python 3.12.

Released 03-10-2023.

1.3
---

- Update build dependencies to released versions. No functional changes.

Released 03-03-2023.

1.2
---

- Use `c-siphash library`__ without modifications.
- Switch the build system to Meson and meson-python.
- Add support for the SipHash-1-3 variant.

__ https://github.com/c-util/c-siphash

Released 21-11-2022.


1.1
---

- Added the :meth:`intdigest() <hash.intdigest>` method.
- Added reStructuredText `documentation`__.

__ https://dnicolodi.github.io/python-siphash24/

Released 06-11-2022.


1.0
---

Initial release, 11-09-2022.
