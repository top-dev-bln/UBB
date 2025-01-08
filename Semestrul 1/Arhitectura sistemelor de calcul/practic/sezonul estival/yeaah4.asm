bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    mesaj db "<%d>*<%d>=<%d>",0
    format db "%d",0
    a dw 0
    b dw 0


segment code use32 class=code

    start:
        lea eax, [a]
        push eax
        push dword format
        call [scanf]
        add esp ,4*2
        
        lea eax, [b]
        push eax
        push dword format
        call [scanf]
        add esp, 4*2
        
        mov ax, [a]
        mov bx, [b]
        
        imul bx
        
        push dx
        push ax
        mov ax,[b]
        cwde
        push eax
        mov ax,[a]
        cwde
        push eax

        push mesaj
        call [printf]
        add esp, 4*5
        
    
        push    dword 0
        call    [exit]