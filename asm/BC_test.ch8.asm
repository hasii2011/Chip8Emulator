; Setting used by the chipper assembler
option schip11
option binary
align off

; Recursive Disassembly
End of file
0x0200	cls
0x0202	ld v3, #00
0x0204	ld v4, #01
0x0206	ld v5, #ee
0x0208	se v5, #ee
0x020a	jp loc_0310
0x020c	ld v3, #00
0x020e	ld v4, #02
0x0210	ld v5, #ee
0x0212	ld v6, #ee
0x0214	se v5, v6
0x0216	jp loc_0310
0x0218	ld v3, #00
0x021a	ld v4, #03
0x021c	ld v5, #ee
0x021e	sne v5, #fd
0x0220	jp loc_0310
0x0222	ld v3, #00
0x0224	ld v4, #04
0x0226	ld v5, #ee
0x0228	add v5, #01
0x022a	se v5, #ef
0x022c	jp loc_0310
0x022e	ld v3, #00
0x0230	ld v4, #05
0x0232	ld vf, #01
0x0234	ld v5, #ee
0x0236	ld v6, #ef
0x0238	sub v5, v6
0x023a	se vf, #00
0x023c	jp loc_0310
0x023e	ld v3, #00
0x0240	ld v4, #06
0x0242	ld vf, #00
0x0244	ld v5, #ef
0x0246	ld v6, #ee
0x0248	sub v5, v6
0x024a	se vf, #01
0x024c	jp loc_0310
0x024e	ld vf, #00
0x0250	ld v3, #00
0x0252	ld v4, #07
0x0254	ld v5, #ee
0x0256	ld v6, #ef
0x0258	subn v5, v6
0x025a	se vf, #01
0x025c	jp loc_0310
0x025e	ld v3, #00
0x0260	ld v4, #08
0x0262	ld vf, #01
0x0264	ld v5, #ef
0x0266	ld v6, #ee
0x0268	subn v5, v6
0x026a	se vf, #00
0x026c	jp loc_0310
0x026e	ld v3, #00
0x0270	ld v4, #09
0x0272	ld v5, #f0
0x0274	ld v6, #0f
0x0276	or v5, v6
0x0278	se v5, #ff
0x027a	jp loc_0310
0x027c	ld v3, #01
0x027e	ld v4, #00
0x0280	ld v5, #f0
0x0282	ld v6, #0f
0x0284	and v5, v6
0x0286	se v5, #00
0x0288	jp loc_0310
0x028a	ld v3, #01
0x028c	ld v4, #01
0x028e	ld v5, #f0
0x0290	ld v6, #0f
0x0292	xor v5, v6
0x0294	se v5, #ff
0x0296	jp loc_0310
0x0298	ld vf, #00
0x029a	ld v3, #01
0x029c	ld v4, #02
0x029e	ld v5, #81
0x02a0	shl v5
0x02a2	se vf, #01
0x02a4	jp loc_0310
0x02a6	ld v3, #01
0x02a8	ld v4, #03
0x02aa	ld vf, #01
0x02ac	ld v5, #47
0x02ae	shl v5
0x02b0	se vf, #00
0x02b2	jp loc_0310
0x02b4	ld v3, #01
0x02b6	ld v4, #04
0x02b8	ld vf, #00
0x02ba	ld v5, #01
0x02bc	shr v5
0x02be	se vf, #01
0x02c0	jp loc_0310
0x02c2	ld v3, #01
0x02c4	ld v4, #05
0x02c6	ld vf, #01
0x02c8	ld v5, #02
0x02ca	shr v5
0x02cc	se vf, #00
0x02ce	jp loc_0310
0x02d0	ld v3, #01
0x02d2	ld v4, #06
0x02d4	ld v0, #15
0x02d6	ld v1, #78
0x02d8	ld I, #03d0
0x02da	ld [I], v1
0x02dc	ld v1, [I]
0x02de	se v0, #15
0x02e0	jp loc_0310
0x02e2	se v1, #78
0x02e4	jp loc_0310
0x02e6	ld v3, #01
0x02e8	ld v4, #07
0x02ea	ld v0, #8a
0x02ec	ld I, #03d0
0x02ee	ld b, v0
0x02f0	ld I, #03d0
0x02f2	ld v0, [I]
0x02f4	se v0, #01
0x02f6	jp loc_0310
0x02f8	ld v0, #01
0x02fa	add I, v0
0x02fc	ld v0, [I]
0x02fe	se v0, #03
0x0300	jp loc_0310
0x0302	ld v0, #01
0x0304	add I, v0
0x0306	ld v0, [I]
0x0308	se v0, #08
0x030a	jp loc_0310
0x030c	jp loc_0332
loc_030e:   ; == START OF CODE BLOCK ==
0x030e	jp loc_030e
loc_0310:   ; == START OF CODE BLOCK ==
0x0310	ld I, #032a
0x0312	ld v0, #13
0x0314	ld v1, #09
0x0316	drw v0, v1, #8
0x0318	ld f, v3
0x031a	ld v0, #22
0x031c	ld v1, #0b
0x031e	drw v0, v1, #5
0x0320	ld f, v4
0x0322	ld v0, #28
0x0324	ld v1, #0b
0x0326	drw v0, v1, #5
0x0328	jp loc_030e
0x032a	db #ff	;GRAPHIC = ########
0x032b	db #f0	;GRAPHIC = ####    
0x032c	db #f0	;GRAPHIC = ####    
0x032d	db #ff	;GRAPHIC = ########
0x032e	db #f0	;GRAPHIC = ####    
0x032f	db #f0	;GRAPHIC = ####    
0x0330	db #f0	;GRAPHIC = ####    
0x0331	db #ff	;GRAPHIC = ########
loc_0332:   ; == START OF CODE BLOCK ==
0x0332	ld I, #0358
0x0334	ld v0, #15
0x0336	ld v1, #0b
0x0338	ld v3, #08
loc_033a:   ; == START OF CODE BLOCK ==
0x033a	drw v0, v1, #8
0x033c	add v0, #08
0x033e	add I, v3
0x0340	se v0, #2d
0x0342	jp loc_033a
0x0344	ld I, #0370
0x0346	ld v0, #02
0x0348	ld v1, #18
0x034a	ld v3, #08
loc_034c:   ; == START OF CODE BLOCK ==
0x034c	drw v0, v1, #8
0x034e	add v0, #05
0x0350	add I, v3
0x0352	se v0, #3e
0x0354	jp loc_034c
0x0356	jp loc_030e
0x0358	db #f0	;GRAPHIC = ####    
0x0359	db #88	;GRAPHIC = #   #   
0x035a	db #88	;GRAPHIC = #   #   
0x035b	db #f0	;GRAPHIC = ####    
0x035c	db #88	;GRAPHIC = #   #   
0x035d	db #88	;GRAPHIC = #   #   
0x035e	db #88	;GRAPHIC = #   #   
0x035f	db #f0	;GRAPHIC = ####    
0x0360	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0361	db #84	;GRAPHIC = #    #  
0x0362	db #84	;GRAPHIC = #    #  
0x0363	db #84	;GRAPHIC = #    #  
0x0364	db #84	;GRAPHIC = #    #  
0x0365	db #84	;GRAPHIC = #    #  
0x0366	db #84	;GRAPHIC = #    #  
0x0367	db #78	;GRAPHIC =  ####   	ASCII(x)
0x0368	db #84	;GRAPHIC = #    #  
0x0369	db #c4	;GRAPHIC = ##   #  
0x036a	db #a4	;GRAPHIC = # #  #  
0x036b	db #94	;GRAPHIC = #  # #  
0x036c	db #8c	;GRAPHIC = #   ##  
0x036d	db #84	;GRAPHIC = #    #  
0x036e	db #84	;GRAPHIC = #    #  
0x036f	db #84	;GRAPHIC = #    #  
0x0370	db #c0	;GRAPHIC = ##      
0x0371	db #a0	;GRAPHIC = # #     
0x0372	db #a0	;GRAPHIC = # #     
0x0373	db #c0	;GRAPHIC = ##      
0x0374	db #a0	;GRAPHIC = # #     
0x0375	db #a0	;GRAPHIC = # #     
0x0376	db #c0	;GRAPHIC = ##      
0x0377	db #00	;GRAPHIC =         
0x0378	db #00	;GRAPHIC =         
0x0379	db #00	;GRAPHIC =         
0x037a	db #a0	;GRAPHIC = # #     
0x037b	db #a0	;GRAPHIC = # #     
0x037c	db #e0	;GRAPHIC = ###     
0x037d	db #20	;GRAPHIC =   #     
0x037e	db #20	;GRAPHIC =   #     
0x037f	db #e0	;GRAPHIC = ###     
0x0380	db #00	;GRAPHIC =         
0x0381	db #00	;GRAPHIC =         
0x0382	db #00	;GRAPHIC =         
0x0383	db #00	;GRAPHIC =         
0x0384	db #00	;GRAPHIC =         
0x0385	db #00	;GRAPHIC =         
0x0386	db #00	;GRAPHIC =         
0x0387	db #00	;GRAPHIC =         
0x0388	db #c0	;GRAPHIC = ##      
0x0389	db #a0	;GRAPHIC = # #     
0x038a	db #a0	;GRAPHIC = # #     
0x038b	db #c0	;GRAPHIC = ##      
0x038c	db #a0	;GRAPHIC = # #     
0x038d	db #a0	;GRAPHIC = # #     
0x038e	db #c0	;GRAPHIC = ##      
0x038f	db #00	;GRAPHIC =         
0x0390	db #00	;GRAPHIC =         
0x0391	db #00	;GRAPHIC =         
0x0392	db #60	;GRAPHIC =  ##     	ASCII(`)
0x0393	db #a0	;GRAPHIC = # #     
0x0394	db #c0	;GRAPHIC = ##      
0x0395	db #80	;GRAPHIC = #       
0x0396	db #60	;GRAPHIC =  ##     	ASCII(`)
0x0397	db #00	;GRAPHIC =         
0x0398	db #00	;GRAPHIC =         
0x0399	db #00	;GRAPHIC =         
0x039a	db #60	;GRAPHIC =  ##     	ASCII(`)
0x039b	db #80	;GRAPHIC = #       
0x039c	db #40	;GRAPHIC =  #      	ASCII(@)
0x039d	db #20	;GRAPHIC =   #     
0x039e	db #c0	;GRAPHIC = ##      
0x039f	db #00	;GRAPHIC =         
0x03a0	db #80	;GRAPHIC = #       
0x03a1	db #80	;GRAPHIC = #       
0x03a2	db #c0	;GRAPHIC = ##      
0x03a3	db #80	;GRAPHIC = #       
0x03a4	db #80	;GRAPHIC = #       
0x03a5	db #80	;GRAPHIC = #       
0x03a6	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03a7	db #00	;GRAPHIC =         
0x03a8	db #e0	;GRAPHIC = ###     
0x03a9	db #80	;GRAPHIC = #       
0x03aa	db #80	;GRAPHIC = #       
0x03ab	db #80	;GRAPHIC = #       
0x03ac	db #80	;GRAPHIC = #       
0x03ad	db #80	;GRAPHIC = #       
0x03ae	db #e0	;GRAPHIC = ###     
0x03af	db #00	;GRAPHIC =         
0x03b0	db #00	;GRAPHIC =         
0x03b1	db #00	;GRAPHIC =         
0x03b2	db #40	;GRAPHIC =  #      	ASCII(@)
0x03b3	db #a0	;GRAPHIC = # #     
0x03b4	db #a0	;GRAPHIC = # #     
0x03b5	db #a0	;GRAPHIC = # #     
0x03b6	db #40	;GRAPHIC =  #      	ASCII(@)
0x03b7	db #00	;GRAPHIC =         
0x03b8	db #20	;GRAPHIC =   #     
0x03b9	db #20	;GRAPHIC =   #     
0x03ba	db #20	;GRAPHIC =   #     
0x03bb	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03bc	db #a0	;GRAPHIC = # #     
0x03bd	db #a0	;GRAPHIC = # #     
0x03be	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03bf	db #00	;GRAPHIC =         
0x03c0	db #00	;GRAPHIC =         
0x03c1	db #00	;GRAPHIC =         
0x03c2	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03c3	db #a0	;GRAPHIC = # #     
0x03c4	db #c0	;GRAPHIC = ##      
0x03c5	db #80	;GRAPHIC = #       
0x03c6	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03c7	db #00	;GRAPHIC =         
0x03c8	db #00	;GRAPHIC =         
0x03c9	db #00	;GRAPHIC =         
0x03ca	db #00	;GRAPHIC =         
0x03cb	db #60	;GRAPHIC =  ##     	ASCII(`)
0x03cc	db #40	;GRAPHIC =  #      	ASCII(@)
0x03cd	db #40	;GRAPHIC =  #      	ASCII(@)
0x03ce	db #50	;GRAPHIC =  # #    	ASCII(P)
0x03cf	db #00	;GRAPHIC =         
0x03d0	db #00	;GRAPHIC =         
0x03d1	db #00	;GRAPHIC =         
0x03d2	db #00	;GRAPHIC =         
0x03d3	db #00	;GRAPHIC =         
0x03d4	db #00	;GRAPHIC =         
0x03d5	db #00	;GRAPHIC =         
