; Setting used by the chipper assembler
option schip11
option binary
align off

; Recursive Disassembly
End of file
0x0200	jp loc_0219
0x0202	db #4d	;GRAPHIC =  #  ## #	ASCII(M)
0x0203	db #49	;GRAPHIC =  #  #  #	ASCII(I)
0x0204	db #53	;GRAPHIC =  # #  ##	ASCII(S)
0x0205	db #53	;GRAPHIC =  # #  ##	ASCII(S)
0x0206	db #49	;GRAPHIC =  #  #  #	ASCII(I)
0x0207	db #4c	;GRAPHIC =  #  ##  	ASCII(L)
0x0208	db #45	;GRAPHIC =  #   # #	ASCII(E)
0x0209	db #20	;GRAPHIC =   #     
0x020a	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x020b	db #79	;GRAPHIC =  ####  #	ASCII(y)
0x020c	db #20	;GRAPHIC =   #     
0x020d	db #44	;GRAPHIC =  #   #  	ASCII(D)
0x020e	db #61	;GRAPHIC =  ##    #	ASCII(a)
0x020f	db #76	;GRAPHIC =  ### ## 	ASCII(v)
0x0210	db #69	;GRAPHIC =  ## #  #	ASCII(i)
0x0211	db #64	;GRAPHIC =  ##  #  	ASCII(d)
0x0212	db #20	;GRAPHIC =   #     
0x0213	db #57	;GRAPHIC =  # # ###	ASCII(W)
0x0214	db #49	;GRAPHIC =  #  #  #	ASCII(I)
0x0215	db #4e	;GRAPHIC =  #  ### 	ASCII(N)
0x0216	db #54	;GRAPHIC =  # # #  	ASCII(T)
0x0217	db #45	;GRAPHIC =  #   # #	ASCII(E)
0x0218	db #52	;GRAPHIC =  # #  # 	ASCII(R)
loc_0219:   ; == START OF CODE BLOCK ==
0x0219	ld vc, #0c
0x021b	ld v0, #00
0x021d	ld v1, #00
0x021f	ld v5, #08
0x0221	ld v6, #0a
0x0223	ld v7, #00
0x0225	ld ve, #01
0x0227	ld I, #02ad
loc_0229:   ; == START OF CODE BLOCK ==
0x0229	drw v0, v1, #4
0x022b	add v0, #08
0x022d	se v0, #40
0x022f	jp loc_0229
0x0231	ld v0, #00
0x0233	ld v1, #1c
0x0235	ld I, #02b0
0x0237	drw v0, v1, #4
loc_0239:   ; == START OF CODE BLOCK ==
0x0239	ld I, #02b0
0x023b	drw v0, v1, #4
0x023d	se ve, #01
0x023f	jp loc_0249
0x0241	add v0, #04
0x0243	sne v0, #38
0x0245	ld ve, #00
0x0247	jp loc_024f
loc_0249:   ; == START OF CODE BLOCK ==
0x0249	add v0, #fc
0x024b	sne v0, #00
0x024d	ld ve, #01
loc_024f:   ; == START OF CODE BLOCK ==
0x024f	drw v0, v1, #4
0x0251	ld dt, vc
loc_0253:   ; == START OF CODE BLOCK ==
0x0253	ld vb, dt
0x0255	se vb, #00
0x0257	jp loc_0253
0x0259	ld v2, #08
0x025b	skp v2
0x025d	jp loc_0295
0x025f	se vc, #00
0x0261	add vc, #fe
0x0263	ld v3, #1b
0x0265	ld v2, v0
0x0267	ld I, #02b0
0x0269	drw v2, v3, #1
0x026b	ld v4, #00
loc_026d:   ; == START OF CODE BLOCK ==
0x026d	drw v2, v3, #1
0x026f	add v3, #ff
0x0271	drw v2, v3, #1
0x0273	se vf, #00
0x0275	ld v4, #01
0x0277	se v3, #03
0x0279	jp loc_026d
0x027b	drw v2, v3, #1
0x027d	se v4, #01
0x027f	jp loc_0291
0x0281	add v7, #05
0x0283	add v5, #ff
0x0285	ld v2, v0
0x0287	ld v3, #00
0x0289	ld I, #02ad
0x028b	drw v2, v3, #4
0x028d	sne v5, #00
0x028f	jp loc_0297
loc_0291:   ; == START OF CODE BLOCK ==
0x0291	add v6, #ff
0x0293	se v6, #00
loc_0295:   ; == START OF CODE BLOCK ==
0x0295	jp loc_0239
loc_0297:   ; == START OF CODE BLOCK ==
0x0297	ld I, #02b4
0x0299	ld b, v7
0x029b	ld v2, [I]
0x029d	ld v3, #1b
0x029f	ld v4, #0d
0x02a1	ld f, v1
0x02a3	drw v3, v4, #5
0x02a5	add v3, #05
0x02a7	ld f, v2
0x02a9	drw v3, v4, #5
loc_02ab:   ; == START OF CODE BLOCK ==
0x02ab	jp loc_02ab
0x02ad	db #10	;GRAPHIC =    #    
0x02ae	db #38	;GRAPHIC =   ###   	ASCII(8)
0x02af	db #38	;GRAPHIC =   ###   	ASCII(8)
0x02b0	db #10	;GRAPHIC =    #    
0x02b1	db #38	;GRAPHIC =   ###   	ASCII(8)
0x02b2	db #7c	;GRAPHIC =  #####  	ASCII(|)
0x02b3	db #fe	;GRAPHIC = ####### 
