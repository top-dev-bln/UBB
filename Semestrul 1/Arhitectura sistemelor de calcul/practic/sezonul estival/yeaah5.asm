bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data
    mesaj db "Cat = %d, rest = %d",0
    format db "%d",0
    a dw 0
    b dw 0


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
        mov eax,0
        mov ebx,0
        mov ax, [a]
        mov bx, [b]
        cwd
        idiv bx ;ax-cat dx-rest
        
        
      
        
        
        cwde
        mov ebx, eax
        mov ax,dx
        cwde
        
        
        push eax
        push ebx
        push mesaj
        call [printf]
        add esp, 4*3
        
    
        push    dword 0
        call    [exit]