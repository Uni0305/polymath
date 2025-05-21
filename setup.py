import sys, os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# ensure cython is installed
try:
    from Cython.Distutils import build_ext as cython_build_ext
except:
    print("You don't seem to have Cython installed. Please get a")
    print("copy from www.cython.org and install it")
    sys.exit(1)


# scan the provided directory for extension files, converting
# them to extension names in dotted notation
def scandir(dir, files=[]):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and path.endswith(".py"):
            files.append(path.replace(os.path.sep, ".")[:-3])
        elif os.path.isdir(path):
            scandir(path, files)
    return files


# generate an Extension object from its dotted name
def makeExtension(extName):
    extPath = extName.replace(".", os.path.sep) + ".py"
    return Extension(
        extName,
        [extPath],
        include_dirs=[],
        extra_compile_args=["-O3", "-Wall"],
        extra_link_args=["-g"],
        libraries=[],
    )


# get the list of extensions
extNames = scandir("polymath")

# and build up the set of Extension objects
extensions = [makeExtension(name) for name in extNames]

# finally, we can pass all this to distutils
setup(
    name="polymath",
    packages=["polymath", "polymath.filters"],
    ext_modules=extensions,
    cmdclass={"build_ext": cython_build_ext},
)