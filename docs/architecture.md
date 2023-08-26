# Architecture

This chapter explains how the Python Tool Manager works under the hood.

## Overview

The following picture should give you a brief overview on the data flow and the participants of the _Python Tool
Manager_ in action.

![Overview](graphs/overview.mmd.svg)

The user interacts with the exercise on the {term}`LMS` platform. The exercise communicates with the _Python Tool
Manager_ over the {term}`LTI` protocol, which handles access control and guarantees the authenticity of the data.
{term}`LMS` and _Python Tool Manager_ can run on different servers. Only server to server communication using HTTP or
HTTPS (which is strongly recommended) is mandatory.

The Python code of the exercises managed by the _Python Tool Manager_ is stored in a database and runs inside a
{term}`Docker` container. This provides an additional security layer and gives maximum flexibility to the programmer of
the exercise. The pytm library handles the communication between the exercise and the _Python Tool Manager_ backend.

## Communication

Exercise classes are stateless. Any stateful information has to be serialized and transferred to the client and back to
the server. Besides the serialized data, a
corresponding [hash-based message authentication code](https://en.wikipedia.org/wiki/HMAC) is transmitted. This prevents
client side manipulation of the data. Furthermore, input and output information is transferred between client and
backend.

![Overview](graphs/communication.mmd.svg)
