JP lbl-219	;
#4d		;01001101
#49		;01001001
#53		;01010011
#53		;01010011
#49		;01001001
#4c		;01001100
#45		;01000101
#20		;00100000
#62		;01100010
#79		;01111001
#20		;00100000
#44		;01000100
#61		;01100001
#76		;01110110
#69		;01101001
#64		;01100100
#20		;00100000
#57		;01010111
#49		;01001001
#4e		;01001110
#54		;01010100
#45		;01000101
#52		;01010010
lbl-219:
LD Vc, #0c;
LD V0, #00;
LD V1, #00;
LD V5, #08;
LD V6, #0a;
LD V7, #00;
LD Ve, #01;
LD I, lbl-2ad;
lbl-229:
DRW V0, V1, #4;
ADD V0, #08;
SE V0, #40;
JP lbl-229;
LD V0, #00;
LD V1, #1c;
LD I, lbl-2b0;
DRW V0, V1, #4;
lbl-239:
LD I, lbl-2b0;
DRW V0, V1, #4;
SE Ve, #01;
JP lbl-249;
ADD V0, #04;
SNE V0, #38;
LD Ve, #00;
JP lbl-24f;
lbl-249:
ADD V0, #fc;
SNE V0, #00;
LD Ve, #01;
lbl-24f:
DRW V0, V1, #4;
LD DT, Vc;
lbl-253:
LD Vb, DT;
SE Vb, #00;
JP lbl-253;
LD V2, #08;
SKP V2;
JP lbl-295;
SE Vc, #00;
ADD Vc, #fe;
LD V3, #1b;
LD V2, V0;
LD I, lbl-2b0;
DRW V2, V3, #1;
LD V4, #00;
lbl-26d:
DRW V2, V3, #1;
ADD V3, #ff;
DRW V2, V3, #1;
SE Vf, #00;
LD V4, #01;
SE V3, #03;
JP lbl-26d;
DRW V2, V3, #1;
SE V4, #01;
JP lbl-291;
ADD V7, #05;
ADD V5, #ff;
LD V2, V0;
LD V3, #00;
LD I, lbl-2ad;
DRW V2, V3, #4;
SNE V5, #00;
JP lbl-297;
lbl-291:
ADD V6, #ff;
SE V6, #00;
lbl-295:
JP lbl-239;
lbl-297:
LD I, #2b4;
LD B, V7;
LD V2, [I];
LD V3, #1b;
LD V4, #0d;
LD F, V1;
DRW V3, V4, #5;
ADD V3, #05;
LD F, V2;
DRW V3, V4, #5;
lbl-2ab:
JP lbl-2ab;
lbl-2ad:
#10		;00010000
#38		;00111000
#38		;00111000
lbl-2b0:
#10		;00010000
#38		;00111000
#7c		;01111100
#fe		;11111110
