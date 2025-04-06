cmake_minimum_required(VERSION 3.30)
project(Lab5 C)

set(CMAKE_C_STANDARD 11)

add_executable(Lab5 main.c controller.c repo.c tests.c ui.c validator.c oferta.c oferta.h controller.h repo.h tests.h ui.h validator.h)
