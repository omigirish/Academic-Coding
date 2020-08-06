Data Segment
no dw 5648h
0 dw ?
z dw ?
data ends

code segment
assume cs:code,ds:data
start: mov ax,data
mov ds,ax
mov cx,0010h
mov bx,0000h
mov dx,0000h
mov ax,no
back:rol ax,1
IC up
INC dx
JMP NXT
up:INC bx
NXT: DEC CX
INZ back
mov 0,bx
mov z,dx
int 3
code ends
end start
