cmake_minimum_required(VERSION 3.30)
project(Lab6)

set(CMAKE_CXX_STANDARD 20)


add_compile_options(-Wall -Wextra -Wpedantic)



add_executable(Lab6 main.cpp
        ui.cpp
        ui.h
        tests.cpp
        tests.h
        oferta.cpp
        oferta.h
        service.cpp
        service.h
        repository.cpp
        validator.cpp
        validator.h
)