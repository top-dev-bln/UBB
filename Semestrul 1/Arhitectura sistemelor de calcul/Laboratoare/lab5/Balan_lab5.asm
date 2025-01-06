bits 32
global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data

    S1 db 1, 3, 6, 2, 3, 7
    S2 db 6, 3, 8, 1, 2, 5
    l equ $-S2 
    d times l db 0
    
segment code use32 class=code
    start:
    
    mov esi, S1
    mov edi, S2
    
    cld
    
    mov ecx, l
    
    
    repeta:
        jecxz stop ; il bag aici ca sa am si conditie de oprire , fiindca nu influenteaza cand verifica daca ecx-ul e 0 la inceput
        cmpsb
        ja mai_mare
        
        push edi
        mov al,[edi-1]
        mov edi,d
        add edi,l
        sub edi,ecx
        stosb
        pop edi
        dec ecx
        jmp repeta
        
    
    
    jmp stop
    
    mai_mare:
    
        push edi
        mov al,[esi-1]
        
        mov edi,d
        add edi,l
        sub edi,ecx
        stosb
        pop edi
        dec ecx
        jmp repeta

    stop:

        push    dword 0
        call    [exit]
