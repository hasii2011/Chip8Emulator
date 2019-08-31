
from enum import Enum


class Chip8Mnemonics(Enum):

    SYS = 0x0000    # 0nnn; Jump to a machine code routine at nnn; ignored by modern interpreters
    RTS = 0x00EE    # 00EE; Return from a subroutine; Set PC to the address at top of the stack, then subtracts 1 from the stack pointer.

    CLS = 0x00E0    # Clear the display

    JUMP   = 0x1000   # 1nnn;     Jump to location nnn
    CALL   = 0x2000   # 2nnn;     Call subroutine at location nnn
    SEL    = 0x3000   # 3xkk; SEL Vx, kk;     Skip next instruction if Vx = kk    Skip based on literal
    SNEL   = 0x4000   # 4xkk; SNEL Vx, kk;    Skip next instruction if Vx != kk   Skip based on literal
    SER    = 0x5000   # 5xy0; SER Vx, Vy;     Skip next instruction if Vx = Vy    Skip based on register compares
    LDL    = 0x6000   # 6xkk; LDL Vx, kk;     Set Vx = kk                         Load literal
    ADD    = 0x7000   # 7xkk; ADD Vx, kk;     Adds the value kk to the value of register Vx, then stores the result in Vx
    MOV    = 0x8000   # 8xy0; MOV Vx, Vy;     Set Vx = Vy.
    OR     = 0x8001   # 8xy1; OR Vx, Vy;      Set Vx = Vx OR Vy
    AND    = 0x8002   # 8xy2; AND Vx, Vy;     Set Vx = Vx AND Vy
    XOR    = 0x8003   # 8xy3; XOR Vx, Vy;     Set Vx = Vx XOR Vy
    ADDR   = 0x8004   # 8xy4; ADD Vx, Vy;     Set Vx = Vx + Vy        VF is set to 1 when there's a carry, and to 0 when there isn't
    SUB    = 0x8005   # 8xy5; SUB Vx, Vy;     Set Vx = Vx - Vy        VF is set to 0 when there's a borrow, and 1 when there isn't
    SHR    = 0x8006   # 8xy6; SHR Vx, Vy;     Set Vx = Vx SHR 1       Store least significant bit of VX in VF; shifts VX to the right by 1
    SUBN   = 0x8007   # 8xy7; SUBN Vx, Vy;    Set Vx = Vy - Vx        VF is set to 0 when there's a borrow, and 1 when there isn't
    SHL    = 0x800E   # 8xyE; SHL Vx, Vy;     Set Vx = Vx SHL 1       Stores most significant bit of VX in VF; shifts VX to the left by 1
    SNER   = 0x9000   # 9xy0; SNER Vx, Vy;    Skip next instruction if Vx != Vy
    LDI    = 0xA000   # Annn; LDI I, addr;    Set I = nnn; The value of register I is set to nnn
    JPV    = 0xB000   # Bnnn; JUMP V0, addr;        Jump to location nnn + V0       The program counter is set to nnn plus the value of V0
    RNDMSK = 0xC000   # Cxkk; RNDMSK Vx, byte;      Set Vx = random byte AND kk     interpreter generates a random number from 0 to 255
    DRAW   = 0xD000   # Dxyn; DRAW Vx, Vy, nibble;  Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision
    SKP    = 0xE09E   # Ex9E; SKP Vx;             Skip next instruction if key with the value of Vx is pressed
    SKNP   = 0xE0A1   # ExA1; SKNP Vx;            Skip next instruction if key with the value of Vx is not pressed
    LDDT   = 0xF007   # Fx07; LDT Vx, DT;         Set Vx = delay timer value
    WAITKEY = 0xF00A  # Fx0A; WAITKEY Vx, K;   Wait for a key press, store the value of the key in Vx.
    SDT  = 0xF015   # Fx15; SDT DT, Vx;        Set delay timer = Vx
    SST  = 0xF018   # Fx18; SST ST, Vx;        Set sound timer = Vx
    ADDI = 0xF01E   # Fx1E; ADDI I, Vx;        Set I = I + Vx
    LDIS = 0xF029   # Fx29; LDIS F, Vx;        I equals location of sprite for the character in Vx; chars 0-F represented by a 4x5 font
    MOVBCD  = 0xF033   # Fx33; MOVBCD B, Vx;    Store BCD representation of Vx in memory locations I, I+1, and I+2
    MOVM    = 0xF055   # Fx55; MOVM [I], Vx;    Store registers V0-Vx in memory starting at location I.
    READM   = 0xF065   # Fx65; READM Vx, [I];   Read registers V0 through Vx from memory starting at location I.


