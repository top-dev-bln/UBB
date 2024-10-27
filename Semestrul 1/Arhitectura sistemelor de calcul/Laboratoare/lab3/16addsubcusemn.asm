bits 32

global start        


extern exit
import exit msvcrt.dll

segment data use32 class=data

 a db 1
 b dw 2
 c dd 8
 d dq 4
 

segment code use32 class=code
    start:

    ;(d-a)-(a-c)-d
    
    mov ebx, [d]
    mov ecx, [d+4] ; ecx:ebx = d
    
    mov al , [a]
    cbw; ax=a
    cwde;
    cdq; EDX:EAX = a
    sub ebx,eax
    sbb ecx,edx;ecx:ebx = d-a
    
    ;eax=a
    sub eax,[c]
    cdq ; EDX:EAX = a-c
    
    sub ebx,eax
    sbb ecx,edx ; ECX:EBX = (d-a) - (a-c)
    
    mov eax, [d]
    mov edx, [d+4]
    
    sub ebx,eax
    sbb ecx,edx
    
    
    
    
    
    
    
    
    
    
    
    
    

        push    dword 0
        call    [exit] 
