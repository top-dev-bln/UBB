bits 32
global start        

extern exit, scanf ,printf
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    n dd 0
    m dd 0
    a dd 0
    format db "%d",0
    

segment code use32 class=code
    start:
    
        push dword n
        push format
        call [scanf]
        add esp, 4*2
        
        push dword m
        push format
        call [scanf]
        add esp, 4*2
        
        push dword a
        push format
        call [scanf]
        add esp, 4*2
        
        
       
        mov eax, [a]
        
        mov ecx, 16
        sub ecx, [m]
        
        shl ax, cl
        
        mov ecx,16
        sub ecx,14
        add ecx,[n]
        
        shr ax, cl
        
        
        
        
        push eax
        push format
        call [printf]
        
        
        
  
        
        
        


        push    dword 0
        call    [exit]
