##Dumping the strings
```sh
$ strings elfie.bin | grep -i python
Error loading Python DLL: %s (error code %d)
Error detected starting Python VM.
PYTHONHOME
PYTHONPATH
Cannot GetProcAddress for Py_SetPythonHome
Py_SetPythonHome
bpython27.dll
bpyside-python2.7.dll
bshiboken-python2.7.dll
python27.dll
```
The python27.dll is used, so use pyinstxtractor.py to get the python source from executable
##Get the source from executable
```sh
$ python2.7 pyinstxtractor.py elfie.bin
[*] Processing elfie.bin
[*] Pyinstaller version: 2.1+
[*] Python version: 27
[*] Length of package: 12034944 bytes
[*] Found 26 files in CArchive
[*] Begining extraction...please standby
[*] Found 244 files in PYZ archive
[*] Successfully extracted pyinstaller archive: elfie.bin

You can now use a python decompiler on the pyc files within the extracted directory

$ ls -l elfie.bin_extracted/ | awk {'print $9'}
bz2.pyd
elfie
elfie.exe.manifest
_hashlib.pyd
Microsoft.VC90.CRT.manifest
msvcm90.dll
msvcp90.dll
msvcr90.dll
out00-PYZ.pyz
out00-PYZ.pyz_extracted
pyi_archive
_pyi_bootstrap
pyi_carchive
pyi_importers
pyi_os_path
pyside-python2.7.dll
PySide.QtCore.pyd
PySide.QtGui.pyd
python27.dll
QtCore4.dll
QtGui4.dll
select.pyd
shiboken-python2.7.dll
_socket.pyd
_ssl.pyd
struct
unicodedata.pyd
```
One of the extracted file is elfie. Elfie is deobfuscating the python script. It contains the 56k lines of obfuscated source.
```py
...
O0O0OO0OO0O0OOO0O0OOO00O0OOOOO00 += 'G9mNm9nanRJMXQzaCtjbmhROENVZDE'
O0O0OO0OO0O0OOO0O0OOO00O0OOOOO00 += '0RTcxMnFYRlhMNDN1VWJRVHZ6cDJKUHdOU2FZbS8'
O0O0OO0OO0O0OOO0O0OOO00O0OOOOO00 += 'vcm9Y'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'ZmhvM'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'Ho1cFZ5Q2t0dHlYdGsrMENNTU0rWlpTQ3pMSkxTeCszSnF5QW'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += '1MMlJXVDBrT1JLWUhpZFM2VWRDeDQ0aHc0N'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'UZMZGpPTFpwdUNxY1pMNGhaTmluMzY5QnBWSHFpMUpkS0RoQ2Z4V3FCQUd'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'WUkszbmF6VStFR2tScEpFK1FMbzRUQzloNlFMZWNkT2'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'RabTBrZE'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'VXWFY3QUtiTXFXQVYrenh4amxJZXI5MXd1YWJiWkRaWDRQV0'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'xDUmhGcnRDcnd4VkF5'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'aTBTMXd3OC8yY0ZqdzBIU0JMT0tEcktGckJUTkpvRGw2d'
O00OO00OOO0OOOO0OOOO0OO00000OOO0 += 'nNocTB'
import base64
exec(base64.b64decode(OOO0OOOOOOOO0000O000O00O0OOOO00O + O0O00OO0OO00OO00OO00O000OOO0O000 + O00OO0000OO0OO0OOO00O00000OO0OO0 + O00OO00000O0OOO0OO0O0O0OO0OOO0O0 + O0O00OO0O0O0O00OOO0OOOOOO00OO0O0 + O0OO00O0000OOOO00OOO0OO0000O0OO0 + O0O0OO000OOO00000OO0OOOO0OO00000 + OO0OOO0O00000O00OOOOO0OO0OO00OOO + O000000000OOO00OO00000OOOO00OOOO + OOO0OOO00O0OO0O0OOOO00OO00OO0O00 + O0OO0OOO00O0OOO0O00OOO0O0OOOO00O + OOOO000O0OOOOO0O0O0000O0O0OO00O0 + O00O0O00OO0O0OO00O0OO0O00O0O00OO + OOOOOOO0O0O00OOO0OO00O0O00OOOOO0 + O00O000O0O00000O00OO0OO0OOO000O0 + O0O000O0O0O0OO0000O0O0OOO0OOOOO0 + O000000OOO0O00OO00OO00OO0OO00O0O + OOOOOO000OOO0O000O0O00OO0OOOO0O0 + O00OOOO0OO0O000OO0OOOOO0OOOO0000 + O0OO00000OOOOO0OOO000O00000OOO00 + OOO00O0OOOOO00OO0OOOOO0O0O00O0O0 + OOO000O0OOO0OOO0OOOO0OOOOO0O0O00 + OO0OOOO0O00OOOO0OOOO0O0OOO0OO0O0 + O0OO0OO00000OOOO0OOOOO0O00O0O0O0 + OO00OOO00OO0OOO000O000000O0O0000 + OO0O0000OO0000OO000OO0O0OO0O00OO + OO00000O0OO000O0O000OOOOOOO0O0OO + O0O00O000OOOO000O0OOOOO0O000000O + O000OOOOOOOOOO0O0OO0OO000OO000O0 + O0OO00OOO0O0OOOO0O0O0000000O0OOO + O0000O0OOOO00OO0OOO00OO000O0000O + OOOOO0OO0O00OOOOOO00O00000O0OO0O + OO0O0OOOO0O000OOOO00O0O00O0O0O0O + O0OOO00OOOO0OO0OO0O000O0OO0OO000 + O0OOOO0O00OOOOO0OOO000O00O00OO00 + OO0OO00000O00O0000000O00O0OO0O00 + OOO0000OO00000OO00O0OO0000OOOO00 + O00O000O00O0O00OO0OO0O000000OOOO + O000O00O000O00O000O0OO00O0000O0O + O0O0OO0OO0O0OOO0O0OOO00O0OOOOO00 + O0OOO0OO00OO0OOO00OO0O0O0O0O00OO + OO0OOO00000OO000O0OOOO00O0O0O00O + O00OO00OOO0OOOO0OOOO0OO00000OOO0 + OOOOOO0OO0O0OO0O0000OOO0O00O0O0O + O0O0O00O0000O00OOOO000O00OO00O00 + OOOOO0000OO000O0O0000OOOOO0000OO + OO00OOO0O00OO0OO0OOOO000OO0000OO + O00000O0OO00O0OO00000O000OOO00O0 + O0OOO00O0O0O0OO00000OO0OO00O00OO + O0000OO00000000OO000O0OOO000OO00 + OO0OO0O00000O0O000OOO0O0O0O000O0 + OOOOO0O00OOOOO0O0OOOOOOO0OO0OO00 + OOOOO00O0O0O0O0O0OO00O0OOOO00O0O + O0OOOO0OO000OOOOOO0O0OO0OOO0O000 + OOOO000OOOOO00000O000OO0O00O0O0O + O00OOO000O0O0OOOO00O0O00O0OO00OO + OO0O00OO0OO00O0O000O0000O0OOOOO0 + OO0O0O00OO00OOOOOO0O0O0OOO0OOO0O + OO0OOO00OOO00OOOOOOOOOOOO00OO00O + OOO0000O0OO0OOOOO000O00O0OO0O00O + OOO0O00O00OOOOOOO00OOOO0000O0O00 + O0O00OO00O0O00O0O00O0OOO00O0O0OO + O00OOOOO000O00O0O00000OOO0000OOO + O0O0OOO000O000OO0O0O0OOOOO0OO000))
```
##Changing the 'exec' to 'print' and dump the code
```sh
$ python2.7 elfie.py > new_elfie.py
```
##The email is found
```py
def O000OOOOOO0OOOO00000OO0O0O000OO0(self):
    O0O0O0000OOO000O00000OOO000OO000 = getattr(self, 'txeTnialPot'[::-1])()
    if (O0O0O0000OOO000O00000OOO000OO000 == ''.join((OO00O00OOOO00OO000O00OO0OOOO0000 for OO00O00OOOO00OO000O00OO0OOOO0000 in reversed('moc.no-eralf@OOOOY.sev0000L.eiflE')))):
        self.OO0O0O0O0OO0OO00000OO00O0O0000O0.setWindowTitle('!sseccus taerg'[::-1])
        self.OOOOOOOOOO0O0OOOOO000OO000OO0O00 = True
        self.OO0O0O0O0OO0OO00000OO00O0O0000O0.setVisible(False)
        self.OO0O0O0O0OO0OO00000OO00O0O0000O0.setVisible(True)
```
Email: Elfie.L0000ves.YOOOO@flare-on.com
## Got message
Very good. I am most pleased with your progress. Attached is the next challenge and the password to the zip archive is "flare" again.

Despite what they say about you, I think you're doing great.

Always be sure to run the challenge on the command line to confirm that it is actually doing what you think it's doing.

-FLARE

