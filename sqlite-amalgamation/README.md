##Steps to Remember

1) Get the src from http://www.sqlite.org/download.html such as http://www.sqlite.org/2015/sqlite-amalgamation-3080802.zip
2) Get the binary dll just so that we can get the def file http://www.sqlite.org/2015/sqlite-dll-win32-x86-3080802.zip
3) open cmd prompt run `vcvarsall amd64`
4) go to the src dir that contains the .c, .h and .def file and run `msbuild sqlite3_dll.vcxproj /t:Build /p:Configuration=Release`
