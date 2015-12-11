SET(SRC_LIST main.c)
INCLUDE_DIRECTORIES(/tmp/test/include/hello)
LINK_DIRECTORIES(/tmp/test/lib)
ADD_EXECUTABLE(main ${SRC_LIST})
TARGET_LINK_LIBRARIES(main hello)

