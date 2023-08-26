# Architecture

This chapter explains how the Python Tool Manager works under the hood.

## Overview

![Overview](graphs/overview.mmd.svg)

The user interacts with the exercise on the {term}`LMS` platform. The exercise communicates with the Python Tool Manager
over the {term}`LTI` protocol, which handles access control and guarantees the authenticity of the data. {term}`LMS` and
Python Tool Manager can run on different servers. Only server to server communication using HTTP or HTTPS
(which is strongly recommended) is mandatory.

The Python code of the exercises managed by the Python Tool Manager is stored in a database and runs inside a
{term}`Docker` container. This provides an additional security layer and gives maximum flexibility to the programmer of
the exercise.

## Exercise