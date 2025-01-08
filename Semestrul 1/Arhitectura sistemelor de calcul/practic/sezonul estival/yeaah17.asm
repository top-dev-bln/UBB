bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    n dd 0
    mesaj db "%x",0
    format db "%d",0

segment code use32 class=code

    start:
    
        push dword n
        push dword format
        call [scanf]
        add esp ,4*2
        

        
 

        
        
        push dword [n]
        push mesaj
        call [printf]
        add esp, 4*2
        
    
        push    dword 0
        call    [exit]