Data Segment
no dw 5648h
o dw ?
z dw ?
data ends

code segment
assume cs:code,ds:data
start:  ;mov ax,data
	;mov ds,ax
	mov cx,0010h
	mov bx,0000h
	mov dx,0000h
	mov ax,no
back: rol ax,1
      JC up
      INC dx
      JMP nxt
up: INC bx
nxt: DEC CX
JNZ back
mov o,bx
mov z,dx
int 3
code ends
end start
