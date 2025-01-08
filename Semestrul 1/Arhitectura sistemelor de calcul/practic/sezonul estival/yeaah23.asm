bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    
    form db "%x",0
    format db "%d",10,0
    n dd 0


segment code use32 class=code

    start:
    
        push dword n
        push dword form
        call [scanf]
        add esp ,4*2
        
        
        push dword [n]
        push dword format
        call [printf]
        add esp, 4*2
        
        mov eax, [n]
        neg eax
        
        mov edx,0
        mov dl, al
        neg edx
        
        
        push edx
        push dword format
        call [printf]
        
  
        push    dword 0
        call    [exit]
        
        