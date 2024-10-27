bits 32

global start        


extern exit
import exit msvcrt.dll

segment data use32 class=data

 a db 2
 b db 2
 c db 4
 d dd 7
 e dq 6
 

segment code use32 class=code
    start:
    ;   2/(a+b*c-9)+e-d
    mov al, [b]
    mul byte [c] ; AX = b*c
    
    mov bl, [a]
    
    mov bh, 0
    add bx,ax
    
    sub bx, 9 ; bx = (a+b*c-9)
    
    mov eax, 2
    mov dx,0
    div bx ; ax = 2/ paranteza
    

    
    mov edx,0
    add eax, [e]
    adc edx, [e+4]
    
    sub eax, [d]
    sbb edx , 0
    
    
    
    

        push    dword 0
        call    [exit] 
