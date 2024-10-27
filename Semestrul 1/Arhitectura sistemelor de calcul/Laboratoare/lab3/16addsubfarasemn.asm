bits 32

global start        


extern exit
import exit msvcrt.dll

segment data use32 class=data

 a db 2
 b dw 1
 c dd 4
 d dq 8
 

segment code use32 class=code
    start:

    ;c-a-(b+a)+c = c+c-a-a-b
    
    mov eax, [c]
    add eax, eax
    mov ebx,0
    mov bl, [a] 
    sub eax, ebx
    sub eax, ebx
    mov edx,0
    mov dx, [b]
    sub eax,edx
    
    
    
    
    
    
    
    
    
    
    

        push    dword 0
        call    [exit] 
