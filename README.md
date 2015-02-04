These steps are primarily for windows...
1) Get a clean Python27 or use your existing one just be aware that this may have unintended consequences
2) Follow steps in pysqlite\BUILDME.md noting that the paths may be different depending on where your python27 is located
3) When running make sure that the python that has the rebuild pysqlite and mod_spatialite runtime is on the path and the that the DLLs dir is on the path
