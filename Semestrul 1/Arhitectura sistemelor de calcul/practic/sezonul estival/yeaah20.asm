bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    format db "%x",0
    sumna db "suma = %x",10,0
    diffa db "diferenta = %x",0
    
    a dd 0
    b dd 0


segment code use32 class=code

    start:
    
        push dword a
        push dword format
        call [scanf]
        add esp ,4*2
        
        push dword b
        push dword format
        call [scanf]
        add esp ,4*2
        
        mov eax, [a]
        mov ebx, [b]
        
        mov edx,0
        mov dx, ax
        add dx, bx
        
        shr eax, 16
        shr ebx, 16
        
        mov ecx,0
        mov cx, ax
        sub cx, bx
        
        pushad
        push edx
        push dword sumna
        call [printf]
        add esp, 4*2
        popad
        push ecx
        push dword diffa
        call [printf]
        add esp, 4*2
        
  
        push    dword 0
        call    [exit]
        
        