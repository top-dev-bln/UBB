bits 32
global start        

extern exit,fopen,fread,fclose
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data

    nume_fisier db "textul.txt",0
    mod_acces db "r",0
    
    vocale db "bcdfghjklmnpqrstvwxyz",0
    
    descriptor dd -1
    len equ 100
    text times len db 0
    
    


segment code use32 class=code
    start:
    
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp,4*2
        
        mov [descriptor], eax
        
        cmp eax,0
        je final
        
        push dword [descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov esi , dword text
        
        
        mov ecx,len
        mov ebx,0
        jecxz final
        
        next_car:
        
            mov edi , dword vocale
            lodsb;al caracter din text
            
            push ecx
            mov ecx,21
            check:
                scasb
                je gasit
            loop check
            
            
            jmp continua
            
            gasit:
                inc ebx
            
            
            
            
            continua:
            pop ecx
        loop next_car
        
        
        
        
        
        
        
        
        
        
        
        
        
        push dword [descriptor]
        call [fclose]
        add esp,4
        
        final:


        push    dword 0
        call    [exit]
