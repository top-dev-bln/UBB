;Dandu-se un sir de octeti si un subsir al sau, sa se elimine din primul sir toate aparitiile subsirului.

bits 32
global start

extern exit
import exit msvcrt.dll


segment data use32 class=data
sir db  12h,11h,41h, 23h, 0ah, 29h , 12h, 1Ah, 13h
len_sir equ $-sir
sub_sir db 12h, 1Ah, 13h
len_sub equ $-sub_sir


segment code use32 class=code
    start:
    
    mov ecx, len_sir
    mov esi, sir
    mov edi, sub_sir
    mov ebx,0

    repeta:
    
        cmpsb
        jne not_egal

        
        inc bl
        cmp bl, len_sub
        jne continue
        push ecx
        mov ecx , len_sub

        remove:
        mov edx, esi
        sub edx, ecx
        mov byte [edx], 0
        loop remove
        
        
        pop ecx
        
        
        
      
        
        not_egal:
        mov edi, sub_sir
        mov bl,0
        continue:

    loop repeta
    
    
    

    
    
 


    push    dword 0
    call    [exit]