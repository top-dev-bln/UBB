bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    rezultat dd 0
    format db "%d",0
    a dd 0 
    b dd 0
    

segment code use32 class=code
    start:
    
        push dword a
        push format
        call [scanf]
        add esp, 4*1
        
        push dword b
        push format
        call [scanf]
        add esp, 4*1
        
        mov eax, [a]
        mov ebx, [a]
        add eax, [b]
        sub ebx, [b]
        
        cdq
        idiv ebx
        
        mov [rezultat] ,eax
        
        
        
        
        
        
        
        
        push eax
        push format
        call [printf]
        add esp, 4*2
    
    
    


        push    dword 0
        call    [exit]
