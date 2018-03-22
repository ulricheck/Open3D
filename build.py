from conan.packager import ConanMultiPackager
from conans.tools import os_info
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(pure_c=True)
    builder.run()
