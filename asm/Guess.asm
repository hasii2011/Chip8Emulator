; Setting used by the chipper assembler
option schip11
option binary
align off

; Recursive Disassembly
End of file
0x0200	ld ve, #01
loc_0202:   ; == START OF CODE BLOCK ==
0x0202	cls
0x0204	ld vd, #01
0x0206	ld va, #01
0x0208	ld vb, #01
loc_020a:   ; == START OF CODE BLOCK ==
0x020a	ld vc, vd
0x020c	and vc, ve
0x020e	sne vc, #00
0x0210	jp loc_0220
0x0212	ld v8, vd
0x0214	call loc_023e
0x0216	se va, #40
0x0218	jp loc_0220
0x021a	ld va, #01
0x021c	add vb, #06
0x021e	se vc, #3f
loc_0220:   ; == START OF CODE BLOCK ==
0x0220	add vd, #01
0x0222	se vd, #3f
0x0224	jp loc_020a
0x0226	ld v0, k
0x0228	sne v0, #05
0x022a	add v9, ve
0x022c	add ve, ve
0x022e	se ve, #40
0x0230	jp loc_0202
0x0232	ld va, #1c
0x0234	ld vb, #0d
0x0236	ld v8, v9
0x0238	cls
0x023a	call loc_023e
loc_023c:   ; == START OF CODE BLOCK ==
0x023c	jp loc_023c
loc_023e:   ; == START OF CODE BLOCK ==
0x023e	ld I, #0294
0x0240	ld b, v8
0x0242	ld v2, [I]
0x0244	call loc_0254
0x0246	drw va, vb, #5
0x0248	add va, #04
0x024a	ld v1, v2
0x024c	call loc_0254
0x024e	drw va, vb, #5
0x0250	add va, #05
0x0252	ret
loc_0254:   ; == START OF CODE BLOCK ==
0x0254	ld v3, v1
0x0256	add v3, v3
0x0258	add v3, v3
0x025a	add v3, v1
0x025c	ld I, #0262
0x025e	add I, v3
0x0260	ret
0x0262	db #e0	;GRAPHIC = ###     
0x0263	db #a0	;GRAPHIC = # #     
0x0264	db #a0	;GRAPHIC = # #     
0x0265	db #a0	;GRAPHIC = # #     
0x0266	db #e0	;GRAPHIC = ###     
0x0267	db #40	;GRAPHIC =  #      	ASCII(@)
0x0268	db #40	;GRAPHIC =  #      	ASCII(@)
0x0269	db #40	;GRAPHIC =  #      	ASCII(@)
0x026a	db #40	;GRAPHIC =  #      	ASCII(@)
0x026b	db #40	;GRAPHIC =  #      	ASCII(@)
0x026c	db #e0	;GRAPHIC = ###     
0x026d	db #20	;GRAPHIC =   #     
0x026e	db #e0	;GRAPHIC = ###     
0x026f	db #80	;GRAPHIC = #       
0x0270	db #e0	;GRAPHIC = ###     
0x0271	db #e0	;GRAPHIC = ###     
0x0272	db #20	;GRAPHIC =   #     
0x0273	db #e0	;GRAPHIC = ###     
0x0274	db #20	;GRAPHIC =   #     
0x0275	db #e0	;GRAPHIC = ###     
0x0276	db #a0	;GRAPHIC = # #     
0x0277	db #a0	;GRAPHIC = # #     
0x0278	db #e0	;GRAPHIC = ###     
0x0279	db #20	;GRAPHIC =   #     
0x027a	db #20	;GRAPHIC =   #     
0x027b	db #e0	;GRAPHIC = ###     
0x027c	db #80	;GRAPHIC = #       
0x027d	db #e0	;GRAPHIC = ###     
0x027e	db #20	;GRAPHIC =   #     
0x027f	db #e0	;GRAPHIC = ###     
0x0280	db #e0	;GRAPHIC = ###     
0x0281	db #80	;GRAPHIC = #       
0x0282	db #e0	;GRAPHIC = ###     
0x0283	db #a0	;GRAPHIC = # #     
0x0284	db #e0	;GRAPHIC = ###     
0x0285	db #e0	;GRAPHIC = ###     
0x0286	db #20	;GRAPHIC =   #     
0x0287	db #20	;GRAPHIC =   #     
0x0288	db #20	;GRAPHIC =   #     
0x0289	db #20	;GRAPHIC =   #     
0x028a	db #e0	;GRAPHIC = ###     
0x028b	db #a0	;GRAPHIC = # #     
0x028c	db #e0	;GRAPHIC = ###     
0x028d	db #a0	;GRAPHIC = # #     
0x028e	db #e0	;GRAPHIC = ###     
0x028f	db #e0	;GRAPHIC = ###     
0x0290	db #a0	;GRAPHIC = # #     
0x0291	db #e0	;GRAPHIC = ###     
0x0292	db #20	;GRAPHIC =   #     
0x0293	db #e0	;GRAPHIC = ###     
