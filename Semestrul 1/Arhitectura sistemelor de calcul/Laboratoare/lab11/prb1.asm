bits 32
global start        

extern exit, printf, permutari
import exit msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    numar dd 1193746
    len equ 6
    format db "%x",10,0
    formatz db "%d",10,0
    zece equ 10


segment code use32 class=code 
    start:
    

              
        push dword [numar]
        push dword format
        call [printf]
        add esp , 8
        
        push dword formatz
        push dword len
        push dword [numar]
        call permutari
        add esp,8
        
        
        push    dword 0
        call    [exit]
