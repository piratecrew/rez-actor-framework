# -*- coding: utf-8 -*-

name = "actor_framework"

version = "0.18.4"

authors = ["aupe"]

private_build_requires = [
    "cmake-3.6",
    "devtoolset-9",
]

build_command = "make -f {root}/Makefile {install}"


def commands():
    env.PATH.prepend("{root}/share/caf/tools")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CPLUS_INCLUDE_PATH.append("{root}/include")
