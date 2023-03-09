#!/usr/bin/python3
import os
stdout_fd = os.dup(1)
os.write(stdout_fd, "#pythoniscool\n".encode())
os.close(stdout_fd)
