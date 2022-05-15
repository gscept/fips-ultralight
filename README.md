# fips-ultralight

fipsified ultralight (https://github.com/ultralight-ux/Ultralight)

fips build system: https://github.com/floooh/fips

Minimal package that will download a binary release from ultralight-ux, unpack and place the headers, libraries and shared files into the fips deploy folder. 

It declares a ultralight cmake interface library that can be added to the dependencies. 

To install call 

`fips ultralight`

from your main project that has a dependency in its `fips.yml`.

For the automatic unpacking to work you will need to install py7zr (https://github.com/miurahr/py7zr) e.g. via
`pip install py7zr`
