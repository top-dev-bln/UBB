bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    mess db "a = %d (baza 10), a = %x (baza 16)",0
    a dd -89

    

segment code use32 class=code
    start:
    
 
        
        
        push dword [a]
        push dword [a]
        push mess
        call [printf]
        add esp, 4*2
    
    
    


        push    dword 0
        call    [exit]
