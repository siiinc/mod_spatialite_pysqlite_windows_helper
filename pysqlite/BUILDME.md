* get pysqlite from https://github.com/ghaering/pysqlite.git
* %vcvarsall% amd64
* build %cd%\..\sqlite-amalgamation-3080802 using details in sqlite-amalgamation-3080802\README.md
* copy sqlite3.lib to %cd%\..\..\Python27\libs
* copy sqlite3.dll to %cd%\..\..\Python27\DLLs
* copy sqlite3.h to %cd%\..\..\Python27\include
* get spatialite runtime http://www.gaia-gis.it/gaia-sins/windows-bin-amd64 and copy mod_spatialite dlls to %cd%\..\..\Python27\DLLs
* set path=%cd%\..\..\Python27\;%cd%\..\..\Python27\Python27\DLLs;%path%
* python setup.py install
* copy build\lib.win-amd64-2.7\pysqlite2\dbapi2.py to %cd%\..\..\Python27\Lib\sqlite3
* copy build\lib.win-amd64-2.7\pysqlite2\_sqlite.pyd to %cd%\..\..\Python27\DLLs
