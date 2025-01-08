bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen, fclose, fprintf
import exit msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    cuvant resb 30
    format_c db "%s", 0
    descriptor dd 0
    mod_acces db "w", 0
    format_s db "%d", 0

; our code starts here
segment code use32 class=code
    start:
        cld
        repeta:
            push cuvant
            push format_c
            call [scanf]
            add esp, 8
            
            cmp byte [cuvant], '$'
            je iesire
            
            
            push mod_acces
            push cuvant
            call [fopen]
            add esp, 8
            
            cmp eax, 0
            je iesire
            
            mov [descriptor], eax
            
            
            mov ebx, 0
            mov esi, cuvant
            bucla:
                lodsb
                cmp AL, 0
                je f_bucla
                inc ebx
            jmp bucla
                
            f_bucla:
            
            push ebx
            push format_s
            push dword [descriptor]
            call [fprintf]
            add esp, 3*4
            
            push dword [descriptor]
            call [fclose]
            add esp, 4
            
        jmp repeta
    
        iesire:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

        
        
        
        
        
        
        
        
        