##The logic of the program is contained in sub_401084 function
```asm
.text:00401084 sub_401084      proc near               ; CODE XREF: sub_401000+5Fp
.text:00401084
.text:00401084 var_C           = byte ptr -0Ch
.text:00401084 arg_0           = dword ptr  8          ; cypher text
.text:00401084 arg_4           = dword ptr  0Ch        ; input
.text:00401084 arg_8           = dword ptr  10h        ; size
.text:00401084
.text:00401084                 push    ebp
.text:00401085                 mov     ebp, esp
.text:00401087                 sub     esp, 0
.text:0040108A                 push    edi
.text:0040108B                 push    esi
.text:0040108C                 xor     ebx, ebx
.text:0040108E                 mov     ecx, 25h
.text:00401093                 cmp     [ebp+arg_8], ecx
.text:00401096
.text:00401096 loc_401096:
.text:00401096                 jl      short loc_4010D7
.text:00401098                 mov     esi, [ebp+arg_4]
.text:0040109B                 mov     edi, [ebp+arg_0]
.text:0040109E                 lea     edi, [edi+ecx-1]
.text:004010A2
.text:004010A2 loc_4010A2:                             ; CODE XREF: sub_401084+4Fj
.text:004010A2                 mov     dx, bx
.text:004010A5                 and     dx, 3
.text:004010A9                 mov     ax, 1C7h
.text:004010AD                 push    eax
.text:004010AE                 sahf
.text:004010AF                 lodsb
.text:004010B0                 pushf
.text:004010B1                 xor     al, [esp+10h+var_C]
.text:004010B5                 xchg    cl, dl
.text:004010B7                 rol     ah, cl
.text:004010B9                 popf
.text:004010BA                 adc     al, ah
.text:004010BC                 xchg    cl, dl
.text:004010BE                 xor     edx, edx
.text:004010C0                 and     eax, 0FFh
.text:004010C5                 add     bx, ax
.text:004010C8                 scasb
.text:004010C9                 cmovnz  cx, dx
.text:004010CD                 pop     eax
.text:004010CE                 jecxz   short loc_4010D7
.text:004010D0                 sub     edi, 2
.text:004010D3                 loop    loc_4010A2
.text:004010D5                 jmp     short loc_4010D9
.text:004010D7 ; ---------------------------------------------------------------------------
.text:004010D7
.text:004010D7 loc_4010D7:                             ; CODE XREF: sub_401084:loc_401096j
.text:004010D7                                         ; sub_401084+4Aj
.text:004010D7                 xor     eax, eax
.text:004010D9
.text:004010D9 loc_4010D9:                             ; CODE XREF: sub_401084+51j
.text:004010D9                 pop     esi
.text:004010DA                 pop     edi
.text:004010DB                 mov     esp, ebp
.text:004010DD                 pop     ebp
.text:004010DE                 retn
.text:004010DE sub_401084      endp
.text:004010DE
```
##The array of the cypher email
```asm
.text:004010E4                 db 0AFh
.text:004010E5                 db 0AAh
.text:004010E6                 db 0ADh
.text:004010E7                 db 0EBh
.text:004010E8                 db 0AEh ; «
.text:004010E9                 db 0AAh ; ¬
.text:004010EA                 db 0ECh ; ∞
.text:004010EB                 db 0A4h ; ñ
.text:004010EC                 db 0BAh ; ║
.text:004010ED                 db 0AFh ; »
.text:004010EE                 db 0AEh ; «
.text:004010EF                 db 0AAh ; ¬
.text:004010F0                 db  8Ah ; è
.text:004010F1                 db 0C0h ; └
.text:004010F2                 db 0A7h ; º
.text:004010F3                 db 0B0h ; ░
.text:004010F4                 db 0BCh ; ╝
.text:004010F5                 db  9Ah ; Ü
.text:004010F6                 db 0BAh ; ║
.text:004010F7                 db 0A5h ; Ñ
.text:004010F8                 db 0A5h ; Ñ
.text:004010F9                 db 0BAh ; ║
.text:004010FA                 db 0AFh ; »
.text:004010FB                 db 0B8h ; ╕
.text:004010FC                 db  9Dh ; ¥
.text:004010FD                 db 0B8h ; ╕
.text:004010FE                 db 0F9h ; ∙
.text:004010FF                 db 0AEh ; «
.text:00401100                 db  9Dh ; ¥
.text:00401101                 db 0ABh ; ½
.text:00401102                 db 0B4h ; ┤
.text:00401103                 db 0BCh ; ╝
.text:00401104                 db 0B6h ; ╢
.text:00401105                 db 0B3h ; │
.text:00401106                 db  90h ; É
.text:00401107                 db  9Ah ; Ü
.text:00401108                 db 0A8h ; ¿
```
##After using a solver.py script got the email
Email: a_Little_b1t_harder_plez@flare-on.com
##Got a message
Great job, you're really knocking these out! Here's the next binary for your goaty enjoyment. The password to the zip archive is "flare" again.

Keep up the good work, and good luck!

-FLARE
