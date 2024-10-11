bits 32


global start        

extern exit
import exit msvcrt.dll


segment data use32 class=data
a resb 1
b resb 1
c resb 1
d resb 1

segment code use32 class=code
    start:
        mov byte [a],3
        mov byte [b],4
        mov byte [c],1
        mov byte [d],2
        
        
        mov EAX,0
        mov al,[a]
        add byte al,[b]
        add byte al,[d]
        sub byte al,[c]
        
        mov dl,[d]
        sub byte [a],dl
        
        sub byte al,[a]
        

        push    dword 0 
        call    [exit] 
