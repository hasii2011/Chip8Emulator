LD I, lbl-2b4;
CALL lbl-3e6;
CALL lbl-2b6;
lbl-206:
ADD V0, #01;
DRW V0, V1, #1;
SE V0, #25;
JP lbl-206;
lbl-20e:
ADD V1, #ff;
DRW V0, V1, #1;
LD V0, #1a;
DRW V0, V1, #1;
LD V0, #25;
SE V1, #00;
JP lbl-20e;
lbl-21c:
RND V4, #70;
SNE V4, #70;
JP lbl-21c;
RND V3, #03;
LD V0, #1e;
LD V1, #03;
CALL lbl-25c;
lbl-22a:
LD DT, V5;
DRW V0, V1, #4;
SE Vf, #01;
JP lbl-23c;
DRW V0, V1, #4;
ADD V1, #ff;
DRW V0, V1, #4;
CALL lbl-340;
JP lbl-21c;
lbl-23c:
SKNP V7	;
CALL lbl-272;
SKNP V8	;
CALL lbl-284;
SKNP V9	;
CALL lbl-296;
SKP V2	;
JP lbl-250;
LD V6, #00;
LD DT, V6;
lbl-250:
LD V6, DT;
SE V6, #00;
JP lbl-23c;
DRW V0, V1, #4;
ADD V1, #01;
JP lbl-22a;
lbl-25c:
LD I, lbl-2c4;
ADD I, V4;
LD V6, #00;
SNE V3, #01;
LD V6, #04;
SNE V3, #02;
LD V6, #08;
SNE V3, #03;
LD V6, #0c;
ADD I, V6;
RET	;
lbl-272:
DRW V0, V1, #4;
ADD V0, #ff;
CALL lbl-334;
SE Vf, #01;
RET	;
DRW V0, V1, #4;
ADD V0, #01;
CALL lbl-334;
RET	;
lbl-284:
DRW V0, V1, #4;
ADD V0, #01;
CALL lbl-334;
SE Vf, #01;
RET	;
DRW V0, V1, #4;
ADD V0, #ff;
CALL lbl-334;
RET	;
lbl-296:
DRW V0, V1, #4;
ADD V3, #01;
SNE V3, #04;
LD V3, #00;
CALL lbl-25c;
CALL lbl-334;
SE Vf, #01;
RET	;
DRW V0, V1, #4;
ADD V3, #ff;
SNE V3, #ff;
LD V3, #03;
CALL lbl-25c;
CALL lbl-334;
RET	;
lbl-2b4:
#80	;10000000
#00	;00000000
lbl-2b6:
LD V7, #05;
LD V8, #06;
LD V9, #04;
LD V1, #1f;
LD V5, #10;
LD V2, #07;
RET	;
lbl-2c4:
#40        ;01000000
#e0        ;11100000
#00        ;00000000
#00        ;00000000
#40        ;01000000
#c0        ;11000000
#40        ;01000000
#00        ;00000000
#00        ;00000000
#e0        ;11100000
#40        ;01000000
#00        ;00000000
#40        ;01000000
#60        ;01100000
#40        ;01000000
#00        ;00000000
#40        ;01000000
#40        ;01000000
#60        ;01100000
#00        ;00000000
#20        ;00100000
#e0        ;11100000
#00        ;00000000
#00        ;00000000
#c0        ;11000000
#40        ;01000000
#40        ;01000000
#00        ;00000000
#00        ;00000000
#e0        ;11100000
#80        ;10000000
#00        ;00000000
#40        ;01000000
#40        ;01000000
#c0        ;11000000
#00        ;00000000
#00        ;00000000
#e0        ;11100000
#20        ;00100000
#00        ;00000000
#60        ;01100000
#40        ;01000000
#40        ;01000000
#00        ;00000000
#80        ;10000000
#e0        ;11100000
#00        ;00000000
#00        ;00000000
#40        ;01000000
#c0        ;11000000
#80        ;10000000
#00        ;00000000
#c0        ;11000000
#60        ;01100000
#00        ;00000000
#00        ;00000000
#40        ;01000000
#c0        ;11000000
#80        ;10000000
#00        ;00000000
#c0        ;11000000
#60        ;01100000
#00        ;00000000
#00        ;00000000
#80        ;10000000
#c0        ;11000000
#40        ;01000000
#00        ;00000000
#00        ;00000000
#60        ;01100000
#c0        ;11000000
#00        ;00000000
#80        ;10000000
#c0        ;11000000
#40        ;01000000
#00        ;00000000
#00        ;00000000
#60        ;01100000
#c0        ;11000000
#00        ;00000000
#c0        ;11000000
#c0        ;11000000
#00        ;00000000
#00        ;00000000
#c0        ;11000000
#c0        ;11000000
#00        ;00000000
#00        ;00000000
#c0        ;11000000
#c0        ;11000000
#00        ;00000000
#00        ;00000000
#c0        ;11000000
#c0        ;11000000
#00        ;00000000
#00        ;00000000
#40        ;01000000
#40        ;01000000
#40        ;01000000
#40        ;01000000
#00        ;00000000
#f0        ;11110000
#00        ;00000000
#00        ;00000000
#40        ;01000000
#40        ;01000000
#40        ;01000000
#40        ;01000000
#00        ;00000000
#f0        ;11110000
#00        ;00000000
#00        ;00000000
lbl-334:
DRW V0, V1, #4;
LD V6, #35;
lbl-338:
ADD V6, #ff;
SE V6, #00;
JP lbl-338;
RET	;
lbl-340:
LD I, lbl-2b4;
LD Vc, V1;
SE Vc, #1e;
ADD Vc, #01;
SE Vc, #1e;
ADD Vc, #01;
SE Vc, #1e;
ADD Vc, #01;
lbl-350:
CALL lbl-35e;
SNE Vb, #0a;
CALL lbl-372;
SNE V1, Vc;
RET	;
ADD V1, #01;
JP lbl-350;
lbl-35e:
LD V0, #1b;
LD Vb, #00;
lbl-362:
DRW V0, V1, #1;
SE Vf, #00;
ADD Vb, #01;
DRW V0, V1, #1;
ADD V0, #01;
SE V0, #25;
JP lbl-362;
RET	;
lbl-372:
LD V0, #1b;
lbl-374:
DRW V0, V1, #1;
ADD V0, #01;
SE V0, #25;
JP lbl-374;
LD Ve, V1;
LD Vd, Ve;
ADD Ve, #ff;
lbl-382:
LD V0, #1b;
LD Vb, #00;
lbl-386:
DRW V0, Ve, #1;
SE Vf, #00;
JP lbl-390;
DRW V0, Ve, #1;
JP lbl-394;
lbl-390:
DRW V0, Vd, #1;
ADD Vb, #01;
lbl-394:
ADD V0, #01;
SE V0, #25;
JP lbl-386;
SNE Vb, #00;
JP lbl-3a6;
ADD Vd, #ff;
ADD Ve, #ff;
SE Vd, #01;
JP lbl-382;
lbl-3a6:
CALL lbl-3c0;
SE Vf, #01;
CALL lbl-3c0;
ADD Va, #01;
CALL lbl-3c0;
LD V0, Va;
LD Vd, #07;
AND V0, Vd;
SNE V0, #04;
ADD V5, #fe;
SNE V5, #02;
LD V5, #04;
RET	;
lbl-3c0:
LD I, #700;
LD [I], V2;
LD I, #804;
LD B, Va;
LD V2, [I];
LD F, V0;
LD Vd, #32;
LD Ve, #00;
DRW Vd, Ve, #5;
ADD Vd, #05;
LD F, V1;
DRW Vd, Ve, #5;
ADD Vd, #05;
LD F, V2;
DRW Vd, Ve, #5;
LD I, #700;
LD V2, [I];
LD I, lbl-2b4;
RET;
lbl-3e6:
LD Va, #00;
LD V0, #19;
RET;
#37;00110111
#23;00100011
