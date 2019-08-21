; Setting used by the chipper assembler
option schip11
option binary
align off

; Recursive Disassembly
End of file
0x0200	jp loc_021a
0x0202	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x0203	db #2e	;GRAPHIC =   # ### 	ASCII(.)
0x0204	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0205	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0206	db #20	;GRAPHIC =   #     
0x0207	db #43	;GRAPHIC =  #    ##	ASCII(C)
0x0208	db #2e	;GRAPHIC =   # ### 	ASCII(.)
0x0209	db #20	;GRAPHIC =   #     
0x020a	db #45	;GRAPHIC =  #   # #	ASCII(E)
0x020b	db #67	;GRAPHIC =  ##  ###	ASCII(g)
0x020c	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x020d	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x020e	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x020f	db #72	;GRAPHIC =  ###  # 	ASCII(r)
0x0210	db #67	;GRAPHIC =  ##  ###	ASCII(g)
0x0211	db #20	;GRAPHIC =   #     
0x0212	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x0213	db #38	;GRAPHIC =   ###   	ASCII(8)
0x0214	db #2f	;GRAPHIC =   # ####	ASCII(/)
0x0215	db #38	;GRAPHIC =   ###   	ASCII(8)
0x0216	db #2d	;GRAPHIC =   # ## #	ASCII(-)
0x0217	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0218	db #39	;GRAPHIC =   ###  #	ASCII(9)
0x0219	db #31	;GRAPHIC =   ##   #	ASCII(1)
loc_021a:   ; == START OF CODE BLOCK ==
0x021a	xor v0, v0
0x021c	xor v1, v1
0x021e	ld I, #08c8
0x0220	ld [I], v1
0x0222	ld v0, #05
0x0224	ld I, #08cc
0x0226	ld [I], v0
0x0228	xor v7, v7
loc_022a:   ; == START OF CODE BLOCK ==
0x022a	xor v6, v6
0x022c	call loc_0772
0x022e	cls
0x0230	call loc_0794
loc_0232:   ; == START OF CODE BLOCK ==
0x0232	ld ve, #40
0x0234	and v7, ve
0x0236	ld ve, #27
0x0238	or v7, ve
0x023a	ld v8, #1a
0x023c	ld v9, #0c
0x023e	ld va, #38
0x0240	ld vb, #00
0x0242	ld vc, #02
0x0244	ld vd, #1a
0x0246	call loc_0750
0x0248	ld I, #08ed
0x024a	drw va, vb, #4
0x024c	drw vc, vd, #4
loc_024e:   ; == START OF CODE BLOCK ==
0x024e	call loc_03d0
0x0250	se ve, #00
0x0252	jp loc_027c
loc_0254:   ; == START OF CODE BLOCK ==
0x0254	ld I, #08cc
0x0256	ld v0, [I]
0x0258	ld v5, v0
0x025a	rnd v4, #ff
0x025c	and v4, v5
0x025e	call loc_04f6
0x0260	rnd v4, #ff
0x0262	and v4, v5
0x0264	call loc_061e
0x0266	ld v0, #01
0x0268	sknp v0
0x026a	call loc_07d6
0x026c	se v6, #f7
0x026e	jp loc_024e
0x0270	ld ve, v6
0x0272	call loc_087a
0x0274	ld ve, #64
0x0276	call loc_087a
0x0278	call loc_07d6
0x027a	jp loc_022a
loc_027c:   ; == START OF CODE BLOCK ==
0x027c	ld v0, dt
0x027e	sne v0, #00
0x0280	jp loc_0310
0x0282	ld v0, v8
0x0284	shr v0
0x0286	ld v1, va
0x0288	shr v1
0x028a	sub v0, v1
0x028c	sne v0, #00
0x028e	jp loc_029a
0x0290	sne v0, #01
0x0292	jp loc_029a
0x0294	sne v0, #ff
0x0296	jp loc_029a
0x0298	jp loc_02c8
loc_029a:   ; == START OF CODE BLOCK ==
0x029a	ld v0, v9
0x029c	shr v0
0x029e	ld v1, vb
0x02a0	shr v1
0x02a2	sub v0, v1
0x02a4	sne v0, #00
0x02a6	jp loc_02b2
0x02a8	sne v0, #01
0x02aa	jp loc_02b2
0x02ac	sne v0, #ff
0x02ae	jp loc_02b2
0x02b0	jp loc_02c8
loc_02b2:   ; == START OF CODE BLOCK ==
0x02b2	ld I, #08ed
0x02b4	drw va, vb, #4
0x02b6	ld va, #38
0x02b8	ld vb, #00
0x02ba	drw va, vb, #4
0x02bc	ld ve, #f3
0x02be	and v7, ve
0x02c0	ld ve, #04
0x02c2	or v7, ve
0x02c4	ld ve, #32
0x02c6	call loc_087a
loc_02c8:   ; == START OF CODE BLOCK ==
0x02c8	ld v0, v8
0x02ca	shr v0
0x02cc	ld v1, vc
0x02ce	shr v1
0x02d0	sub v0, v1
0x02d2	sne v0, #00
0x02d4	jp loc_02e0
0x02d6	sne v0, #01
0x02d8	jp loc_02e0
0x02da	sne v0, #ff
0x02dc	jp loc_02e0
0x02de	jp loc_0254
loc_02e0:   ; == START OF CODE BLOCK ==
0x02e0	ld v0, v9
0x02e2	shr v0
0x02e4	ld v1, vd
0x02e6	shr v1
0x02e8	sub v0, v1
0x02ea	sne v0, #00
0x02ec	jp loc_02f8
0x02ee	sne v0, #01
0x02f0	jp loc_02f8
0x02f2	sne v0, #ff
0x02f4	jp loc_02f8
0x02f6	jp loc_0254
loc_02f8:   ; == START OF CODE BLOCK ==
0x02f8	ld I, #08ed
0x02fa	drw vc, vd, #4
0x02fc	ld vc, #02
0x02fe	ld vd, #1a
0x0300	drw vc, vd, #4
0x0302	ld ve, #cf
0x0304	and v7, ve
0x0306	ld ve, #20
0x0308	or v7, ve
0x030a	ld ve, #19
0x030c	call loc_087a
0x030e	jp loc_0254
loc_0310:   ; == START OF CODE BLOCK ==
0x0310	ld v0, #3f
0x0312	call loc_08a8
0x0314	call loc_0750
0x0316	ld I, #08ed
0x0318	drw va, vb, #4
0x031a	drw vc, vd, #4
0x031c	ld ve, #40
0x031e	xor v7, ve
0x0320	ld v0, v7
0x0322	and v0, ve
0x0324	se v0, #00
0x0326	jp loc_0232
0x0328	ld ve, v6
0x032a	call loc_087a
0x032c	call loc_088a
0x032e	cls
0x0330	ld v6, #11
0x0332	ld v7, #0a
0x0334	ld I, #08ca
0x0336	call loc_07e6
0x0338	ld v6, #11
0x033a	ld v7, #10
0x033c	ld I, #08c8
0x033e	call loc_07e6
0x0340	ld v4, #00
0x0342	ld v5, #08
0x0344	ld v6, #00
0x0346	ld v7, #0f
loc_0348:   ; == START OF CODE BLOCK ==
0x0348	ld I, #0b19
0x034a	drw v4, v6, #9
0x034c	ld I, #0b22
0x034e	drw v5, v6, #9
0x0350	ld v0, #03
0x0352	call loc_08a8
0x0354	se ve, #00
0x0356	jp loc_03c6
0x0358	ld I, #0b19
0x035a	drw v4, v6, #9
0x035c	ld I, #0b22
0x035e	drw v5, v6, #9
0x0360	add v4, #02
0x0362	add v5, #02
0x0364	se v4, #30
0x0366	jp loc_0348
loc_0368:   ; == START OF CODE BLOCK ==
0x0368	ld I, #0b19
0x036a	drw v4, v6, #9
0x036c	ld I, #0b22
0x036e	drw v5, v6, #9
0x0370	ld v0, #03
0x0372	call loc_08a8
0x0374	se ve, #00
0x0376	jp loc_03c6
0x0378	ld I, #0b19
0x037a	drw v4, v6, #9
0x037c	ld I, #0b22
0x037e	drw v5, v6, #9
0x0380	add v6, #02
0x0382	se v6, #16
0x0384	jp loc_0368
loc_0386:   ; == START OF CODE BLOCK ==
0x0386	ld I, #0b19
0x0388	drw v4, v6, #9
0x038a	ld I, #0b22
0x038c	drw v5, v6, #9
0x038e	ld v0, #03
0x0390	call loc_08a8
0x0392	se ve, #00
0x0394	jp loc_03c6
0x0396	ld I, #0b19
0x0398	drw v4, v6, #9
0x039a	ld I, #0b22
0x039c	drw v5, v6, #9
0x039e	add v4, #fe
0x03a0	add v5, #fe
0x03a2	se v4, #00
0x03a4	jp loc_0386
loc_03a6:   ; == START OF CODE BLOCK ==
0x03a6	ld I, #0b19
0x03a8	drw v4, v6, #9
0x03aa	ld I, #0b22
0x03ac	drw v5, v6, #9
0x03ae	ld v0, #03
0x03b0	call loc_08a8
0x03b2	se ve, #00
0x03b4	jp loc_03c6
0x03b6	ld I, #0b19
0x03b8	drw v4, v6, #9
0x03ba	ld I, #0b22
0x03bc	drw v5, v6, #9
0x03be	add v6, #fe
0x03c0	se v6, #00
0x03c2	jp loc_03a6
0x03c4	jp loc_0348
loc_03c6:   ; == START OF CODE BLOCK ==
0x03c6	ld I, #0b22
0x03c8	drw v5, v6, #9
0x03ca	ld I, #0b2b
0x03cc	drw v5, v6, #9
0x03ce	jp loc_021a
loc_03d0:   ; == START OF CODE BLOCK ==
0x03d0	ld v3, v7
0x03d2	ld ve, #03
0x03d4	and v3, ve
0x03d6	ld v4, v8
0x03d8	ld v5, v9
0x03da	ld ve, #06
0x03dc	sknp ve
0x03de	jp loc_0432
0x03e0	ld ve, #03
0x03e2	sknp ve
0x03e4	jp loc_044a
0x03e6	ld ve, #08
0x03e8	sknp ve
0x03ea	jp loc_0462
0x03ec	ld ve, #07
0x03ee	sknp ve
0x03f0	jp loc_047a
0x03f2	sne v3, #03
0x03f4	add v5, #02
0x03f6	sne v3, #00
0x03f8	add v5, #fe
0x03fa	sne v3, #02
0x03fc	add v4, #02
0x03fe	sne v3, #01
0x0400	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0401	db #fe	;GRAPHIC = ####### 
0x0402	ld v0, v4
0x0404	ld v1, v5
0x0406	call loc_07ba
0x0408	ld v2, v0
0x040a	ld ve, #08
0x040c	and v0, ve
0x040e	se v0, #00
0x0410	jp loc_0492
0x0412	ld ve, #07
0x0414	ld v0, v2
0x0416	and v2, ve
0x0418	sne v2, #05
0x041a	db #14	;GRAPHIC =    # #  
0x041b	db #9a	;GRAPHIC = #  ## # 
0x041c	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x041d	db #06	;GRAPHIC =      ## 
0x041e	db #14	;GRAPHIC =    # #  
0x041f	db #b2	;GRAPHIC = # ##  # 
0x0420	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0421	db #07	;GRAPHIC =      ###
0x0422	db #14	;GRAPHIC =    # #  
0x0423	db #ec	;GRAPHIC = ### ##  
0x0424	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0425	db #50	;GRAPHIC =  # #    	ASCII(P)
0x0426	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0427	db #fc	;GRAPHIC = ######  
0x0428	db #87	;GRAPHIC = #    ###
0x0429	db #e2	;GRAPHIC = ###   # 
0x042a	db #87	;GRAPHIC = #    ###
0x042b	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x042c	db #88	;GRAPHIC = #   #   
0x042d	db #40	;GRAPHIC =  #      	ASCII(@)
0x042e	db #89	;GRAPHIC = #   #  #
0x042f	db #50	;GRAPHIC =  # #    	ASCII(P)
0x0430	db #17	;GRAPHIC =    # ###
0x0431	db #50	;GRAPHIC =  # #    	ASCII(P)
loc_0432:   ; == START OF CODE BLOCK ==
0x0432	db #80	;GRAPHIC = #       
0x0433	db #40	;GRAPHIC =  #      	ASCII(@)
0x0434	db #81	;GRAPHIC = #      #
0x0435	db #50	;GRAPHIC =  # #    	ASCII(P)
0x0436	db #71	;GRAPHIC =  ###   #	ASCII(q)
0x0437	db #02	;GRAPHIC =       # 
0x0438	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0439	db #ba	;GRAPHIC = # ### # 
0x043a	db #82	;GRAPHIC = #     # 
0x043b	db #00	;GRAPHIC =         
0x043c	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x043d	db #08	;GRAPHIC =     #   
0x043e	db #80	;GRAPHIC = #       
0x043f	db #e2	;GRAPHIC = ###   # 
0x0440	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0441	db #00	;GRAPHIC =         
0x0442	db #13	;GRAPHIC =    #  ##
0x0443	db #f2	;GRAPHIC = ####  # 
0x0444	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x0445	db #03	;GRAPHIC =       ##
0x0446	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x0447	db #02	;GRAPHIC =       # 
0x0448	db #14	;GRAPHIC =    # #  
0x0449	db #0e	;GRAPHIC =     ### 
loc_044a:   ; == START OF CODE BLOCK ==
0x044a	db #80	;GRAPHIC = #       
0x044b	db #40	;GRAPHIC =  #      	ASCII(@)
0x044c	db #81	;GRAPHIC = #      #
0x044d	db #50	;GRAPHIC =  # #    	ASCII(P)
0x044e	db #71	;GRAPHIC =  ###   #	ASCII(q)
0x044f	db #fe	;GRAPHIC = ####### 
0x0450	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0451	db #ba	;GRAPHIC = # ### # 
0x0452	db #82	;GRAPHIC = #     # 
0x0453	db #00	;GRAPHIC =         
0x0454	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0455	db #08	;GRAPHIC =     #   
0x0456	db #80	;GRAPHIC = #       
0x0457	db #e2	;GRAPHIC = ###   # 
0x0458	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0459	db #00	;GRAPHIC =         
0x045a	db #13	;GRAPHIC =    #  ##
0x045b	db #f2	;GRAPHIC = ####  # 
0x045c	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x045d	db #00	;GRAPHIC =         
0x045e	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x045f	db #fe	;GRAPHIC = ####### 
0x0460	db #14	;GRAPHIC =    # #  
0x0461	db #0e	;GRAPHIC =     ### 
loc_0462:   ; == START OF CODE BLOCK ==
0x0462	db #80	;GRAPHIC = #       
0x0463	db #40	;GRAPHIC =  #      	ASCII(@)
0x0464	db #81	;GRAPHIC = #      #
0x0465	db #50	;GRAPHIC =  # #    	ASCII(P)
0x0466	db #70	;GRAPHIC =  ###    	ASCII(p)
0x0467	db #02	;GRAPHIC =       # 
0x0468	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0469	db #ba	;GRAPHIC = # ### # 
0x046a	db #82	;GRAPHIC = #     # 
0x046b	db #00	;GRAPHIC =         
0x046c	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x046d	db #08	;GRAPHIC =     #   
0x046e	db #80	;GRAPHIC = #       
0x046f	db #e2	;GRAPHIC = ###   # 
0x0470	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0471	db #00	;GRAPHIC =         
0x0472	db #13	;GRAPHIC =    #  ##
0x0473	db #f2	;GRAPHIC = ####  # 
0x0474	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x0475	db #02	;GRAPHIC =       # 
0x0476	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0477	db #02	;GRAPHIC =       # 
0x0478	db #14	;GRAPHIC =    # #  
0x0479	db #0e	;GRAPHIC =     ### 
loc_047a:   ; == START OF CODE BLOCK ==
0x047a	db #80	;GRAPHIC = #       
0x047b	db #40	;GRAPHIC =  #      	ASCII(@)
0x047c	db #81	;GRAPHIC = #      #
0x047d	db #50	;GRAPHIC =  # #    	ASCII(P)
0x047e	db #70	;GRAPHIC =  ###    	ASCII(p)
0x047f	db #fe	;GRAPHIC = ####### 
0x0480	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0481	db #ba	;GRAPHIC = # ### # 
0x0482	db #82	;GRAPHIC = #     # 
0x0483	db #00	;GRAPHIC =         
0x0484	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0485	db #08	;GRAPHIC =     #   
0x0486	db #80	;GRAPHIC = #       
0x0487	db #e2	;GRAPHIC = ###   # 
0x0488	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0489	db #00	;GRAPHIC =         
0x048a	db #13	;GRAPHIC =    #  ##
0x048b	db #f2	;GRAPHIC = ####  # 
0x048c	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x048d	db #01	;GRAPHIC =        #
0x048e	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x048f	db #fe	;GRAPHIC = ####### 
0x0490	db #14	;GRAPHIC =    # #  
0x0491	db #0e	;GRAPHIC =     ### 
loc_0492:   ; == START OF CODE BLOCK ==
0x0492	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0493	db #50	;GRAPHIC =  # #    	ASCII(P)
0x0494	db #d8	;GRAPHIC = ## ##   
0x0495	db #94	;GRAPHIC = #  # #  
0x0496	db #8e	;GRAPHIC = #   ### 
0x0497	db #f0	;GRAPHIC = ####    
0x0498	db #00	;GRAPHIC =         
0x0499	db #ee	;GRAPHIC = ### ### 
0x049a	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x049b	db #f0	;GRAPHIC = ####    
0x049c	db #80	;GRAPHIC = #       
0x049d	db #e2	;GRAPHIC = ###   # 
0x049e	db #80	;GRAPHIC = #       
0x049f	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x04a0	db #f0	;GRAPHIC = ####    
0x04a1	db #55	;GRAPHIC =  # # # #	ASCII(U)
0x04a2	db #a8	;GRAPHIC = # # #   
0x04a3	db #f1	;GRAPHIC = ####   #
0x04a4	db #d4	;GRAPHIC = ## # #  
0x04a5	db #54	;GRAPHIC =  # # #  	ASCII(T)
0x04a6	db #76	;GRAPHIC =  ### ## 	ASCII(v)
0x04a7	db #01	;GRAPHIC =        #
0x04a8	db #61	;GRAPHIC =  ##    #	ASCII(a)
0x04a9	db #05	;GRAPHIC =      # #
0x04aa	db #f0	;GRAPHIC = ####    
0x04ab	db #07	;GRAPHIC =      ###
0x04ac	db #40	;GRAPHIC =  #      	ASCII(@)
0x04ad	db #00	;GRAPHIC =         
0x04ae	db #f1	;GRAPHIC = ####   #
0x04af	db #18	;GRAPHIC =    ##   
0x04b0	db #14	;GRAPHIC =    # #  
0x04b1	db #24	;GRAPHIC =   #  #  	ASCII($)
0x04b2	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04b3	db #f0	;GRAPHIC = ####    
0x04b4	db #80	;GRAPHIC = #       
0x04b5	db #e2	;GRAPHIC = ###   # 
0x04b6	db #80	;GRAPHIC = #       
0x04b7	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x04b8	db #f0	;GRAPHIC = ####    
0x04b9	db #55	;GRAPHIC =  # # # #	ASCII(U)
0x04ba	db #a8	;GRAPHIC = # # #   
0x04bb	db #f5	;GRAPHIC = #### # #
0x04bc	db #d4	;GRAPHIC = ## # #  
0x04bd	db #54	;GRAPHIC =  # # #  	ASCII(T)
0x04be	db #76	;GRAPHIC =  ### ## 	ASCII(v)
0x04bf	db #04	;GRAPHIC =      #  
0x04c0	db #80	;GRAPHIC = #       
0x04c1	db #a0	;GRAPHIC = # #     
0x04c2	db #81	;GRAPHIC = #      #
0x04c3	db #b0	;GRAPHIC = # ##    
0x04c4	db #27	;GRAPHIC =   #  ###	ASCII(')
0x04c5	db #ba	;GRAPHIC = # ### # 
0x04c6	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04c7	db #f0	;GRAPHIC = ####    
0x04c8	db #80	;GRAPHIC = #       
0x04c9	db #e2	;GRAPHIC = ###   # 
0x04ca	db #30	;GRAPHIC =   ##    	ASCII(0)
0x04cb	db #00	;GRAPHIC =         
0x04cc	db #14	;GRAPHIC =    # #  
0x04cd	db #d2	;GRAPHIC = ## #  # 
0x04ce	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04cf	db #0c	;GRAPHIC =     ##  
0x04d0	db #87	;GRAPHIC = #    ###
0x04d1	db #e3	;GRAPHIC = ###   ##
0x04d2	db #80	;GRAPHIC = #       
0x04d3	db #c0	;GRAPHIC = ##      
0x04d4	db #81	;GRAPHIC = #      #
0x04d5	db #d0	;GRAPHIC = ## #    
0x04d6	db #27	;GRAPHIC =   #  ###	ASCII(')
0x04d7	db #ba	;GRAPHIC = # ### # 
0x04d8	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04d9	db #f0	;GRAPHIC = ####    
0x04da	db #80	;GRAPHIC = #       
0x04db	db #e2	;GRAPHIC = ###   # 
0x04dc	db #30	;GRAPHIC =   ##    	ASCII(0)
0x04dd	db #00	;GRAPHIC =         
0x04de	db #14	;GRAPHIC =    # #  
0x04df	db #e4	;GRAPHIC = ###  #  
0x04e0	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04e1	db #30	;GRAPHIC =   ##    	ASCII(0)
0x04e2	db #87	;GRAPHIC = #    ###
0x04e3	db #e3	;GRAPHIC = ###   ##
0x04e4	db #60	;GRAPHIC =  ##     	ASCII(`)
0x04e5	db #ff	;GRAPHIC = ########
0x04e6	db #f0	;GRAPHIC = ####    
0x04e7	db #18	;GRAPHIC =    ##   
0x04e8	db #f0	;GRAPHIC = ####    
0x04e9	db #15	;GRAPHIC =    # # #
0x04ea	db #14	;GRAPHIC =    # #  
0x04eb	db #24	;GRAPHIC =   #  #  	ASCII($)
0x04ec	db #43	;GRAPHIC =  #    ##	ASCII(C)
0x04ed	db #01	;GRAPHIC =        #
0x04ee	db #64	;GRAPHIC =  ##  #  	ASCII(d)
0x04ef	db #3a	;GRAPHIC =   ### # 	ASCII(:)
0x04f0	db #43	;GRAPHIC =  #    ##	ASCII(C)
0x04f1	db #02	;GRAPHIC =       # 
0x04f2	db #64	;GRAPHIC =  ##  #  	ASCII(d)
0x04f3	db #00	;GRAPHIC =         
0x04f4	db #14	;GRAPHIC =    # #  
0x04f5	db #24	;GRAPHIC =   #  #  	ASCII($)
loc_04f6:   ; == START OF CODE BLOCK ==
0x04f6	db #82	;GRAPHIC = #     # 
0x04f7	db #70	;GRAPHIC =  ###    	ASCII(p)
0x04f8	db #83	;GRAPHIC = #     ##
0x04f9	db #70	;GRAPHIC =  ###    	ASCII(p)
0x04fa	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x04fb	db #0c	;GRAPHIC =     ##  
0x04fc	db #82	;GRAPHIC = #     # 
0x04fd	db #e2	;GRAPHIC = ###   # 
0x04fe	db #80	;GRAPHIC = #       
0x04ff	db #a0	;GRAPHIC = # #     
0x0500	db #81	;GRAPHIC = #      #
0x0501	db #b0	;GRAPHIC = # ##    
0x0502	db #27	;GRAPHIC =   #  ###	ASCII(')
0x0503	db #ba	;GRAPHIC = # ### # 
0x0504	db #a8	;GRAPHIC = # # #   
0x0505	db #ed	;GRAPHIC = ### ## #
0x0506	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0507	db #f0	;GRAPHIC = ####    
0x0508	db #80	;GRAPHIC = #       
0x0509	db #e2	;GRAPHIC = ###   # 
0x050a	db #30	;GRAPHIC =   ##    	ASCII(0)
0x050b	db #00	;GRAPHIC =         
0x050c	db #15	;GRAPHIC =    # # #
0x050d	db #24	;GRAPHIC =   #  #  	ASCII($)
0x050e	db #da	;GRAPHIC = ## ## # 
0x050f	db #b4	;GRAPHIC = # ## #  
0x0510	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0511	db #0c	;GRAPHIC =     ##  
0x0512	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x0513	db #02	;GRAPHIC =       # 
0x0514	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0515	db #00	;GRAPHIC =         
0x0516	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x0517	db #fe	;GRAPHIC = ####### 
0x0518	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0519	db #08	;GRAPHIC =     #   
0x051a	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x051b	db #02	;GRAPHIC =       # 
0x051c	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x051d	db #04	;GRAPHIC =      #  
0x051e	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x051f	db #fe	;GRAPHIC = ####### 
0x0520	db #da	;GRAPHIC = ## ## # 
0x0521	db #b4	;GRAPHIC = # ## #  
0x0522	db #00	;GRAPHIC =         
0x0523	db #ee	;GRAPHIC = ### ### 
0x0524	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0525	db #80	;GRAPHIC = #       
0x0526	db #f1	;GRAPHIC = ####   #
0x0527	db #07	;GRAPHIC =      ###
0x0528	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x0529	db #00	;GRAPHIC =         
0x052a	db #15	;GRAPHIC =    # # #
0x052b	db #d4	;GRAPHIC = ## # #  
0x052c	db #34	;GRAPHIC =   ## #  	ASCII(4)
0x052d	db #00	;GRAPHIC =         
0x052e	db #15	;GRAPHIC =    # # #
0x052f	db #d4	;GRAPHIC = ## # #  
0x0530	db #81	;GRAPHIC = #      #
0x0531	db #00	;GRAPHIC =         
0x0532	db #83	;GRAPHIC = #     ##
0x0533	db #0e	;GRAPHIC =     ### 
0x0534	db #3f	;GRAPHIC =   ######	ASCII(?)
0x0535	db #00	;GRAPHIC =         
0x0536	db #15	;GRAPHIC =    # # #
0x0537	db #56	;GRAPHIC =  # # ## 	ASCII(V)
0x0538	db #83	;GRAPHIC = #     ##
0x0539	db #90	;GRAPHIC = #  #    
0x053a	db #83	;GRAPHIC = #     ##
0x053b	db #b5	;GRAPHIC = # ## # #
0x053c	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x053d	db #00	;GRAPHIC =         
0x053e	db #15	;GRAPHIC =    # # #
0x053f	db #8c	;GRAPHIC = #   ##  
0x0540	db #33	;GRAPHIC =   ##  ##	ASCII(3)
0x0541	db #00	;GRAPHIC =         
0x0542	db #15	;GRAPHIC =    # # #
0x0543	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0544	db #87	;GRAPHIC = #    ###
0x0545	db #e3	;GRAPHIC = ###   ##
0x0546	db #83	;GRAPHIC = #     ##
0x0547	db #80	;GRAPHIC = #       
0x0548	db #83	;GRAPHIC = #     ##
0x0549	db #a5	;GRAPHIC = # #  # #
0x054a	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x054b	db #00	;GRAPHIC =         
0x054c	db #15	;GRAPHIC =    # # #
0x054d	db #bc	;GRAPHIC = # ####  
0x054e	db #33	;GRAPHIC =   ##  ##	ASCII(3)
0x054f	db #00	;GRAPHIC =         
0x0550	db #15	;GRAPHIC =    # # #
0x0551	db #a4	;GRAPHIC = # #  #  
0x0552	db #87	;GRAPHIC = #    ###
0x0553	db #e3	;GRAPHIC = ###   ##
0x0554	db #15	;GRAPHIC =    # # #
0x0555	db #d4	;GRAPHIC = ## # #  
0x0556	db #83	;GRAPHIC = #     ##
0x0557	db #80	;GRAPHIC = #       
0x0558	db #83	;GRAPHIC = #     ##
0x0559	db #a5	;GRAPHIC = # #  # #
0x055a	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x055b	db #00	;GRAPHIC =         
0x055c	db #15	;GRAPHIC =    # # #
0x055d	db #bc	;GRAPHIC = # ####  
0x055e	db #33	;GRAPHIC =   ##  ##	ASCII(3)
0x055f	db #00	;GRAPHIC =         
0x0560	db #15	;GRAPHIC =    # # #
0x0561	db #a4	;GRAPHIC = # #  #  
0x0562	db #87	;GRAPHIC = #    ###
0x0563	db #e3	;GRAPHIC = ###   ##
0x0564	db #83	;GRAPHIC = #     ##
0x0565	db #90	;GRAPHIC = #  #    
0x0566	db #83	;GRAPHIC = #     ##
0x0567	db #b5	;GRAPHIC = # ## # #
0x0568	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x0569	db #00	;GRAPHIC =         
0x056a	db #15	;GRAPHIC =    # # #
0x056b	db #8c	;GRAPHIC = #   ##  
0x056c	db #33	;GRAPHIC =   ##  ##	ASCII(3)
0x056d	db #00	;GRAPHIC =         
0x056e	db #15	;GRAPHIC =    # # #
0x056f	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0570	db #87	;GRAPHIC = #    ###
0x0571	db #e3	;GRAPHIC = ###   ##
0x0572	db #15	;GRAPHIC =    # # #
0x0573	db #d4	;GRAPHIC = ## # #  
0x0574	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x0575	db #40	;GRAPHIC =  #      	ASCII(@)
0x0576	db #81	;GRAPHIC = #      #
0x0577	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x0578	db #41	;GRAPHIC =  #     #	ASCII(A)
0x0579	db #00	;GRAPHIC =         
0x057a	db #15	;GRAPHIC =    # # #
0x057b	db #d4	;GRAPHIC = ## # #  
0x057c	db #da	;GRAPHIC = ## ## # 
0x057d	db #b4	;GRAPHIC = # ## #  
0x057e	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x057f	db #02	;GRAPHIC =       # 
0x0580	db #da	;GRAPHIC = ## ## # 
0x0581	db #b4	;GRAPHIC = # ## #  
0x0582	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0583	db #f3	;GRAPHIC = ####  ##
0x0584	db #87	;GRAPHIC = #    ###
0x0585	db #e2	;GRAPHIC = ###   # 
0x0586	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x0587	db #0c	;GRAPHIC =     ##  
0x0588	db #87	;GRAPHIC = #    ###
0x0589	db #21	;GRAPHIC =   #    #	ASCII(!)
0x058a	db #00	;GRAPHIC =         
0x058b	db #ee	;GRAPHIC = ### ### 
0x058c	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x058d	db #10	;GRAPHIC =    #    
0x058e	db #81	;GRAPHIC = #      #
0x058f	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x0590	db #41	;GRAPHIC =  #     #	ASCII(A)
0x0591	db #00	;GRAPHIC =         
0x0592	db #15	;GRAPHIC =    # # #
0x0593	db #d4	;GRAPHIC = ## # #  
0x0594	db #da	;GRAPHIC = ## ## # 
0x0595	db #b4	;GRAPHIC = # ## #  
0x0596	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x0597	db #fe	;GRAPHIC = ####### 
0x0598	db #da	;GRAPHIC = ## ## # 
0x0599	db #b4	;GRAPHIC = # ## #  
0x059a	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x059b	db #f3	;GRAPHIC = ####  ##
0x059c	db #87	;GRAPHIC = #    ###
0x059d	db #e2	;GRAPHIC = ###   # 
0x059e	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x059f	db #00	;GRAPHIC =         
0x05a0	db #87	;GRAPHIC = #    ###
0x05a1	db #21	;GRAPHIC =   #    #	ASCII(!)
0x05a2	db #00	;GRAPHIC =         
0x05a3	db #ee	;GRAPHIC = ### ### 
0x05a4	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x05a5	db #20	;GRAPHIC =   #     
0x05a6	db #81	;GRAPHIC = #      #
0x05a7	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x05a8	db #41	;GRAPHIC =  #     #	ASCII(A)
0x05a9	db #00	;GRAPHIC =         
0x05aa	db #15	;GRAPHIC =    # # #
0x05ab	db #d4	;GRAPHIC = ## # #  
0x05ac	db #da	;GRAPHIC = ## ## # 
0x05ad	db #b4	;GRAPHIC = # ## #  
0x05ae	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x05af	db #02	;GRAPHIC =       # 
0x05b0	db #da	;GRAPHIC = ## ## # 
0x05b1	db #b4	;GRAPHIC = # ## #  
0x05b2	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x05b3	db #f3	;GRAPHIC = ####  ##
0x05b4	db #87	;GRAPHIC = #    ###
0x05b5	db #e2	;GRAPHIC = ###   # 
0x05b6	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x05b7	db #08	;GRAPHIC =     #   
0x05b8	db #87	;GRAPHIC = #    ###
0x05b9	db #21	;GRAPHIC =   #    #	ASCII(!)
0x05ba	db #00	;GRAPHIC =         
0x05bb	db #ee	;GRAPHIC = ### ### 
0x05bc	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x05bd	db #80	;GRAPHIC = #       
0x05be	db #81	;GRAPHIC = #      #
0x05bf	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x05c0	db #41	;GRAPHIC =  #     #	ASCII(A)
0x05c1	db #00	;GRAPHIC =         
0x05c2	db #15	;GRAPHIC =    # # #
0x05c3	db #d4	;GRAPHIC = ## # #  
0x05c4	db #da	;GRAPHIC = ## ## # 
0x05c5	db #b4	;GRAPHIC = # ## #  
0x05c6	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x05c7	db #fe	;GRAPHIC = ####### 
0x05c8	db #da	;GRAPHIC = ## ## # 
0x05c9	db #b4	;GRAPHIC = # ## #  
0x05ca	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x05cb	db #f3	;GRAPHIC = ####  ##
0x05cc	db #87	;GRAPHIC = #    ###
0x05cd	db #e2	;GRAPHIC = ###   # 
0x05ce	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x05cf	db #04	;GRAPHIC =      #  
0x05d0	db #87	;GRAPHIC = #    ###
0x05d1	db #21	;GRAPHIC =   #    #	ASCII(!)
0x05d2	db #00	;GRAPHIC =         
0x05d3	db #ee	;GRAPHIC = ### ### 
0x05d4	db #c1	;GRAPHIC = ##     #
0x05d5	db #f0	;GRAPHIC = ####    
0x05d6	db #80	;GRAPHIC = #       
0x05d7	db #12	;GRAPHIC =    #  # 
0x05d8	db #30	;GRAPHIC =   ##    	ASCII(0)
0x05d9	db #00	;GRAPHIC =         
0x05da	db #15	;GRAPHIC =    # # #
0x05db	db #e4	;GRAPHIC = ###  #  
0x05dc	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x05dd	db #0c	;GRAPHIC =     ##  
0x05de	db #87	;GRAPHIC = #    ###
0x05df	db #e3	;GRAPHIC = ###   ##
0x05e0	db #82	;GRAPHIC = #     # 
0x05e1	db #e3	;GRAPHIC = ###   ##
0x05e2	db #15	;GRAPHIC =    # # #
0x05e3	db #0e	;GRAPHIC =     ### 
0x05e4	db #da	;GRAPHIC = ## ## # 
0x05e5	db #b4	;GRAPHIC = # ## #  
0x05e6	db #80	;GRAPHIC = #       
0x05e7	db #0e	;GRAPHIC =     ### 
0x05e8	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x05e9	db #00	;GRAPHIC =         
0x05ea	db #15	;GRAPHIC =    # # #
0x05eb	db #f2	;GRAPHIC = ####  # 
0x05ec	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x05ed	db #04	;GRAPHIC =      #  
0x05ee	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x05ef	db #fe	;GRAPHIC = ####### 
0x05f0	db #16	;GRAPHIC =    # ## 
0x05f1	db #14	;GRAPHIC =    # #  
0x05f2	db #80	;GRAPHIC = #       
0x05f3	db #0e	;GRAPHIC =     ### 
0x05f4	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x05f5	db #00	;GRAPHIC =         
0x05f6	db #15	;GRAPHIC =    # # #
0x05f7	db #fe	;GRAPHIC = ####### 
0x05f8	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x05f9	db #0c	;GRAPHIC =     ##  
0x05fa	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x05fb	db #02	;GRAPHIC =       # 
0x05fc	db #16	;GRAPHIC =    # ## 
0x05fd	db #14	;GRAPHIC =    # #  
0x05fe	db #80	;GRAPHIC = #       
0x05ff	db #0e	;GRAPHIC =     ### 
0x0600	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x0601	db #00	;GRAPHIC =         
0x0602	db #16	;GRAPHIC =    # ## 
0x0603	db #0a	;GRAPHIC =     # # 
0x0604	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x0605	db #08	;GRAPHIC =     #   
0x0606	db #7a	;GRAPHIC =  #### # 	ASCII(z)
0x0607	db #02	;GRAPHIC =       # 
0x0608	db #16	;GRAPHIC =    # ## 
0x0609	db #14	;GRAPHIC =    # #  
0x060a	db #80	;GRAPHIC = #       
0x060b	db #0e	;GRAPHIC =     ### 
0x060c	db #4f	;GRAPHIC =  #  ####	ASCII(O)
0x060d	db #00	;GRAPHIC =         
0x060e	db #15	;GRAPHIC =    # # #
0x060f	db #dc	;GRAPHIC = ## ###  
0x0610	db #62	;GRAPHIC =  ##   # 	ASCII(b)
0x0611	db #00	;GRAPHIC =         
0x0612	db #7b	;GRAPHIC =  #### ##	ASCII({)
0x0613	db #fe	;GRAPHIC = ####### 
0x0614	db #da	;GRAPHIC = ## ## # 
0x0615	db #b4	;GRAPHIC = # ## #  
0x0616	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0617	db #f3	;GRAPHIC = ####  ##
0x0618	db #87	;GRAPHIC = #    ###
0x0619	db #e2	;GRAPHIC = ###   # 
0x061a	db #87	;GRAPHIC = #    ###
0x061b	db #21	;GRAPHIC =   #    #	ASCII(!)
0x061c	db #00	;GRAPHIC =         
0x061d	db #ee	;GRAPHIC = ### ### 
loc_061e:   ; == START OF CODE BLOCK ==
0x061e	ld v2, v7
0x0620	ld v3, v7
0x0622	ld ve, #30
0x0624	and v2, ve
0x0626	ld v0, vc
0x0628	ld v1, vd
0x062a	call loc_07ba
0x062c	ld I, #08ed
0x062e	ld ve, #f0
0x0630	and v0, ve
0x0632	se v0, #00
0x0634	jp loc_064c
loc_0636:   ; == START OF CODE BLOCK ==
0x0636	drw vc, vd, #4
0x0638	sne v2, #30
0x063a	add vd, #02
0x063c	sne v2, #00
0x063e	add vd, #fe
0x0640	sne v2, #20
0x0642	add vc, #02
0x0644	sne v2, #10
0x0646	add vc, #fe
0x0648	drw vc, vd, #4
0x064a	ret
loc_064c:   ; == START OF CODE BLOCK ==
0x064c	ld ve, #80
0x064e	ld v1, dt
0x0650	se v1, #00
0x0652	jp loc_0704
0x0654	se v4, #00
0x0656	jp loc_0704
0x0658	ld v1, v0
0x065a	shl v3
0x065c	sne vf, #00
0x065e	jp loc_067e
0x0660	ld v3, v9
0x0662	sub v3, vd
0x0664	sne vf, #00
0x0666	jp loc_06b6
0x0668	se v3, #00
0x066a	jp loc_069c
0x066c	xor v7, ve
0x066e	ld v3, v8
0x0670	sub v3, vc
0x0672	sne vf, #00
0x0674	jp loc_06ea
0x0676	se v3, #00
0x0678	jp loc_06d0
0x067a	xor v7, ve
0x067c	jp loc_0704
loc_067e:   ; == START OF CODE BLOCK ==
0x067e	ld v3, v8
0x0680	sub v3, vc
0x0682	sne vf, #00
0x0684	jp loc_06ea
0x0686	se v3, #00
0x0688	jp loc_06d0
0x068a	xor v7, ve
0x068c	ld v3, v9
0x068e	sub v3, vd
0x0690	sne vf, #00
0x0692	jp loc_06b6
0x0694	se v3, #00
0x0696	jp loc_069c
0x0698	xor v7, ve
0x069a	jp loc_0704
loc_069c:   ; == START OF CODE BLOCK ==
0x069c	ld v3, #40
0x069e	and v1, v3
0x06a0	sne v1, #00
0x06a2	jp loc_0704
0x06a4	drw vc, vd, #4
0x06a6	add vd, #02
0x06a8	drw vc, vd, #4
0x06aa	xor v7, ve
0x06ac	ld ve, #cf
0x06ae	and v7, ve
0x06b0	ld v2, #30
0x06b2	or v7, v2
0x06b4	ret
loc_06b6:   ; == START OF CODE BLOCK ==
0x06b6	ld v3, #10
0x06b8	and v1, v3
0x06ba	sne v1, #00
0x06bc	jp loc_0704
0x06be	drw vc, vd, #4
0x06c0	add vd, #fe
0x06c2	drw vc, vd, #4
0x06c4	xor v7, ve
0x06c6	ld ve, #cf
0x06c8	and v7, ve
0x06ca	ld v2, #00
0x06cc	or v7, v2
0x06ce	ret
loc_06d0:   ; == START OF CODE BLOCK ==
0x06d0	ld v3, #20
0x06d2	and v1, v3
0x06d4	sne v1, #00
0x06d6	jp loc_0704
0x06d8	drw vc, vd, #4
0x06da	add vc, #02
0x06dc	drw vc, vd, #4
0x06de	xor v7, ve
0x06e0	ld ve, #cf
0x06e2	and v7, ve
0x06e4	ld v2, #20
0x06e6	or v7, v2
0x06e8	ret
loc_06ea:   ; == START OF CODE BLOCK ==
0x06ea	ld v3, #80
0x06ec	and v1, v3
0x06ee	sne v1, #00
0x06f0	jp loc_0704
0x06f2	drw vc, vd, #4
0x06f4	add vc, #fe
0x06f6	drw vc, vd, #4
0x06f8	xor v7, ve
0x06fa	ld ve, #cf
0x06fc	and v7, ve
0x06fe	ld v2, #10
0x0700	or v7, v2
0x0702	ret
loc_0704:   ; == START OF CODE BLOCK ==
0x0704	rnd v1, #f0
0x0706	and v0, v1
0x0708	se v0, #00
0x070a	jp loc_0716
loc_070c:   ; == START OF CODE BLOCK ==
0x070c	xor v7, ve
0x070e	ld ve, #30
0x0710	xor v7, ve
0x0712	xor v2, ve
0x0714	jp loc_0636
loc_0716:   ; == START OF CODE BLOCK ==
0x0716	drw vc, vd, #4
0x0718	shl v0
0x071a	sne vf, #00
0x071c	jp loc_0724
0x071e	ld v2, #90
0x0720	add vc, #fe
0x0722	jp loc_0746
loc_0724:   ; == START OF CODE BLOCK ==
0x0724	shl v0
0x0726	sne vf, #00
0x0728	jp loc_0730
0x072a	ld v2, #30
0x072c	add vd, #02
0x072e	jp loc_0746
loc_0730:   ; == START OF CODE BLOCK ==
0x0730	shl v0
0x0732	sne vf, #00
0x0734	jp loc_073c
0x0736	ld v2, #a0
0x0738	add vc, #02
0x073a	jp loc_0746
loc_073c:   ; == START OF CODE BLOCK ==
0x073c	shl v0
0x073e	sne vf, #00
0x0740	jp loc_070c
0x0742	ld v2, #00
0x0744	add vd, #fe
loc_0746:   ; == START OF CODE BLOCK ==
0x0746	drw vc, vd, #4
0x0748	ld ve, #4f
0x074a	and v7, ve
0x074c	or v7, v2
0x074e	ret
loc_0750:   ; == START OF CODE BLOCK ==
0x0750	ld v0, v7
0x0752	ld ve, #03
0x0754	and v0, ve
0x0756	shl v0
0x0758	ld v1, v8
0x075a	add v1, v9
0x075c	ld ve, #02
0x075e	and v1, ve
0x0760	sne v1, #00
0x0762	add v0, #01
0x0764	shl v0
0x0766	shl v0
0x0768	ld I, #08cd
0x076a	add I, v0
0x076c	drw v8, v9, #4
0x076e	ld ve, vf
0x0770	ret
loc_0772:   ; == START OF CODE BLOCK ==
0x0772	ld ve, #00
loc_0774:   ; == START OF CODE BLOCK ==
0x0774	ld I, #0919
0x0776	add I, ve
0x0778	add I, ve
0x077a	add I, ve
0x077c	add I, ve
0x077e	ld v3, [I]
0x0780	ld I, #0b34
0x0782	add I, ve
0x0784	add I, ve
0x0786	add I, ve
0x0788	add I, ve
0x078a	ld [I], v3
0x078c	add ve, #01
0x078e	se ve, #80
0x0790	jp loc_0774
0x0792	ret
loc_0794:   ; == START OF CODE BLOCK ==
0x0794	xor v2, v2
0x0796	xor v3, v3
0x0798	ld ve, #0f
loc_079a:   ; == START OF CODE BLOCK ==
0x079a	ld v0, v2
0x079c	ld v1, v3
0x079e	call loc_07be
0x07a0	and v0, ve
0x07a2	shl v0
0x07a4	ld I, #08f9
0x07a6	add I, v0
0x07a8	drw v2, v3, #2
0x07aa	add v2, #02
0x07ac	se v2, #40
0x07ae	jp loc_079a
0x07b0	xor v2, v2
0x07b2	add v3, #02
0x07b4	sne v3, #20
0x07b6	ret
0x07b8	jp loc_079a
loc_07ba:   ; == START OF CODE BLOCK ==
0x07ba	add v0, #02
0x07bc	add v1, #02
loc_07be:   ; == START OF CODE BLOCK ==
0x07be	shr v0
0x07c0	shr v1
0x07c2	shl v1
0x07c4	shl v1
0x07c6	shl v1
0x07c8	shl v1
0x07ca	ld I, #0b34
0x07cc	add I, v1
0x07ce	add I, v1
0x07d0	add I, v0
0x07d2	ld v0, [I]
0x07d4	ret
loc_07d6:   ; == START OF CODE BLOCK ==
0x07d6	ld I, #08cc
0x07d8	ld v0, [I]
0x07da	shr v0
0x07dc	ld [I], v0
0x07de	ld v0, #01
loc_07e0:   ; == START OF CODE BLOCK ==
0x07e0	sknp v0
0x07e2	jp loc_07e0
0x07e4	ret
loc_07e6:   ; == START OF CODE BLOCK ==
0x07e6	ld v1, [I]
0x07e8	ld ve, #01
0x07ea	xor v4, v4
0x07ec	ld v2, v0
0x07ee	ld v3, v1
loc_07f0:   ; == START OF CODE BLOCK ==
0x07f0	ld v5, #10
0x07f2	sub v3, v5
0x07f4	sne vf, #00
0x07f6	sub v2, ve
0x07f8	sne vf, #00
0x07fa	jp loc_080c
0x07fc	ld v5, #27
0x07fe	sub v2, v5
0x0800	sne vf, #00
0x0802	jp loc_080c
0x0804	ld v0, v2
0x0806	ld v1, v3
0x0808	add v4, ve
0x080a	jp loc_07f0
loc_080c:   ; == START OF CODE BLOCK ==
0x080c	ld f, v4
0x080e	drw v6, v7, #5
0x0810	add v6, #06
0x0812	xor v4, v4
0x0814	ld v2, v0
0x0816	ld v3, v1
loc_0818:   ; == START OF CODE BLOCK ==
0x0818	ld v5, #e8
0x081a	sub v3, v5
0x081c	sne vf, #00
0x081e	sub v2, ve
0x0820	sne vf, #00
0x0822	jp loc_0834
0x0824	ld v5, #03
0x0826	sub v2, v5
0x0828	sne vf, #00
0x082a	jp loc_0834
0x082c	ld v0, v2
0x082e	ld v1, v3
0x0830	add v4, ve
0x0832	jp loc_0818
loc_0834:   ; == START OF CODE BLOCK ==
0x0834	ld f, v4
0x0836	drw v6, v7, #5
0x0838	add v6, #06
0x083a	xor v4, v4
0x083c	ld v2, v0
0x083e	ld v3, v1
loc_0840:   ; == START OF CODE BLOCK ==
0x0840	ld v5, #64
0x0842	sub v3, v5
0x0844	sne vf, #00
0x0846	sub v2, ve
0x0848	sne vf, #00
0x084a	jp loc_0854
0x084c	ld v0, v2
0x084e	ld v1, v3
0x0850	add v4, ve
0x0852	jp loc_0840
loc_0854:   ; == START OF CODE BLOCK ==
0x0854	ld f, v4
0x0856	drw v6, v7, #5
0x0858	add v6, #06
0x085a	xor v4, v4
0x085c	ld v2, v0
0x085e	ld v3, v1
loc_0860:   ; == START OF CODE BLOCK ==
0x0860	ld v5, #0a
0x0862	sub v3, v5
0x0864	sne vf, #00
0x0866	jp loc_086e
0x0868	ld v1, v3
0x086a	add v4, ve
0x086c	jp loc_0860
loc_086e:   ; == START OF CODE BLOCK ==
0x086e	ld f, v4
0x0870	drw v6, v7, #5
0x0872	add v6, #06
0x0874	ld f, v1
0x0876	drw v6, v7, #5
0x0878	ret
loc_087a:   ; == START OF CODE BLOCK ==
0x087a	ld I, #08c8
0x087c	ld v1, [I]
0x087e	add v1, ve
0x0880	se vf, #00
0x0882	add v0, #01
0x0884	ld I, #08c8
0x0886	ld [I], v1
0x0888	ret
loc_088a:   ; == START OF CODE BLOCK ==
0x088a	ld I, #08c8
0x088c	ld v3, [I]
0x088e	ld ve, v0
0x0890	sub ve, v2
0x0892	sne vf, #00
0x0894	ret
0x0896	se ve, #00
0x0898	jp loc_08a2
0x089a	ld ve, v1
0x089c	sub ve, v3
0x089e	sne vf, #00
0x08a0	ret
loc_08a2:   ; == START OF CODE BLOCK ==
0x08a2	ld I, #08ca
0x08a4	ld [I], v1
0x08a6	ret
loc_08a8:   ; == START OF CODE BLOCK ==
0x08a8	xor ve, ve
0x08aa	ld v2, #0f
0x08ac	ld v3, #ff
0x08ae	ld v1, #10
loc_08b0:   ; == START OF CODE BLOCK ==
0x08b0	sknp v2
0x08b2	jp loc_08c4
0x08b4	add v1, v3
0x08b6	se v1, #00
0x08b8	jp loc_08b0
0x08ba	ld v1, #10
0x08bc	add v0, v3
0x08be	se v0, #00
0x08c0	jp loc_08b0
0x08c2	ret
loc_08c4:   ; == START OF CODE BLOCK ==
0x08c4	ld ve, #01
0x08c6	ret
0x08c8	db #00	;GRAPHIC =         
0x08c9	db #00	;GRAPHIC =         
0x08ca	db #00	;GRAPHIC =         
0x08cb	db #00	;GRAPHIC =         
0x08cc	db #05	;GRAPHIC =      # #
0x08cd	db #00	;GRAPHIC =         
0x08ce	db #50	;GRAPHIC =  # #    	ASCII(P)
0x08cf	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08d0	db #20	;GRAPHIC =   #     
0x08d1	db #00	;GRAPHIC =         
0x08d2	db #50	;GRAPHIC =  # #    	ASCII(P)
0x08d3	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08d4	db #20	;GRAPHIC =   #     
0x08d5	db #00	;GRAPHIC =         
0x08d6	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08d7	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08d8	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08d9	db #00	;GRAPHIC =         
0x08da	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08db	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08dc	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08dd	db #00	;GRAPHIC =         
0x08de	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08df	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08e0	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08e1	db #00	;GRAPHIC =         
0x08e2	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08e3	db #60	;GRAPHIC =  ##     	ASCII(`)
0x08e4	db #30	;GRAPHIC =   ##    	ASCII(0)
0x08e5	db #00	;GRAPHIC =         
0x08e6	db #20	;GRAPHIC =   #     
0x08e7	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08e8	db #50	;GRAPHIC =  # #    	ASCII(P)
0x08e9	db #00	;GRAPHIC =         
0x08ea	db #20	;GRAPHIC =   #     
0x08eb	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08ec	db #50	;GRAPHIC =  # #    	ASCII(P)
0x08ed	db #00	;GRAPHIC =         
0x08ee	db #20	;GRAPHIC =   #     
0x08ef	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08f0	db #70	;GRAPHIC =  ###    	ASCII(p)
0x08f1	db #00	;GRAPHIC =         
0x08f2	db #00	;GRAPHIC =         
0x08f3	db #20	;GRAPHIC =   #     
0x08f4	db #00	;GRAPHIC =         
0x08f5	db #00	;GRAPHIC =         
0x08f6	db #00	;GRAPHIC =         
0x08f7	db #00	;GRAPHIC =         
0x08f8	db #00	;GRAPHIC =         
0x08f9	db #00	;GRAPHIC =         
0x08fa	db #00	;GRAPHIC =         
0x08fb	db #00	;GRAPHIC =         
0x08fc	db #00	;GRAPHIC =         
0x08fd	db #00	;GRAPHIC =         
0x08fe	db #00	;GRAPHIC =         
0x08ff	db #00	;GRAPHIC =         
0x0900	db #00	;GRAPHIC =         
0x0901	db #00	;GRAPHIC =         
0x0902	db #00	;GRAPHIC =         
0x0903	db #80	;GRAPHIC = #       
0x0904	db #00	;GRAPHIC =         
0x0905	db #00	;GRAPHIC =         
0x0906	db #00	;GRAPHIC =         
0x0907	db #00	;GRAPHIC =         
0x0908	db #00	;GRAPHIC =         
0x0909	db #c0	;GRAPHIC = ##      
0x090a	db #00	;GRAPHIC =         
0x090b	db #00	;GRAPHIC =         
0x090c	db #00	;GRAPHIC =         
0x090d	db #80	;GRAPHIC = #       
0x090e	db #80	;GRAPHIC = #       
0x090f	db #00	;GRAPHIC =         
0x0910	db #00	;GRAPHIC =         
0x0911	db #c0	;GRAPHIC = ##      
0x0912	db #80	;GRAPHIC = #       
0x0913	db #80	;GRAPHIC = #       
0x0914	db #80	;GRAPHIC = #       
0x0915	db #c0	;GRAPHIC = ##      
0x0916	db #00	;GRAPHIC =         
0x0917	db #80	;GRAPHIC = #       
0x0918	db #00	;GRAPHIC =         
0x0919	db #0c	;GRAPHIC =     ##  
0x091a	db #08	;GRAPHIC =     #   
0x091b	db #08	;GRAPHIC =     #   
0x091c	db #08	;GRAPHIC =     #   
0x091d	db #08	;GRAPHIC =     #   
0x091e	db #08	;GRAPHIC =     #   
0x091f	db #08	;GRAPHIC =     #   
0x0920	db #08	;GRAPHIC =     #   
0x0921	db #08	;GRAPHIC =     #   
0x0922	db #08	;GRAPHIC =     #   
0x0923	db #08	;GRAPHIC =     #   
0x0924	db #08	;GRAPHIC =     #   
0x0925	db #08	;GRAPHIC =     #   
0x0926	db #08	;GRAPHIC =     #   
0x0927	db #08	;GRAPHIC =     #   
0x0928	db #0d	;GRAPHIC =     ## #
0x0929	db #0c	;GRAPHIC =     ##  
0x092a	db #08	;GRAPHIC =     #   
0x092b	db #08	;GRAPHIC =     #   
0x092c	db #08	;GRAPHIC =     #   
0x092d	db #08	;GRAPHIC =     #   
0x092e	db #08	;GRAPHIC =     #   
0x092f	db #08	;GRAPHIC =     #   
0x0930	db #08	;GRAPHIC =     #   
0x0931	db #08	;GRAPHIC =     #   
0x0932	db #08	;GRAPHIC =     #   
0x0933	db #08	;GRAPHIC =     #   
0x0934	db #08	;GRAPHIC =     #   
0x0935	db #08	;GRAPHIC =     #   
0x0936	db #08	;GRAPHIC =     #   
0x0937	db #08	;GRAPHIC =     #   
0x0938	db #0d	;GRAPHIC =     ## #
0x0939	db #0a	;GRAPHIC =     # # 
0x093a	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x093b	db #05	;GRAPHIC =      # #
0x093c	db #05	;GRAPHIC =      # #
0x093d	db #05	;GRAPHIC =      # #
0x093e	db #05	;GRAPHIC =      # #
0x093f	db #e5	;GRAPHIC = ###  # #
0x0940	db #05	;GRAPHIC =      # #
0x0941	db #05	;GRAPHIC =      # #
0x0942	db #e5	;GRAPHIC = ###  # #
0x0943	db #05	;GRAPHIC =      # #
0x0944	db #05	;GRAPHIC =      # #
0x0945	db #05	;GRAPHIC =      # #
0x0946	db #05	;GRAPHIC =      # #
0x0947	db #c5	;GRAPHIC = ##   # #
0x0948	db #0a	;GRAPHIC =     # # 
0x0949	db #0a	;GRAPHIC =     # # 
0x094a	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x094b	db #05	;GRAPHIC =      # #
0x094c	db #05	;GRAPHIC =      # #
0x094d	db #05	;GRAPHIC =      # #
0x094e	db #05	;GRAPHIC =      # #
0x094f	db #e5	;GRAPHIC = ###  # #
0x0950	db #05	;GRAPHIC =      # #
0x0951	db #05	;GRAPHIC =      # #
0x0952	db #e5	;GRAPHIC = ###  # #
0x0953	db #05	;GRAPHIC =      # #
0x0954	db #05	;GRAPHIC =      # #
0x0955	db #05	;GRAPHIC =      # #
0x0956	db #05	;GRAPHIC =      # #
0x0957	db #c5	;GRAPHIC = ##   # #
0x0958	db #0a	;GRAPHIC =     # # 
0x0959	db #0a	;GRAPHIC =     # # 
0x095a	db #05	;GRAPHIC =      # #
0x095b	db #0c	;GRAPHIC =     ##  
0x095c	db #08	;GRAPHIC =     #   
0x095d	db #08	;GRAPHIC =     #   
0x095e	db #0f	;GRAPHIC =     ####
0x095f	db #05	;GRAPHIC =      # #
0x0960	db #0c	;GRAPHIC =     ##  
0x0961	db #0d	;GRAPHIC =     ## #
0x0962	db #05	;GRAPHIC =      # #
0x0963	db #08	;GRAPHIC =     #   
0x0964	db #08	;GRAPHIC =     #   
0x0965	db #08	;GRAPHIC =     #   
0x0966	db #0d	;GRAPHIC =     ## #
0x0967	db #05	;GRAPHIC =      # #
0x0968	db #0e	;GRAPHIC =     ### 
0x0969	db #0f	;GRAPHIC =     ####
0x096a	db #05	;GRAPHIC =      # #
0x096b	db #0c	;GRAPHIC =     ##  
0x096c	db #08	;GRAPHIC =     #   
0x096d	db #08	;GRAPHIC =     #   
0x096e	db #0f	;GRAPHIC =     ####
0x096f	db #05	;GRAPHIC =      # #
0x0970	db #0c	;GRAPHIC =     ##  
0x0971	db #0d	;GRAPHIC =     ## #
0x0972	db #05	;GRAPHIC =      # #
0x0973	db #08	;GRAPHIC =     #   
0x0974	db #08	;GRAPHIC =     #   
0x0975	db #08	;GRAPHIC =     #   
0x0976	db #0d	;GRAPHIC =     ## #
0x0977	db #05	;GRAPHIC =      # #
0x0978	db #0a	;GRAPHIC =     # # 
0x0979	db #0a	;GRAPHIC =     # # 
0x097a	db #05	;GRAPHIC =      # #
0x097b	db #0a	;GRAPHIC =     # # 
0x097c	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x097d	db #06	;GRAPHIC =      ## 
0x097e	db #05	;GRAPHIC =      # #
0x097f	db #95	;GRAPHIC = #  # # #
0x0980	db #0a	;GRAPHIC =     # # 
0x0981	db #0a	;GRAPHIC =     # # 
0x0982	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0983	db #05	;GRAPHIC =      # #
0x0984	db #05	;GRAPHIC =      # #
0x0985	db #c5	;GRAPHIC = ##   # #
0x0986	db #0a	;GRAPHIC =     # # 
0x0987	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0988	db #05	;GRAPHIC =      # #
0x0989	db #05	;GRAPHIC =      # #
0x098a	db #95	;GRAPHIC = #  # # #
0x098b	db #0a	;GRAPHIC =     # # 
0x098c	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x098d	db #05	;GRAPHIC =      # #
0x098e	db #05	;GRAPHIC =      # #
0x098f	db #95	;GRAPHIC = #  # # #
0x0990	db #0a	;GRAPHIC =     # # 
0x0991	db #0a	;GRAPHIC =     # # 
0x0992	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0993	db #05	;GRAPHIC =      # #
0x0994	db #06	;GRAPHIC =      ## 
0x0995	db #c5	;GRAPHIC = ##   # #
0x0996	db #0a	;GRAPHIC =     # # 
0x0997	db #05	;GRAPHIC =      # #
0x0998	db #0a	;GRAPHIC =     # # 
0x0999	db #0a	;GRAPHIC =     # # 
0x099a	db #05	;GRAPHIC =      # #
0x099b	db #0f	;GRAPHIC =     ####
0x099c	db #05	;GRAPHIC =      # #
0x099d	db #08	;GRAPHIC =     #   
0x099e	db #08	;GRAPHIC =     #   
0x099f	db #08	;GRAPHIC =     #   
0x09a0	db #08	;GRAPHIC =     #   
0x09a1	db #08	;GRAPHIC =     #   
0x09a2	db #0c	;GRAPHIC =     ##  
0x09a3	db #08	;GRAPHIC =     #   
0x09a4	db #0f	;GRAPHIC =     ####
0x09a5	db #05	;GRAPHIC =      # #
0x09a6	db #08	;GRAPHIC =     #   
0x09a7	db #08	;GRAPHIC =     #   
0x09a8	db #08	;GRAPHIC =     #   
0x09a9	db #08	;GRAPHIC =     #   
0x09aa	db #08	;GRAPHIC =     #   
0x09ab	db #0f	;GRAPHIC =     ####
0x09ac	db #05	;GRAPHIC =      # #
0x09ad	db #08	;GRAPHIC =     #   
0x09ae	db #08	;GRAPHIC =     #   
0x09af	db #0c	;GRAPHIC =     ##  
0x09b0	db #08	;GRAPHIC =     #   
0x09b1	db #08	;GRAPHIC =     #   
0x09b2	db #08	;GRAPHIC =     #   
0x09b3	db #08	;GRAPHIC =     #   
0x09b4	db #0f	;GRAPHIC =     ####
0x09b5	db #05	;GRAPHIC =      # #
0x09b6	db #0f	;GRAPHIC =     ####
0x09b7	db #05	;GRAPHIC =      # #
0x09b8	db #0a	;GRAPHIC =     # # 
0x09b9	db #0a	;GRAPHIC =     # # 
0x09ba	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x09bb	db #05	;GRAPHIC =      # #
0x09bc	db #b5	;GRAPHIC = # ## # #
0x09bd	db #05	;GRAPHIC =      # #
0x09be	db #05	;GRAPHIC =      # #
0x09bf	db #05	;GRAPHIC =      # #
0x09c0	db #05	;GRAPHIC =      # #
0x09c1	db #c5	;GRAPHIC = ##   # #
0x09c2	db #0a	;GRAPHIC =     # # 
0x09c3	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x09c4	db #05	;GRAPHIC =      # #
0x09c5	db #b5	;GRAPHIC = # ## # #
0x09c6	db #05	;GRAPHIC =      # #
0x09c7	db #e5	;GRAPHIC = ###  # #
0x09c8	db #05	;GRAPHIC =      # #
0x09c9	db #05	;GRAPHIC =      # #
0x09ca	db #e5	;GRAPHIC = ###  # #
0x09cb	db #05	;GRAPHIC =      # #
0x09cc	db #b5	;GRAPHIC = # ## # #
0x09cd	db #05	;GRAPHIC =      # #
0x09ce	db #c5	;GRAPHIC = ##   # #
0x09cf	db #0a	;GRAPHIC =     # # 
0x09d0	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x09d1	db #05	;GRAPHIC =      # #
0x09d2	db #05	;GRAPHIC =      # #
0x09d3	db #05	;GRAPHIC =      # #
0x09d4	db #05	;GRAPHIC =      # #
0x09d5	db #b5	;GRAPHIC = # ## # #
0x09d6	db #05	;GRAPHIC =      # #
0x09d7	db #d5	;GRAPHIC = ## # # #
0x09d8	db #0a	;GRAPHIC =     # # 
0x09d9	db #0a	;GRAPHIC =     # # 
0x09da	db #05	;GRAPHIC =      # #
0x09db	db #0c	;GRAPHIC =     ##  
0x09dc	db #08	;GRAPHIC =     #   
0x09dd	db #08	;GRAPHIC =     #   
0x09de	db #08	;GRAPHIC =     #   
0x09df	db #08	;GRAPHIC =     #   
0x09e0	db #0d	;GRAPHIC =     ## #
0x09e1	db #05	;GRAPHIC =      # #
0x09e2	db #0f	;GRAPHIC =     ####
0x09e3	db #05	;GRAPHIC =      # #
0x09e4	db #0c	;GRAPHIC =     ##  
0x09e5	db #08	;GRAPHIC =     #   
0x09e6	db #0f	;GRAPHIC =     ####
0x09e7	db #05	;GRAPHIC =      # #
0x09e8	db #08	;GRAPHIC =     #   
0x09e9	db #0f	;GRAPHIC =     ####
0x09ea	db #05	;GRAPHIC =      # #
0x09eb	db #08	;GRAPHIC =     #   
0x09ec	db #08	;GRAPHIC =     #   
0x09ed	db #0d	;GRAPHIC =     ## #
0x09ee	db #05	;GRAPHIC =      # #
0x09ef	db #0f	;GRAPHIC =     ####
0x09f0	db #05	;GRAPHIC =      # #
0x09f1	db #0c	;GRAPHIC =     ##  
0x09f2	db #08	;GRAPHIC =     #   
0x09f3	db #08	;GRAPHIC =     #   
0x09f4	db #08	;GRAPHIC =     #   
0x09f5	db #08	;GRAPHIC =     #   
0x09f6	db #0d	;GRAPHIC =     ## #
0x09f7	db #05	;GRAPHIC =      # #
0x09f8	db #0a	;GRAPHIC =     # # 
0x09f9	db #0f	;GRAPHIC =     ####
0x09fa	db #05	;GRAPHIC =      # #
0x09fb	db #0f	;GRAPHIC =     ####
0x09fc	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x09fd	db #05	;GRAPHIC =      # #
0x09fe	db #05	;GRAPHIC =      # #
0x09ff	db #c5	;GRAPHIC = ##   # #
0x0a00	db #0a	;GRAPHIC =     # # 
0x0a01	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0a02	db #e5	;GRAPHIC = ###  # #
0x0a03	db #95	;GRAPHIC = #  # # #
0x0a04	db #0a	;GRAPHIC =     # # 
0x0a05	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x0a06	db #05	;GRAPHIC =      # #
0x0a07	db #b0	;GRAPHIC = # ##    
0x0a08	db #05	;GRAPHIC =      # #
0x0a09	db #05	;GRAPHIC =      # #
0x0a0a	db #b5	;GRAPHIC = # ## # #
0x0a0b	db #05	;GRAPHIC =      # #
0x0a0c	db #c5	;GRAPHIC = ##   # #
0x0a0d	db #0a	;GRAPHIC =     # # 
0x0a0e	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0a0f	db #e5	;GRAPHIC = ###  # #
0x0a10	db #95	;GRAPHIC = #  # # #
0x0a11	db #0a	;GRAPHIC =     # # 
0x0a12	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x0a13	db #05	;GRAPHIC =      # #
0x0a14	db #05	;GRAPHIC =      # #
0x0a15	db #c5	;GRAPHIC = ##   # #
0x0a16	db #0f	;GRAPHIC =     ####
0x0a17	db #05	;GRAPHIC =      # #
0x0a18	db #0f	;GRAPHIC =     ####
0x0a19	db #07	;GRAPHIC =      ###
0x0a1a	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0a1b	db #05	;GRAPHIC =      # #
0x0a1c	db #d5	;GRAPHIC = ## # # #
0x0a1d	db #08	;GRAPHIC =     #   
0x0a1e	db #0f	;GRAPHIC =     ####
0x0a1f	db #05	;GRAPHIC =      # #
0x0a20	db #0e	;GRAPHIC =     ### 
0x0a21	db #0f	;GRAPHIC =     ####
0x0a22	db #05	;GRAPHIC =      # #
0x0a23	db #08	;GRAPHIC =     #   
0x0a24	db #0f	;GRAPHIC =     ####
0x0a25	db #05	;GRAPHIC =      # #
0x0a26	db #0c	;GRAPHIC =     ##  
0x0a27	db #08	;GRAPHIC =     #   
0x0a28	db #08	;GRAPHIC =     #   
0x0a29	db #08	;GRAPHIC =     #   
0x0a2a	db #08	;GRAPHIC =     #   
0x0a2b	db #0d	;GRAPHIC =     ## #
0x0a2c	db #05	;GRAPHIC =      # #
0x0a2d	db #08	;GRAPHIC =     #   
0x0a2e	db #0f	;GRAPHIC =     ####
0x0a2f	db #05	;GRAPHIC =      # #
0x0a30	db #08	;GRAPHIC =     #   
0x0a31	db #0f	;GRAPHIC =     ####
0x0a32	db #05	;GRAPHIC =      # #
0x0a33	db #08	;GRAPHIC =     #   
0x0a34	db #0f	;GRAPHIC =     ####
0x0a35	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x0a36	db #05	;GRAPHIC =      # #
0x0a37	db #d4	;GRAPHIC = ## # #  
0x0a38	db #07	;GRAPHIC =      ###
0x0a39	db #0a	;GRAPHIC =     # # 
0x0a3a	db #05	;GRAPHIC =      # #
0x0a3b	db #0a	;GRAPHIC =     # # 
0x0a3c	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0a3d	db #05	;GRAPHIC =      # #
0x0a3e	db #05	;GRAPHIC =      # #
0x0a3f	db #f5	;GRAPHIC = #### # #
0x0a40	db #05	;GRAPHIC =      # #
0x0a41	db #05	;GRAPHIC =      # #
0x0a42	db #b5	;GRAPHIC = # ## # #
0x0a43	db #05	;GRAPHIC =      # #
0x0a44	db #05	;GRAPHIC =      # #
0x0a45	db #d5	;GRAPHIC = ## # # #
0x0a46	db #08	;GRAPHIC =     #   
0x0a47	db #08	;GRAPHIC =     #   
0x0a48	db #0d	;GRAPHIC =     ## #
0x0a49	db #0c	;GRAPHIC =     ##  
0x0a4a	db #08	;GRAPHIC =     #   
0x0a4b	db #0f	;GRAPHIC =     ####
0x0a4c	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x0a4d	db #05	;GRAPHIC =      # #
0x0a4e	db #05	;GRAPHIC =      # #
0x0a4f	db #b5	;GRAPHIC = # ## # #
0x0a50	db #05	;GRAPHIC =      # #
0x0a51	db #05	;GRAPHIC =      # #
0x0a52	db #f5	;GRAPHIC = #### # #
0x0a53	db #05	;GRAPHIC =      # #
0x0a54	db #05	;GRAPHIC =      # #
0x0a55	db #95	;GRAPHIC = #  # # #
0x0a56	db #0a	;GRAPHIC =     # # 
0x0a57	db #05	;GRAPHIC =      # #
0x0a58	db #0a	;GRAPHIC =     # # 
0x0a59	db #0a	;GRAPHIC =     # # 
0x0a5a	db #05	;GRAPHIC =      # #
0x0a5b	db #08	;GRAPHIC =     #   
0x0a5c	db #08	;GRAPHIC =     #   
0x0a5d	db #08	;GRAPHIC =     #   
0x0a5e	db #0d	;GRAPHIC =     ## #
0x0a5f	db #05	;GRAPHIC =      # #
0x0a60	db #0c	;GRAPHIC =     ##  
0x0a61	db #08	;GRAPHIC =     #   
0x0a62	db #08	;GRAPHIC =     #   
0x0a63	db #08	;GRAPHIC =     #   
0x0a64	db #0d	;GRAPHIC =     ## #
0x0a65	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0a66	db #05	;GRAPHIC =      # #
0x0a67	db #c5	;GRAPHIC = ##   # #
0x0a68	db #0a	;GRAPHIC =     # # 
0x0a69	db #0a	;GRAPHIC =     # # 
0x0a6a	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x0a6b	db #05	;GRAPHIC =      # #
0x0a6c	db #95	;GRAPHIC = #  # # #
0x0a6d	db #0c	;GRAPHIC =     ##  
0x0a6e	db #08	;GRAPHIC =     #   
0x0a6f	db #08	;GRAPHIC =     #   
0x0a70	db #08	;GRAPHIC =     #   
0x0a71	db #0d	;GRAPHIC =     ## #
0x0a72	db #05	;GRAPHIC =      # #
0x0a73	db #0c	;GRAPHIC =     ##  
0x0a74	db #08	;GRAPHIC =     #   
0x0a75	db #08	;GRAPHIC =     #   
0x0a76	db #0f	;GRAPHIC =     ####
0x0a77	db #05	;GRAPHIC =      # #
0x0a78	db #0a	;GRAPHIC =     # # 
0x0a79	db #0a	;GRAPHIC =     # # 
0x0a7a	db #75	;GRAPHIC =  ### # #	ASCII(u)
0x0a7b	db #05	;GRAPHIC =      # #
0x0a7c	db #06	;GRAPHIC =      ## 
0x0a7d	db #c5	;GRAPHIC = ##   # #
0x0a7e	db #0a	;GRAPHIC =     # # 
0x0a7f	db #05	;GRAPHIC =      # #
0x0a80	db #08	;GRAPHIC =     #   
0x0a81	db #08	;GRAPHIC =     #   
0x0a82	db #08	;GRAPHIC =     #   
0x0a83	db #08	;GRAPHIC =     #   
0x0a84	db #08	;GRAPHIC =     #   
0x0a85	db #08	;GRAPHIC =     #   
0x0a86	db #0f	;GRAPHIC =     ####
0x0a87	db #05	;GRAPHIC =      # #
0x0a88	db #08	;GRAPHIC =     #   
0x0a89	db #0f	;GRAPHIC =     ####
0x0a8a	db #05	;GRAPHIC =      # #
0x0a8b	db #08	;GRAPHIC =     #   
0x0a8c	db #08	;GRAPHIC =     #   
0x0a8d	db #08	;GRAPHIC =     #   
0x0a8e	db #08	;GRAPHIC =     #   
0x0a8f	db #08	;GRAPHIC =     #   
0x0a90	db #08	;GRAPHIC =     #   
0x0a91	db #0f	;GRAPHIC =     ####
0x0a92	db #05	;GRAPHIC =      # #
0x0a93	db #0a	;GRAPHIC =     # # 
0x0a94	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x0a95	db #06	;GRAPHIC =      ## 
0x0a96	db #05	;GRAPHIC =      # #
0x0a97	db #d5	;GRAPHIC = ## # # #
0x0a98	db #0a	;GRAPHIC =     # # 
0x0a99	db #0a	;GRAPHIC =     # # 
0x0a9a	db #05	;GRAPHIC =      # #
0x0a9b	db #0c	;GRAPHIC =     ##  
0x0a9c	db #0d	;GRAPHIC =     ## #
0x0a9d	db #05	;GRAPHIC =      # #
0x0a9e	db #0a	;GRAPHIC =     # # 
0x0a9f	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0aa0	db #05	;GRAPHIC =      # #
0x0aa1	db #05	;GRAPHIC =      # #
0x0aa2	db #05	;GRAPHIC =      # #
0x0aa3	db #05	;GRAPHIC =      # #
0x0aa4	db #e5	;GRAPHIC = ###  # #
0x0aa5	db #05	;GRAPHIC =      # #
0x0aa6	db #05	;GRAPHIC =      # #
0x0aa7	db #f5	;GRAPHIC = #### # #
0x0aa8	db #05	;GRAPHIC =      # #
0x0aa9	db #05	;GRAPHIC =      # #
0x0aaa	db #f5	;GRAPHIC = #### # #
0x0aab	db #05	;GRAPHIC =      # #
0x0aac	db #05	;GRAPHIC =      # #
0x0aad	db #e5	;GRAPHIC = ###  # #
0x0aae	db #05	;GRAPHIC =      # #
0x0aaf	db #05	;GRAPHIC =      # #
0x0ab0	db #05	;GRAPHIC =      # #
0x0ab1	db #05	;GRAPHIC =      # #
0x0ab2	db #95	;GRAPHIC = #  # # #
0x0ab3	db #0a	;GRAPHIC =     # # 
0x0ab4	db #05	;GRAPHIC =      # #
0x0ab5	db #0c	;GRAPHIC =     ##  
0x0ab6	db #0d	;GRAPHIC =     ## #
0x0ab7	db #05	;GRAPHIC =      # #
0x0ab8	db #0a	;GRAPHIC =     # # 
0x0ab9	db #0a	;GRAPHIC =     # # 
0x0aba	db #05	;GRAPHIC =      # #
0x0abb	db #08	;GRAPHIC =     #   
0x0abc	db #0f	;GRAPHIC =     ####
0x0abd	db #05	;GRAPHIC =      # #
0x0abe	db #08	;GRAPHIC =     #   
0x0abf	db #08	;GRAPHIC =     #   
0x0ac0	db #08	;GRAPHIC =     #   
0x0ac1	db #08	;GRAPHIC =     #   
0x0ac2	db #08	;GRAPHIC =     #   
0x0ac3	db #0f	;GRAPHIC =     ####
0x0ac4	db #05	;GRAPHIC =      # #
0x0ac5	db #0c	;GRAPHIC =     ##  
0x0ac6	db #0d	;GRAPHIC =     ## #
0x0ac7	db #05	;GRAPHIC =      # #
0x0ac8	db #08	;GRAPHIC =     #   
0x0ac9	db #0f	;GRAPHIC =     ####
0x0aca	db #05	;GRAPHIC =      # #
0x0acb	db #0c	;GRAPHIC =     ##  
0x0acc	db #0d	;GRAPHIC =     ## #
0x0acd	db #05	;GRAPHIC =      # #
0x0ace	db #08	;GRAPHIC =     #   
0x0acf	db #08	;GRAPHIC =     #   
0x0ad0	db #08	;GRAPHIC =     #   
0x0ad1	db #08	;GRAPHIC =     #   
0x0ad2	db #08	;GRAPHIC =     #   
0x0ad3	db #0f	;GRAPHIC =     ####
0x0ad4	db #05	;GRAPHIC =      # #
0x0ad5	db #08	;GRAPHIC =     #   
0x0ad6	db #0f	;GRAPHIC =     ####
0x0ad7	db #05	;GRAPHIC =      # #
0x0ad8	db #0a	;GRAPHIC =     # # 
0x0ad9	db #0a	;GRAPHIC =     # # 
0x0ada	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0adb	db #05	;GRAPHIC =      # #
0x0adc	db #05	;GRAPHIC =      # #
0x0add	db #b5	;GRAPHIC = # ## # #
0x0ade	db #05	;GRAPHIC =      # #
0x0adf	db #05	;GRAPHIC =      # #
0x0ae0	db #05	;GRAPHIC =      # #
0x0ae1	db #05	;GRAPHIC =      # #
0x0ae2	db #05	;GRAPHIC =      # #
0x0ae3	db #05	;GRAPHIC =      # #
0x0ae4	db #95	;GRAPHIC = #  # # #
0x0ae5	db #0a	;GRAPHIC =     # # 
0x0ae6	db #0a	;GRAPHIC =     # # 
0x0ae7	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0ae8	db #05	;GRAPHIC =      # #
0x0ae9	db #05	;GRAPHIC =      # #
0x0aea	db #95	;GRAPHIC = #  # # #
0x0aeb	db #0a	;GRAPHIC =     # # 
0x0aec	db #0a	;GRAPHIC =     # # 
0x0aed	db #35	;GRAPHIC =   ## # #	ASCII(5)
0x0aee	db #05	;GRAPHIC =      # #
0x0aef	db #05	;GRAPHIC =      # #
0x0af0	db #05	;GRAPHIC =      # #
0x0af1	db #05	;GRAPHIC =      # #
0x0af2	db #05	;GRAPHIC =      # #
0x0af3	db #05	;GRAPHIC =      # #
0x0af4	db #b5	;GRAPHIC = # ## # #
0x0af5	db #05	;GRAPHIC =      # #
0x0af6	db #05	;GRAPHIC =      # #
0x0af7	db #95	;GRAPHIC = #  # # #
0x0af8	db #0a	;GRAPHIC =     # # 
0x0af9	db #08	;GRAPHIC =     #   
0x0afa	db #08	;GRAPHIC =     #   
0x0afb	db #08	;GRAPHIC =     #   
0x0afc	db #08	;GRAPHIC =     #   
0x0afd	db #08	;GRAPHIC =     #   
0x0afe	db #08	;GRAPHIC =     #   
0x0aff	db #08	;GRAPHIC =     #   
0x0b00	db #08	;GRAPHIC =     #   
0x0b01	db #08	;GRAPHIC =     #   
0x0b02	db #08	;GRAPHIC =     #   
0x0b03	db #08	;GRAPHIC =     #   
0x0b04	db #08	;GRAPHIC =     #   
0x0b05	db #0f	;GRAPHIC =     ####
0x0b06	db #08	;GRAPHIC =     #   
0x0b07	db #08	;GRAPHIC =     #   
0x0b08	db #08	;GRAPHIC =     #   
0x0b09	db #08	;GRAPHIC =     #   
0x0b0a	db #08	;GRAPHIC =     #   
0x0b0b	db #0f	;GRAPHIC =     ####
0x0b0c	db #08	;GRAPHIC =     #   
0x0b0d	db #08	;GRAPHIC =     #   
0x0b0e	db #08	;GRAPHIC =     #   
0x0b0f	db #08	;GRAPHIC =     #   
0x0b10	db #08	;GRAPHIC =     #   
0x0b11	db #08	;GRAPHIC =     #   
0x0b12	db #08	;GRAPHIC =     #   
0x0b13	db #08	;GRAPHIC =     #   
0x0b14	db #08	;GRAPHIC =     #   
0x0b15	db #08	;GRAPHIC =     #   
0x0b16	db #08	;GRAPHIC =     #   
0x0b17	db #08	;GRAPHIC =     #   
0x0b18	db #0f	;GRAPHIC =     ####
0x0b19	db #3c	;GRAPHIC =   ####  	ASCII(<)
0x0b1a	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0b1b	db #99	;GRAPHIC = #  ##  #
0x0b1c	db #99	;GRAPHIC = #  ##  #
0x0b1d	db #42	;GRAPHIC =  #    # 	ASCII(B)
0x0b1e	db #3c	;GRAPHIC =   ####  	ASCII(<)
0x0b1f	db #01	;GRAPHIC =        #
0x0b20	db #10	;GRAPHIC =    #    
0x0b21	db #0f	;GRAPHIC =     ####
0x0b22	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0b23	db #84	;GRAPHIC = #    #  
0x0b24	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x0b25	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x0b26	db #84	;GRAPHIC = #    #  
0x0b27	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0b28	db #00	;GRAPHIC =         
0x0b29	db #10	;GRAPHIC =    #    
0x0b2a	db #e0	;GRAPHIC = ###     
0x0b2b	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0b2c	db #fc	;GRAPHIC = ######  
0x0b2d	db #fe	;GRAPHIC = ####### 
0x0b2e	db #fe	;GRAPHIC = ####### 
0x0b2f	db #84	;GRAPHIC = #    #  
0x0b30	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0b31	db #00	;GRAPHIC =         
0x0b32	db #10	;GRAPHIC =    #    
0x0b33	db #e0	;GRAPHIC = ###     
