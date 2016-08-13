##Logic of program:

```asm
.text:0040104B                 xor     ecx, ecx
.text:0040104D
.text:0040104D loc_40104D:                             ; CODE XREF: start+61j
.text:0040104D                 mov     al, byte_402158[ecx]
.text:00401053                 xor     al, 7Dh
.text:00401055                 cmp     al, byte_402140[ecx]
.text:0040105B                 jnz     short loc_40107B
.text:0040105D                 inc     ecx
.text:0040105E                 cmp     ecx, 18h
.text:00401061                 jl      short loc_40104D
.text:00401063                 push    0               ; lpOverlapped
.text:00401065                 lea     eax, [ebp+NumberOfBytesWritten]
.text:00401068                 push    eax             ; lpNumberOfBytesWritten
.text:00401069                 push    12h             ; nNumberOfBytesToWrite
.text:0040106B                 push    offset aYouAreSuccess ; "You are success\r\n"
.text:00401070                 push    [ebp+hFile]     ; hFile
.text:00401073                 call    WriteFile
```

##Array of byte_402140:

```asm
.data:00402140 byte_402140     db  1Fh                 ; DATA XREF: start+55r
.data:00402141                 db    8
.data:00402142                 db  13h
.data:00402143                 db  13h
.data:00402144                 db    4
.data:00402145                 db  22h ; "
.data:00402146                 db  0Eh
.data:00402147                 db  11h
.data:00402148                 db  4Dh ; M
.data:00402149                 db  0Dh
.data:0040214A                 db  18h
.data:0040214B                 db  3Dh ; =
.data:0040214C                 db  1Bh
.data:0040214D                 db  11h
.data:0040214E                 db  1Ch
.data:0040214F                 db  0Fh
.data:00402150                 db  18h
.data:00402151                 db  50h ; P
.data:00402152                 db  12h
.data:00402153                 db  13h
.data:00402154                 db  53h ; S
.data:00402155                 db  1Eh
.data:00402156                 db  12h
.data:00402157                 db  10h
```
