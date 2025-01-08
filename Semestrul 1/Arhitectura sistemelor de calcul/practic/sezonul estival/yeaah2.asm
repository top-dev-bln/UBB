bits 32
global start


extern exit, scanf
import exit msvcrt.dll
import scanf msvcrt.dll


segment data use32 class=data

    a dd 0
    b dd 0
    rezultat dw 0
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
        
        cdq ; edx:eax = a
        
        idiv ebx ; eax = catul , edx = restul
        mov [rezultat], eax
        
    
        push    dword 0
        call    [exit]