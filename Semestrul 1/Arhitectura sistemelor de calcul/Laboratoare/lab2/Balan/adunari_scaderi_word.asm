bits 32


global start        

extern exit
import exit msvcrt.dll


segment data use32 class=data
a resw 1
b resw 1
c resw 1
d resw 1

segment code use32 class=code
    start:
        mov word [a],3
        mov word [b],4
        mov word [c],1
        mov word [d],2
        
        
        mov EAX,0   ;(a+a-c)-(b+b+d)
        
                
        mov AX,[b]
        add AX,[b]
        add AX,[d]
        
        mov DX,AX
        mov AX,0
        
        mov AX,[a]
        add AX,[a]
        sub AX,[c]
        
        SUB AX,DX

        
        
        
        
        

        push    dword 0 
        call    [exit] 
