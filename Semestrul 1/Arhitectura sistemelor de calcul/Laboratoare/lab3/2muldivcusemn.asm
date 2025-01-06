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
    mov BX, AX   ; BX = b*c
    
    mov al, [a]
    cbw
    
    add bx,ax
    
    sub bx, 9 ; bx = (a+b*c-9)
    
    
    
    
    mov eax, 2
    mov dx,0
    idiv bx ; ax = 2 / paranteza

    cwde ; eax = 2 / paranteza
    sub eax, [d]

    cdq ; edx:eax = 2 / paranteza - d
    add eax, [e]
    adc edx, [e+4]


    

    

        push    dword 0
        call    [exit] 
