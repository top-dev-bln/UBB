cmake_minimum_required(VERSION 3.30)
project(Lab3 C)

set(CMAKE_C_STANDARD 11)


set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=address")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fsanitize=address")


add_executable(Lab3 main.c ui.c service.c repo.c masina.c tests.c)