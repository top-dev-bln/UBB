cmake_minimum_required(VERSION 3.30)
project(lab5neb C)

set(CMAKE_C_STANDARD 11)

add_executable(lab5neb main.c oferta.c controller.c repo.c tests.c ui.c)
