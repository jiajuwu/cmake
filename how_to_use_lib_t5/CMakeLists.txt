CMAKE_MINIMUM_REQUIRED( VERSION 2.8.3 )
PROJECT(newhello)
ADD_SUBDIRECTORY(src)
MESSAGE(STATUS “HOME dir: $ENV{HOME}”)
MESSAGE(STATUS “CMAKE_CURRENT_LIST_FILE: ${CMAKE_CURRENT_LIST_FILE}”)
ADD_TEST(main ${PROJECT_BINARY_DIR}/src/main)
ENABLE_TESTING()
