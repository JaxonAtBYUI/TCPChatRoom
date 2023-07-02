# Overview

This is a simple TCP 'chatroom' which I created to dip my toes into networking. It has two working pieces. The first is the server. This can simply be run using python on any machine. Currently it is hardcoded to use the IP 127.0.0.1 as the IP and port 55555 meaning that it runs on local host. This is for testing and learning purposes.
The second piece is the client. 

The client can also be separately run from the server using python. The client will ask the user for an IP, port, and username that they would like to be known by on that server for the duration of their connection. The client will conect to the server, and all messages sent by the user will be passed to the server, where it will then be sent out to all other users currently connected.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/ITODBmz-Jco)

# Network Communication

The architcture used to create this program is client server architecture, using TCP, with the default IP and port being 127.0.0.1:55555. It is sending the messages back and forth between server and clients as ASCII

# Development Environment

This was created in VS code using python, with the threading and socket libraries.

# Useful Websites

* [Python Documentation - Threading](https://docs.python.org/3/library/threading.html)
* [Python Documentation - Socket](https://docs.python.org/3/library/socket.html)

# Future Work

* There is a strange bug where the try catch statement broke at some point. It suddenly was unable to handle a client disconnecting from the system. This is the largest change to make to the current iteration.
* The way that the current setup works is clunky, using the terminal. I would like to branch into two paths: A nicer terminal application that is more robust, and a version with a GUI.
* Saving what the user's have communicated in the past would be an oprtion, that way one could log what was said, or opt out.
