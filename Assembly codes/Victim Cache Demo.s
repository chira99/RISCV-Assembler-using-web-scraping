addi x1, x1, 120
addi x2, x2, 100
addi x3, x1, 20
addi x7, x7, 4
slli x1, x3, 2
xor x4, x1, x2
or x5, x3, x1
slli x5, x5, 1
addi x5, x5, 90
slt x6, x5, x4
lw x8, 0(x0)
lw x8, 64(x0)
lw x8, 0(x0)
sw x1, 0(x7)
sw x2, 4(x7)
sw x3, 8(x7)
sw x4, 12(x7)
sw x5, 16(x7)
sw x6, 20(x7)
