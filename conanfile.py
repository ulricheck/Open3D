from conans import ConanFile, CMake, tools
import os
from io import StringIO


class Open3dConan(ConanFile):
    version = "0.1.0"

    name = "open3d"
    license = "https://github.com/IntelVCL/Open3D/raw/master/LICENSE"
    description = "Open3D: A Modern Library for 3D Data Processing http://www.open3d.org (Forked for use with Ubitrack"
    url = "https://github.com/ulricheck/Open3D"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    short_paths = True

    requires = (
        "eigen/[>=3.3.4]@camposs/stable",
        "glfw/3.2.1@camposs/stable",
        "pybind11/2.2.1@camposs/stable",
        )

    options = {
        "python": "ANY",
        "opengl_extension_wrapper": ["glew", "glad"],
        }

    default_options = (
        "python=python",
        "opengl_extension_wrapper=glad",
        )

    # all sources are deployed with the package
    exports_sources = "docs/*", "scripts/*", "src/*", "CMakeLists.txt"

    def requirements(self):
        if self.options.opengl_extension_wrapper == 'glad':
            self.requires("glad/0.1.16a0@bincrafters/stable")
        elif self.options.opengl_extension_wrapper == 'glew':
            self.requires("glew/2.1.0@camposs/stable")


    def configure(self):
        if self.options.opengl_extension_wrapper == 'glew':
            self.options["glew"].shared = False
        self.options["glfw"].shared = False

    def build(self):
        cmake = CMake(self)
        cmake.definitions["Open3D_USE_NATIVE_DEPENDENCY_BUILD"] = False
        cmake.definitions["Open3D_BUILD_TESTS"] = False
        cmake.definitions["Open3D_BUILD_PYTHON_BINDING"] = True
        cmake.definitions["Open3D_BUILD_PYTHON_BINDING_TESTS"] = False
        cmake.definitions["Open3D_BUILD_PYTHON_BINDING_TUTORIALS"] = True
        cmake.definitions["OPENGL_EXTENSION_WRAPPER"] = self.options.opengl_extension_wrapper 

        self.output.info("python executable: %s (%s)" % (self.python_exec.replace("\\", "/"), self.python_version))
        cmake.definitions['PYBIND11_PYTHON_VERSION'] = self.python_version
        if self.settings.os == "Macos":
            cmake.definitions['CMAKE_FIND_FRAMEWORK'] = "LAST"

        cmake.configure(source_dir="src")
        cmake.build()
        cmake.install()
        os.rename("LICENSE", "LICENSE.Open3D")

    def package(self):
        src_folder = "src"
        for name in ["Core", "IO", "Visualization"]:
            self.copy("*.h", src=os.path.join(src_folder, name), dst="include/%s" % name, keep_path=True)
        self.copy("*", src=os.path.join(self.build_dir, "bin"), dst="bin", keep_path=False)
        self.copy("*.a", src=os.path.join(self.build_dir, "lib"), dst="lib", keep_path=False)
        self.copy("py3d.*", src=os.path.join(self.build_dir, "lib"), dst="lib/python", keep_path=False)
        self.copy("LICENSE.Open3D")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    @property
    def python_exec(self):
        try:
            pyexec = str(self.options.python)
            output = StringIO()
            self.run('{0} -c "import sys; print(sys.executable)"'.format(pyexec), output=output)
            return '"'+output.getvalue().strip().replace("\\","/")+'"'
        except:
            return ""
    
    _python_version = ""
    @property
    def python_version(self):
        cmd = "from sys import *; print('%d.%d' % (version_info[0],version_info[1]))"
        self._python_version = self._python_version or self.run_python_command(cmd)
        return self._python_version
      
    def run_python_command(self, cmd):
        pyexec = self.python_exec
        if pyexec:
            output = StringIO()
            self.run('{0} -c "{1}"'.format(pyexec, cmd), output=output)
            return output.getvalue().strip()
        else:
            return ""

