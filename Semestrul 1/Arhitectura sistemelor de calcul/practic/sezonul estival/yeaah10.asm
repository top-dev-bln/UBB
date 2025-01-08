bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    format db "%d",0
    mess db "%x",0
    n dd 0 

    

segment code use32 class=code
    start:
    
        push dword n
        push format
        call [scanf]
        add esp, 4*1
        
        
        
        push dword [n]
        push mess
        call [printf]
        add esp, 4*2
    
    
    


        push    dword 0
        call    [exit]
