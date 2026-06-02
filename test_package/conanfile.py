from conan import ConanFile


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    test_type = "explicit"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        # zapif accepts -v (not --version); prints "zapif <version>" and exits 0.
        self.run("zapif -v", env="conanrun")
