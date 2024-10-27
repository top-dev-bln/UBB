bits 32

global start        


extern exit
import exit msvcrt.dll

segment data use32 class=data

 a dw 5
 b db 2
 c dw 1
 d db 2
 e dd 6
 x dq 50
 

segment code use32 class=code
    start:
    ;x/2+100*(a+b)-3/(c+d)+e*e
    
    mov edx,[x+4]
    mov eax, [x]
    mov ebx,2
    div ebx ; EDX:EAX = x/2
    
    push edx
    push eax
    
    mov al, [b]
    cbw
    add ax, [a] ; ax = a+b
    mov bx, 100
    imul bx ; DX:AX = 100*(a+b)
 
    pop ecx
    pop ebx ; EBX:ECX = x/2
    push dx
    push ax

    pop eax ; EAX = 100*(a+b)
    mov EDX, 0
    
    add ECX, EAX
    adc EBX, EDX ; EBX:ECX=x/2 + 100*(a+b)
    
    
    mov DX, [c]
    mov Al, [d]
    cbw ; ax = d
    add DX,AX ; DX = c+d
    
    
    
    mov EAX, 3
    
    push ebx
    mov BX,DX
    mov EDX,0
    
    idiv BX ; AX = 3/(c+d)
    pop EBX
    
    sub ECX, EAX
    sbb EBX, 0  ;  EBX:ECX = x/2 + 100*(a+b) - 3/(c+d)
    
    mov EAX, [e]
    mul EAX
   ; EDX:EAX = e*e
   add EAX, ECX
   adc EDX, EBX
   
   
    
    
     
    
    
    
    
        push    dword 0
        call    [exit] 
