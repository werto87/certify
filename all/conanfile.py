from conans import ConanFile, tools
from conans.tools import check_min_cppstd
import os


class Certify(ConanFile):
    version = "0.0.1"
    name = "certify"
    homepage = "https://github.com/djarek/certify"
    description = "Boost.ASIO-based TLS certificate verification library"
    topics = ("certificate verification")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True
    scm = {
        "type": "git",
        "subfolder": "certify_src",
        "url": "https://github.com/djarek/certify.git",
        "revision": "master"
    }

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("boost/1.76.0")
        self.requires("openssl/1.1.1k")

    def package(self):
        # This should lead to an Include path like #include "include_folder/IncludeFile.hxx"
        self.copy("*.h*", dst="include/boost/certify/",
                  src="certify_src/include/boost/certify/")
        self.copy("*.i*", dst="include/boost/certify/",
                  src="certify_src/include/boost/certify/")

    def package_id(self):
        self.info.header_only()
