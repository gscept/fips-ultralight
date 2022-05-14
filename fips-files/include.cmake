add_library(ultralight INTERFACE)
target_include_directories(ultralight INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/../fips-deploy/ultralight/include)
target_link_directories(ultralight INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/../fips-deploy/ultralight/lib)
target_link_libraries(ultralight INTERFACE AppCore Ultralight UltralightCore WebCore)