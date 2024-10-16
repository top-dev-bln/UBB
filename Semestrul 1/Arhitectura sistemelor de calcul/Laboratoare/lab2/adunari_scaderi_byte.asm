bits 32


global start        

extern exit
import exit msvcrt.dll


segment data use32 class=data
a db 3
b db 4
c db 1
d db 2

segment code use32 class=code
    start:

        mov EAX,0
        mov al,[a]
        add al,[b]
        add al,[d]
        sub al,[c]
        
        mov dl,[d]
        sub byte [a],dl
        
        sub al,[a]
        

        push    dword 0 
        call    [exit] 
