#!/usr/bin/env python
#-*-coding:utf-8-*-
# @File:Segment.py
# @Author: Michael.liu
# @Date:2019/2/12
# @Desc: NLP Segmentation ToolKit - Hanlp Python Version
import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="NlpAnalysis_pkg",
    version="0.0.1",
    author="michael.liu",
    author_email="841412988@qq.com",
    description="py_seg package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelliu03/py-seg.git",
    packages=setuptools.find_packages(),
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: LIEPIN License",
          "Operating System :: OS Independent",
    ],
)