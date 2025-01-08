bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    a dd 0
    b dd 0
    mesaj db "%x",0
    format db "%d",0

segment code use32 class=code

    start:
    
        push dword a
        push dword format
        call [scanf]
        add esp ,4*2
        
        push dword b
        push dword format
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        mov ebx, [b]
        
        add eax,ebx 
        
        ; eax = a+b
        push eax
        pop ax
        pop dx
        
        mov bx, 2
        idiv bx
        
        ;ax = a+b/2
        
        cwde
        
        
        
        push eax
        push mesaj
        call [printf]
        add esp, 4*4
        
    
        push    dword 0
        call    [exit]