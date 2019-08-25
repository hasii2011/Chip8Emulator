; Setting used by the chipper assembler
option schip11
option binary
align off

; Recursive Disassembly
End of file
0x0200	jp loc_0212
0x0202	db #20	;GRAPHIC =   #     
0x0203	db #54	;GRAPHIC =  # # #  	ASCII(T)
0x0204	db #72	;GRAPHIC =  ###  # 	ASCII(r)
0x0205	db #6f	;GRAPHIC =  ## ####	ASCII(o)
0x0206	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x0207	db #69	;GRAPHIC =  ## #  #	ASCII(i)
0x0208	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0209	db #20	;GRAPHIC =   #     
0x020a	db #28	;GRAPHIC =   # #   	ASCII(()
0x020b	db #63	;GRAPHIC =  ##   ##	ASCII(c)
0x020c	db #29	;GRAPHIC =   # #  #	ASCII())
0x020d	db #20	;GRAPHIC =   #     
0x020e	db #32	;GRAPHIC =   ##  # 	ASCII(2)
0x020f	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0210	db #31	;GRAPHIC =   ##   #	ASCII(1)
0x0211	db #30	;GRAPHIC =   ##    	ASCII(0)
loc_0212:   ; == START OF CODE BLOCK ==
0x0212	cls
0x0214	se vf, #00
0x0216	jp loc_03e2
0x0218	se ve, #00
0x021a	jp loc_03e2
0x021c	se vd, #00
0x021e	jp loc_03e2
0x0220	se vc, #00
0x0222	jp loc_03e2
0x0224	se vb, #00
0x0226	jp loc_03e2
0x0228	se va, #00
0x022a	jp loc_03e2
0x022c	se v9, #00
0x022e	jp loc_03e2
0x0230	se v8, #00
0x0232	jp loc_03e2
0x0234	se v7, #00
0x0236	jp loc_03e2
0x0238	se v6, #00
0x023a	jp loc_03e2
0x023c	se v5, #00
0x023e	jp loc_03e2
0x0240	se v4, #00
0x0242	jp loc_03e2
0x0244	se v3, #00
0x0246	jp loc_03e2
0x0248	se v2, #00
0x024a	jp loc_03e2
0x024c	se v1, #00
0x024e	jp loc_03e2
0x0250	se v0, #00
0x0252	jp loc_03e2
0x0254	ld v0, #00
0x0256	ld v1, #01
0x0258	ld v2, #02
0x025a	ld v3, #03
0x025c	ld v4, #04
0x025e	ld v5, #05
0x0260	ld v6, #06
0x0262	ld v7, #07
0x0264	ld v8, #08
0x0266	ld v9, #09
0x0268	ld va, #0a
0x026a	ld vb, #0b
0x026c	ld vc, #0c
0x026e	ld vd, #0d
0x0270	ld ve, #0e
0x0272	ld vf, #0f
0x0274	ld I, #0478
0x0276	ld vf, [I]
0x0278	se vf, #00
0x027a	jp loc_03f8
0x027c	se ve, #00
0x027e	jp loc_03f8
0x0280	se vd, #00
0x0282	jp loc_03f8
0x0284	se vc, #00
0x0286	jp loc_03f8
0x0288	se vb, #00
0x028a	jp loc_03f8
0x028c	se va, #00
0x028e	jp loc_03f8
0x0290	se v9, #00
0x0292	jp loc_03f8
0x0294	se v8, #00
0x0296	jp loc_03f8
0x0298	se v7, #00
0x029a	jp loc_03f8
0x029c	se v6, #00
0x029e	jp loc_03f8
0x02a0	se v5, #00
0x02a2	jp loc_03f8
0x02a4	se v4, #00
0x02a6	jp loc_03f8
0x02a8	se v3, #00
0x02aa	jp loc_03f8
0x02ac	se v2, #00
0x02ae	jp loc_03f8
0x02b0	se v1, #00
0x02b2	jp loc_03f8
0x02b4	se v0, #00
0x02b6	jp loc_03f8
0x02b8	ld v0, #00
0x02ba	ld f, v0
0x02bc	ld v0, [I]
0x02be	sne v0, #00
0x02c0	jp loc_0402
0x02c2	ld I, #0452
0x02c4	ld ve, #7b
0x02c6	ld b, ve
0x02c8	ld v2, [I]
0x02ca	se v0, #01
0x02cc	jp loc_03c6
0x02ce	se v1, #02
0x02d0	jp loc_03c6
0x02d2	se v2, #03
0x02d4	jp loc_03c6
0x02d6	ld ve, #02
0x02d8	ld vf, #00
0x02da	ld v0, #fe
0x02dc	ld v1, #01
0x02de	add v0, v1
0x02e0	se vf, #00
0x02e2	jp loc_040c
0x02e4	ld ve, #03
0x02e6	se v0, #ff
0x02e8	jp loc_040c
0x02ea	ld ve, #04
0x02ec	add v0, v1
0x02ee	se vf, #01
0x02f0	jp loc_040c
0x02f2	ld ve, #05
0x02f4	se v0, #00
0x02f6	jp loc_040c
0x02f8	ld v0, #01
0x02fa	ld ve, #06
0x02fc	ld vf, #00
0x02fe	sub v0, v1
0x0300	se vf, #01
0x0302	jp loc_040c
0x0304	ld ve, #07
0x0306	se v0, #00
0x0308	jp loc_040c
0x030a	ld ve, #08
0x030c	sub v0, v1
0x030e	se vf, #00
0x0310	jp loc_040c
0x0312	ld ve, #09
0x0314	se v0, #ff
0x0316	jp loc_040c
0x0318	ld v0, #01
0x031a	ld ve, #0a
0x031c	ld vf, #00
0x031e	subn v0, v1
0x0320	se vf, #01
0x0322	jp loc_040c
0x0324	ld ve, #0b
0x0326	se v0, #00
0x0328	jp loc_040c
0x032a	ld ve, #0c
0x032c	ld v0, #01
0x032e	ld v1, #00
0x0330	subn v0, v1
0x0332	se vf, #00
0x0334	jp loc_040c
0x0336	ld ve, #0d
0x0338	se v0, #ff
0x033a	jp loc_040c
0x033c	ld v0, #ff
0x033e	ld ve, #0e
0x0340	ld vf, #00
0x0342	shr v0
0x0344	se vf, #01
0x0346	jp loc_040c
0x0348	ld ve, #0f
0x034a	se v0, #7f
0x034c	jp loc_040c
0x034e	ld v0, #40
0x0350	ld ve, #10
0x0352	shr v0
0x0354	se vf, #00
0x0356	jp loc_040c
0x0358	ld ve, #11
0x035a	se v0, #20
0x035c	jp loc_040c
0x035e	ld ve, #12
0x0360	ld vf, #01
0x0362	shl v0
0x0364	se vf, #00
0x0366	jp loc_040c
0x0368	ld ve, #13
0x036a	se v0, #40
0x036c	jp loc_040c
0x036e	ld v0, #fa
0x0370	ld ve, #14
0x0372	shl v0
0x0374	se vf, #01
0x0376	jp loc_040c
0x0378	ld ve, #15
0x037a	se v0, #f4
0x037c	jp loc_040c
0x037e	ld v1, #7b
0x0380	ld ve, #16
0x0382	xor v0, v1
0x0384	se v0, #8f
0x0386	jp loc_040c
0x0388	ld I, #0488
0x038a	ld v7, [I]
0x038c	save_hp_flags
0x038e	ld I, #0478
0x0390	ld v7, [I]
0x0392	load_hp_flags
0x0394	ld ve, #17
0x0396	se v7, #07
0x0398	jp loc_040c
0x039a	se v6, #06
0x039c	jp loc_040c
0x039e	se v5, #05
0x03a0	jp loc_040c
0x03a2	se v4, #04
0x03a4	jp loc_040c
0x03a6	se v3, #03
0x03a8	jp loc_040c
0x03aa	se v2, #02
0x03ac	jp loc_040c
0x03ae	se v1, #01
0x03b0	jp loc_040c
0x03b2	se v0, #00
0x03b4	jp loc_040c
0x03b6	ld ve, #18
0x03b8	ld I, #0ffe
0x03ba	ld v0, #02
0x03bc	ld vf, #00
0x03be	add I, v0
0x03c0	se vf, #01
0x03c2	jp loc_040c
0x03c4	jp loc_0490
loc_03c6:   ; == START OF CODE BLOCK ==
0x03c6	call loc_0412
0x03c8	add v0, #0a
0x03ca	ld v2, #0b
0x03cc	ld f, v2
0x03ce	drw v0, v1, #5
0x03d0	add v0, #05
0x03d2	ld v2, #0c
0x03d4	ld f, v2
0x03d6	drw v0, v1, #5
0x03d8	add v2, #01
0x03da	ld f, v2
0x03dc	add v0, #05
0x03de	drw v0, v1, #5
0x03e0	jp loc_0450
loc_03e2:   ; == START OF CODE BLOCK ==
0x03e2	call loc_0412
0x03e4	add v0, #0a
0x03e6	ld I, #0464
0x03e8	drw v0, v1, #5
0x03ea	add v0, #06
0x03ec	ld I, #0469
0x03ee	drw v0, v1, #5
0x03f0	add v0, #06
0x03f2	ld I, #0464
0x03f4	drw v0, v1, #5
0x03f6	jp loc_0450
loc_03f8:   ; == START OF CODE BLOCK ==
0x03f8	call loc_0412
0x03fa	add v0, #0a
0x03fc	ld I, #045a
0x03fe	drw v0, v1, #5
0x0400	db #14	;GRAPHIC =    # #  
0x0401	db #50	;GRAPHIC =  # #    	ASCII(P)
loc_0402:   ; == START OF CODE BLOCK ==
0x0402	call loc_0412
0x0404	add v0, #0a
0x0406	ld I, #0455
0x0408	drw v0, v1, #5
0x040a	jp loc_0450
loc_040c:   ; == START OF CODE BLOCK ==
0x040c	call loc_0412
0x040e	call loc_0432
0x0410	jp loc_0450
loc_0412:   ; == START OF CODE BLOCK ==
0x0412	db #60	;GRAPHIC =  ##     	ASCII(`)
0x0413	db #00	;GRAPHIC =         
0x0414	db #61	;GRAPHIC =  ##    #	ASCII(a)
0x0415	db #00	;GRAPHIC =         
0x0416	db #a4	;GRAPHIC = # #  #  
0x0417	db #5f	;GRAPHIC =  # #####	ASCII(_)
0x0418	db #d0	;GRAPHIC = ## #    
0x0419	db #15	;GRAPHIC =    # # #
0x041a	db #70	;GRAPHIC =  ###    	ASCII(p)
0x041b	db #05	;GRAPHIC =      # #
0x041c	db #a4	;GRAPHIC = # #  #  
0x041d	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x041e	db #d0	;GRAPHIC = ## #    
0x041f	db #15	;GRAPHIC =    # # #
0x0420	db #70	;GRAPHIC =  ###    	ASCII(p)
0x0421	db #06	;GRAPHIC =      ## 
0x0422	db #d0	;GRAPHIC = ## #    
0x0423	db #15	;GRAPHIC =    # # #
0x0424	db #a4	;GRAPHIC = # #  #  
0x0425	db #5a	;GRAPHIC =  # ## # 	ASCII(Z)
0x0426	db #70	;GRAPHIC =  ###    	ASCII(p)
0x0427	db #06	;GRAPHIC =      ## 
0x0428	db #d0	;GRAPHIC = ## #    
0x0429	db #15	;GRAPHIC =    # # #
0x042a	db #a4	;GRAPHIC = # #  #  
0x042b	db #6e	;GRAPHIC =  ## ### 	ASCII(n)
0x042c	db #70	;GRAPHIC =  ###    	ASCII(p)
0x042d	db #05	;GRAPHIC =      # #
0x042e	db #d0	;GRAPHIC = ## #    
0x042f	db #15	;GRAPHIC =    # # #
0x0430	db #00	;GRAPHIC =         
0x0431	db #ee	;GRAPHIC = ### ### 
loc_0432:   ; == START OF CODE BLOCK ==
0x0432	db #84	;GRAPHIC = #    #  
0x0433	db #00	;GRAPHIC =         
0x0434	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0435	db #0a	;GRAPHIC =     # # 
0x0436	db #85	;GRAPHIC = #    # #
0x0437	db #10	;GRAPHIC =    #    
0x0438	db #a4	;GRAPHIC = # #  #  
0x0439	db #52	;GRAPHIC =  # #  # 	ASCII(R)
0x043a	db #fe	;GRAPHIC = ####### 
0x043b	db #33	;GRAPHIC =   ##  ##	ASCII(3)
0x043c	db #f2	;GRAPHIC = ####  # 
0x043d	db #65	;GRAPHIC =  ##  # #	ASCII(e)
0x043e	db #f0	;GRAPHIC = ####    
0x043f	db #29	;GRAPHIC =   # #  #	ASCII())
0x0440	db #d4	;GRAPHIC = ## # #  
0x0441	db #55	;GRAPHIC =  # # # #	ASCII(U)
0x0442	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0443	db #06	;GRAPHIC =      ## 
0x0444	db #f1	;GRAPHIC = ####   #
0x0445	db #29	;GRAPHIC =   # #  #	ASCII())
0x0446	db #d4	;GRAPHIC = ## # #  
0x0447	db #55	;GRAPHIC =  # # # #	ASCII(U)
0x0448	db #74	;GRAPHIC =  ### #  	ASCII(t)
0x0449	db #06	;GRAPHIC =      ## 
0x044a	db #f2	;GRAPHIC = ####  # 
0x044b	db #29	;GRAPHIC =   # #  #	ASCII())
0x044c	db #d4	;GRAPHIC = ## # #  
0x044d	db #55	;GRAPHIC =  # # # #	ASCII(U)
0x044e	db #00	;GRAPHIC =         
0x044f	db #ee	;GRAPHIC = ### ### 
loc_0450:   ; == START OF CODE BLOCK ==
0x0450	jp loc_0450
0x0452	db #00	;GRAPHIC =         
0x0453	db #00	;GRAPHIC =         
0x0454	db #00	;GRAPHIC =         
0x0455	db #10	;GRAPHIC =    #    
0x0456	db #30	;GRAPHIC =   ##    	ASCII(0)
0x0457	db #10	;GRAPHIC =    #    
0x0458	db #10	;GRAPHIC =    #    
0x0459	db #10	;GRAPHIC =    #    
0x045a	db #f0	;GRAPHIC = ####    
0x045b	db #90	;GRAPHIC = #  #    
0x045c	db #90	;GRAPHIC = #  #    
0x045d	db #90	;GRAPHIC = #  #    
0x045e	db #f0	;GRAPHIC = ####    
0x045f	db #f0	;GRAPHIC = ####    
0x0460	db #80	;GRAPHIC = #       
0x0461	db #f0	;GRAPHIC = ####    
0x0462	db #80	;GRAPHIC = #       
0x0463	db #f0	;GRAPHIC = ####    
0x0464	db #f8	;GRAPHIC = #####   
0x0465	db #20	;GRAPHIC =   #     
0x0466	db #20	;GRAPHIC =   #     
0x0467	db #20	;GRAPHIC =   #     
0x0468	db #f8	;GRAPHIC = #####   
0x0469	db #88	;GRAPHIC = #   #   
0x046a	db #c8	;GRAPHIC = ##  #   
0x046b	db #a8	;GRAPHIC = # # #   
0x046c	db #98	;GRAPHIC = #  ##   
0x046d	db #88	;GRAPHIC = #   #   
0x046e	db #e0	;GRAPHIC = ###     
0x046f	db #90	;GRAPHIC = #  #    
0x0470	db #e0	;GRAPHIC = ###     
0x0471	db #90	;GRAPHIC = #  #    
0x0472	db #88	;GRAPHIC = #   #   
0x0473	db #90	;GRAPHIC = #  #    
0x0474	db #a0	;GRAPHIC = # #     
0x0475	db #c0	;GRAPHIC = ##      
0x0476	db #a0	;GRAPHIC = # #     
0x0477	db #90	;GRAPHIC = #  #    
0x0478	db #00	;GRAPHIC =         
0x0479	db #00	;GRAPHIC =         
0x047a	db #00	;GRAPHIC =         
0x047b	db #00	;GRAPHIC =         
0x047c	db #00	;GRAPHIC =         
0x047d	db #00	;GRAPHIC =         
0x047e	db #00	;GRAPHIC =         
0x047f	db #00	;GRAPHIC =         
0x0480	db #00	;GRAPHIC =         
0x0481	db #00	;GRAPHIC =         
0x0482	db #00	;GRAPHIC =         
0x0483	db #00	;GRAPHIC =         
0x0484	db #00	;GRAPHIC =         
0x0485	db #00	;GRAPHIC =         
0x0486	db #00	;GRAPHIC =         
0x0487	db #00	;GRAPHIC =         
0x0488	db #00	;GRAPHIC =         
0x0489	db #01	;GRAPHIC =        #
0x048a	db #02	;GRAPHIC =       # 
0x048b	db #03	;GRAPHIC =       ##
0x048c	db #04	;GRAPHIC =      #  
0x048d	db #05	;GRAPHIC =      # #
0x048e	db #06	;GRAPHIC =      ## 
0x048f	db #07	;GRAPHIC =      ###
loc_0490:   ; == START OF CODE BLOCK ==
0x0490	db #60	;GRAPHIC =  ##     	ASCII(`)
0x0491	db #00	;GRAPHIC =         
0x0492	db #61	;GRAPHIC =  ##    #	ASCII(a)
0x0493	db #00	;GRAPHIC =         
0x0494	db #f0	;GRAPHIC = ####    
0x0495	db #29	;GRAPHIC =   # #  #	ASCII())
0x0496	db #d0	;GRAPHIC = ## #    
0x0497	db #15	;GRAPHIC =    # # #
0x0498	db #70	;GRAPHIC =  ###    	ASCII(p)
0x0499	db #05	;GRAPHIC =      # #
0x049a	db #a4	;GRAPHIC = # #  #  
0x049b	db #73	;GRAPHIC =  ###  ##	ASCII(s)
0x049c	db #d0	;GRAPHIC = ## #    
0x049d	db #15	;GRAPHIC =    # # #
0x049e	db #14	;GRAPHIC =    # #  
0x049f	db #50	;GRAPHIC =  # #    	ASCII(P)
