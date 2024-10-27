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
    ;(b+b)+(c-a)+d
    mov ax, [b]
    add ax, ax
    mov edx , 0
    mov dx ,ax;  edx = b+b
    mov eax , [c]
    mov ebx, 0
    mov bl, [a]
    sub eax, ebx  ; eax = c-a
    add eax, edx
    mov edx,0
    add eax, [d]
    adc edx, [d+4]
    

    
    
    
    
    
    
    

        push    dword 0
        call    [exit] 
