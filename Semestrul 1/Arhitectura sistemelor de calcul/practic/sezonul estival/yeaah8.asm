bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data

    format db "%d",0
    a dd 89
    b dd 0
    

segment code use32 class=code
    start:
    

        
        push dword b
        push format
        call [scanf]
        add esp, 4*1
        
        mov eax, [a]
        cdq; edx:eax = a
        
        mov ebx, [b]
        idiv ebx ; eax = a/b
        
        add eax, [a]
        
        
        
        
        

        
        
        push eax
        push format
        call [printf]
        add esp, 4*2
    
    
    


        push    dword 0
        call    [exit]
