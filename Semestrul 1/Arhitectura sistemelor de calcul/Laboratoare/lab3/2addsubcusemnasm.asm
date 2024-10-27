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

    ;(c+b)-a-(d+d)
    
    mov ebx,[c] ; EBX= c
    mov ax, [b]
    cwde ; EAX = b
    
    add ebx, eax ; EBX = (c+b)
    
    mov al, [a]
    cbw ; AX = a
    cwde; EAX = a
    
    sub ebx, eax;ebx = (c+b)-a
    mov eax,ebx
    
    cdq ; EDX:EAX = (c+b)-a
    

    mov ebx, [d]
    mov ecx, [d+4]; ecx:ebx = d
    
    sub eax,ebx
    sbb edx,ecx
    
    sub eax,ebx
    sbb edx,ecx
    

    
    
    
    
    
    
    
    

        push    dword 0
        call    [exit] 
