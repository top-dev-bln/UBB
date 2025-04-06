cmake_minimum_required(VERSION 3.28.3)
project(LAB5SPERANTA C)

set(CMAKE_C_STANDARD 11)

# Activează opțiunile de coverage pentru testare
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-arcs -ftest-coverage")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")

# Asigură-te că folosești opțiunile corecte pentru MinGW (pentru Windows)
if(MINGW)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -D_CRT_SECURE_NO_WARNINGS")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_CRT_SECURE_NO_WARNINGS")
endif()

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Werror")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Werror")

add_executable(LAB5SPERANTA main.c ui.c controller.c oferta.c repo.c tests.c )
