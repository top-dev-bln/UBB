cmake_minimum_required(VERSION 3.30)
project(Lab2 C)

set(CMAKE_C_STANDARD 11)

add_executable(Lab2 main.c
        ui.c
        masina.c
        masina.h
        ui.h
        service.c
        repo.c
        tests.c
        repo.h
        service.h
        tests.h)
