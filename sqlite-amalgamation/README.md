##Steps to Remember

1) Get the src from http://www.sqlite.org/download.html such as http://www.sqlite.org/2015/sqlite-amalgamation-3080802.zip

2) Copy the files from the zip into this `sqlite-amalgamation` directory

3) Get the def file from the archive http://www.sqlite.org/2015/sqlite-dll-win32-x86-3080802.zip and copy it into this `sqlite-amalgamation` directory

4) open cmd prompt run `vcvarsall amd64`

5) go to this `sqlite-amalgamation` directory (contains the .c, .h and .def file) and run `msbuild sqlite3_dll.vcxproj /t:Build /p:Configuration=Release`
