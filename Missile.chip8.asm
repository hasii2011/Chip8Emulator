; Setting used by the chipper assembler
option schip11
option binary
align off

; Linear Disassembly
Error at address=0x0204, opcode=0x5353
Error at address=0x0216, opcode=0x5445
Error at address=0x0218, opcode=0x526c
Error at address=0x021a, opcode=0x0c60
Error at address=0x021c, opcode=0x0061
Error at address=0x021e, opcode=0x0065
Error at address=0x0220, opcode=0x0866
Error at address=0x0222, opcode=0x0a67
Error at address=0x0224, opcode=0x006e
Error at address=0x0226, opcode=0x01a2
Error at address=0x022c, opcode=0x0830
Error at address=0x0232, opcode=0x0061
Error at address=0x023e, opcode=0x0112
Error at address=0x0242, opcode=0x0440
Error at address=0x0246, opcode=0x0012
Error at address=0x024a, opcode=0xfc40
Error at address=0x024c, opcode=0x006e
Error at address=0x024e, opcode=0x01d0
Error at address=0x0254, opcode=0x073b
Error at address=0x0256, opcode=0x0012
Error at address=0x0258, opcode=0x5362
Error at address=0x025a, opcode=0x08e2
Error at address=0x025c, opcode=0x9e12
Error at address=0x025e, opcode=0x953c
Error at address=0x0260, opcode=0x007c
Error at address=0x0262, opcode=0xfe63
Error at address=0x0266, opcode=0x00a2
Error at address=0x026c, opcode=0x00d2
Error at address=0x0270, opcode=0xffd2
Error at address=0x0274, opcode=0x0064
Error at address=0x0276, opcode=0x0133
Error at address=0x0278, opcode=0x0312
Error at address=0x027e, opcode=0x0112
Error at address=0x0280, opcode=0x9177
Error at address=0x0282, opcode=0x0575
Error at address=0x0284, opcode=0xff82
Error at address=0x0286, opcode=0x0063
Error at address=0x0288, opcode=0x00a2
Error at address=0x028e, opcode=0x0012
Error at address=0x0290, opcode=0x9776
Error at address=0x0292, opcode=0xff36
Error at address=0x0294, opcode=0x0012
Error at address=0x02a0, opcode=0x0df1
Error at address=0x02a6, opcode=0x05f2
; End of file
0x0200	jp loc_0219
0x0202	sne vd, #49
0x0204	BAD OPCODE 0x5353
0x0206	sne v9, #4c
0x0208	sne v5, #20
0x020a	ld v2, #79
0x020c	call loc_0044
0x020e	ld v1, #76
0x0210	ld v9, #64
0x0212	call loc_0057
0x0214	sne v9, #4e
0x0216	BAD OPCODE 0x5445
0x0218	BAD OPCODE 0x526c
0x021a	BAD OPCODE 0x0c60
0x021c	BAD OPCODE 0x0061
0x021e	BAD OPCODE 0x0065
0x0220	BAD OPCODE 0x0866
0x0222	BAD OPCODE 0x0a67
0x0224	BAD OPCODE 0x006e
0x0226	BAD OPCODE 0x01a2
0x0228	ld I, #0dd0
0x022a	jp loc_0470
0x022c	BAD OPCODE 0x0830
0x022e	sne v0, #12
0x0230	call loc_0960
0x0232	BAD OPCODE 0x0061
0x0234	jp loc_0ca2
0x0236	jp v0, #00d0
0x0238	jp loc_04a2
0x023a	jp v0, #00d0
0x023c	jp loc_043e
0x023e	BAD OPCODE 0x0112
0x0240	sne v9, #70
0x0242	BAD OPCODE 0x0440
0x0244	se v8, #6e
0x0246	BAD OPCODE 0x0012
0x0248	sne vf, #70
0x024a	BAD OPCODE 0xfc40
0x024c	BAD OPCODE 0x006e
0x024e	BAD OPCODE 0x01d0
0x0250	jp loc_04fc
0x0252	jp loc_05fb
0x0254	BAD OPCODE 0x073b
0x0256	BAD OPCODE 0x0012
0x0258	BAD OPCODE 0x5362
0x025a	BAD OPCODE 0x08e2
0x025c	BAD OPCODE 0x9e12
0x025e	BAD OPCODE 0x953c
0x0260	BAD OPCODE 0x007c
0x0262	BAD OPCODE 0xfe63
0x0264	jp loc_0b82
0x0266	BAD OPCODE 0x00a2
0x0268	jp v0, #00d2
0x026a	se v1, #64
0x026c	BAD OPCODE 0x00d2
0x026e	se v1, #73
0x0270	BAD OPCODE 0xffd2
0x0272	se v1, #3f
0x0274	BAD OPCODE 0x0064
0x0276	BAD OPCODE 0x0133
0x0278	BAD OPCODE 0x0312
0x027a	ld vd, #d2
0x027c	se v1, #34
0x027e	BAD OPCODE 0x0112
0x0280	BAD OPCODE 0x9177
0x0282	BAD OPCODE 0x0575
0x0284	BAD OPCODE 0xff82
0x0286	BAD OPCODE 0x0063
0x0288	BAD OPCODE 0x00a2
0x028a	ld I, #0dd2
0x028c	se v4, #45
0x028e	BAD OPCODE 0x0012
0x0290	BAD OPCODE 0x9776
0x0292	BAD OPCODE 0xff36
0x0294	BAD OPCODE 0x0012
0x0296	se v9, #a2
0x0298	jp v0, #04f7
0x029a	se v3, #f2
0x029c	ld v5, #63
0x029e	jp loc_0b64
0x02a0	BAD OPCODE 0x0df1
0x02a2	call loc_09d3
0x02a4	sne v5, #73
0x02a6	BAD OPCODE 0x05f2
0x02a8	call loc_09d3
0x02aa	sne v5, #12
0x02ac	ld I, #0b10
0x02ae	se v8, #38
0x02b0	jp loc_0038
0x02b2	add vc, #fe
