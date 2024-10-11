bits 32
global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data ;[(a*b)-d]/(b+c)
a db 3
b db 4
c db 1
d dw 2
segment code use32 class=code
    start:
    

        push    dword 0
        call    [exit]

        