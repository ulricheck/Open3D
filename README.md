# Branch of IntelLabs Open3D for Ubitrack Integration
## This repository holds a conan recipe for open3d.

[Conan.io](https://conan.io) package for [the open3d C++ library](https://github.com/IntelVCL/Open3D) project

## For Users: Use this package

### Basic setup

    $ conan install open3d/0.1.0@camposs/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    open3d/0.1.0@camposs/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
    
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to ulricheck conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create camposs/stable
    
## Add Remote

    $ conan remote add camp "https://conan.campar.in.tum.de" True

## Upload

    $ conan upload -r camp open3d/0.1.0@camposs/stable

### License
[License](https://github.com/google/open3d/master/LICENSE.txt)


# ORIGINAL README
-----------------


# Open3D: A Modern Library for 3D Data Processing

[![Build Status](https://travis-ci.org/IntelVCL/Open3D.svg?branch=master)](https://travis-ci.org/IntelVCL/Open3D)
[![Build status](https://ci.appveyor.com/api/projects/status/sau3yewsyxaxpkqe?svg=true)](https://ci.appveyor.com/project/syncle/open3d)

## About this project

Open3D is an open-source library that supports rapid development of software that deals with 3D data. The Open3D frontend exposes a set of carefully selected data structures and algorithms in both C++ and Python. The backend is highly optimized and is set up for parallelization. We welcome contributions from the open-source community.

Please cite our work if you use Open3D.
```
@article{Zhou2018,
	author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
	title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
	journal   = {arXiv:1801.09847},
	year      = {2018},
}
```

## Core features

* Basic 3D data structures
* Basic 3D data processing algorithms
* Scene reconstruction
* Surface alignment
* 3D visualization
* Python binding

## Supported compilers

* GCC 4.8 and later on Linux
* XCode 8.0 and later on OS X
* Visual Studio 2015 and later on Windows

## Resources

* Website: [www.open3d.org](http://www.open3d.org)
* Code: [github.com/IntelVCL/Open3D](https://github.com/IntelVCL/Open3D)
* Document: [www.open3d.org/docs](http://www.open3d.org/docs)
* License: [The MIT license](https://opensource.org/licenses/MIT)
