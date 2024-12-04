bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dw 0
    rezultat dw 0
    format_dword db "%d", 0
    format_word db "%hd", 0
    mess1 db "A = ",0
    mess2 db "B = ",0

; our code starts here
segment code use32 class=code
    start:
        push dword mess1
        call [printf]
        add esp, 4
        
        push dword a
        push dword format_dword
        call [scanf]
        add esp, 4*2
        
        push dword mess2
        call [printf]
        add esp , 4 
        
        push dword b
        push dword format_word
        call [scanf]
        add esp, 4*2      
        
        mov ax, [a]
        mov dx, [a+2]
        mov bx , [b]
        
        idiv bx
        
        mov [rezultat],AX
        
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
