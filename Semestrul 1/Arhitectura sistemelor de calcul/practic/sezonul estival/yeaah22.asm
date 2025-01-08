bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    format db "%lld",0
    form db "%d",0

    
    a dd 0
    b dd 0
    k dd 17


segment code use32 class=code

    start:
    
        push dword a
        push dword form
        call [scanf]
        add esp ,4*2
        
        push dword b
        push dword form
        call [scanf]
        add esp ,4*2
        
        mov eax, [a] 
        add eax, [b]
        
        mov ebx, [k]
        mul ebx
        
        
         
        
        push edx
        push eax
        push dword format
        call [printf]
        add esp, 4*3
        
  
        push    dword 0
        call    [exit]
        
        