@echo off
set /p archive="Quale archivio vuoi decriptare?"
MakePack.exe --extract %archive%
pause