===========
api/sources
===========

Get details on source files.
----------------------------

Examples
--------

Get SCM information of source files.::

    scm = sonar.sources.get_source_file_scm(file_key="my_project:/src/foo/Bar.php", from_line=510, to_line=560)

Get source code.::

    source_code = sonar.sources.get_source_code(file_key="my_project:/src/foo/Bar.php", from_line=510, to_line=560)

Get source code as raw text::

    source_raw = sonar.sources.get_sources_raw(file_key="my_project:/src/foo/Bar.php")

