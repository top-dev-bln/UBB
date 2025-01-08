bits 32
global start        

extern exit,fopen,fread,fclose, printf
import exit msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data

    nume_fisier db "textul.txt",0
    mod_acces db "r",0
    cifre times 10 db 0
    
    
    
    descriptor dd -1
    len equ 100
    text times len db 0
    
    format db "%d apare de %d ori",0    
    


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
        
        
        mov ecx,eax
        mov ebx,0
        jecxz final
        
        next_car:
        
            mov eax,0
            lodsb;al caracter din text
            
            

            sub al,'0'
            
            cmp al, 9
            ja continua
            
            mov edi, cifre
            add edi, eax
            

            inc byte [edi]
            

         
            continua:
            
        loop next_car
        
        
        ;acum ca avem vector de frecventa trecem prin el sa cautam maximul
        mov ebx,0
        mov edx,0

        mov esi, cifre
        mov ecx,10
        
        passing:
        
        lodsb; in al avem
        cmp al,bl
        jbe skip
        mov bl,al
        mov dl,10
        sub dl,cl
        
        
        
        skip:
        loop passing
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        pushad
        
        
        push dword [descriptor]
        call [fclose]
        add esp,4
        
        
        
        popad
        push ebx
        push edx
        push dword format
        call [printf]
    
        final:
        


        push    dword 0
        call    [exit]
