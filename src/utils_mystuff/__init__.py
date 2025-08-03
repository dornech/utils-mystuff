# utilities

"""
Package with various utils i.e. VB regex translation, CLI logging, file handling, ...

Set of submodules contains:

- submodule for converting  Microsoft VB /COM type regular expression to Python regular expression
- submodule with utilities to log CLI calls of Python scripts
- submodule with utilities for file handling
- submodule with wrapper for basic GUI functions for various GUI frameworks
- submodule with utilities specific for Win32 platform
- submodule with various utilities - read config file with standard parser, set up standard logger object ...

Raises:
    ImportError: import error if implementation is not available for platform
"""



from importlib.metadata import PackageNotFoundError, version

# try:
#     __version__ = version('utils-mystuff')
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = 'unknown'
# finally:
#     del version, PackageNotFoundError

# up-to-date version tag for modules installed in editable mode inspired by
# https://github.com/maresb/hatch-vcs-footgun-example/blob/main/hatch_vcs_footgun_example/__init__.py
# Define the variable '__version__':
try:

    # own developed alternative variant to hatch-vcs-footgun overcoming problem of ignored setuptools_scm settings
    # from hatch-based pyproject.toml libraries
    from hatch.cli import hatch
    from click.testing import CliRunner
    # determine version via hatch
    __version__ = CliRunner().invoke(hatch, ["version"]).output.strip()

except (ImportError, LookupError):
    # As a fallback, use the version that is hard-coded in the file.
    try:
        from ._version import __version__  # noqa: F401
    except ModuleNotFoundError:
        # The user is probably trying to run this without having installed the
        # package, so complain.
        raise RuntimeError(
            f"Package {__package__} is not correctly installed. Please install it with pip."
        )



from .logger_CLI import *
from .utils_filehandling import *
from .utils_GUI import *
from .utils_various import *
from .convert_regex import *



# platform / OS dependent imports
# inspiration: https://stackoverflow.com/questions/3496592/conditional-import-of-modules-in-python
# general schema:
# if sys.platform == "cli":
#     <import>
# else:
#     if os.name == "nt" or sys.platform == "win32":
#         <import>
#     elif os.name == "posix":
#         <import>
#     elif os.name == "java":
#         <import>
#     elif os.name == "macos":
#         pass
#     else:
#         raise ImportError(f"No implementation for your platform ('{os.name}') available")

if os.name == "nt" or sys.platform == "win32":
    from .utils_win32 import *
else:
    raise ImportError(f"No implementation of window utilities available for your platform ('{os.name}').")
