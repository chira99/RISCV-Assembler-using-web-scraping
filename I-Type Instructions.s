addi x1, x2, 64 
xori x5, x5, 0b100000
ori x1, x5, 0x0010
andi x5, x5, 4 
slli x1, x1, 1
srli x1, x1, 1
srai x1, x1, 1 
slti x5, x1, 2
sltiu x5, x1, 2
lb x5, 40(x6)
lh x5, 0(x6)
lw x5, 40(x6) 
lbu x5, 40(x6) 
lhu x5, 0(x6)



