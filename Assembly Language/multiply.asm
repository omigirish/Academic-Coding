Data Segment
data ends
code segment
start:  mov ax,0ffffh
mov bx,0ffffh
mul bx
int 3
code ends
end start
