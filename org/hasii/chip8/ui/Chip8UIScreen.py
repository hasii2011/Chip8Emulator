
from typing import List

from os import getcwd
from os.path import basename

from pkg_resources import resource_filename

from logging import Logger
from logging import getLogger

from pygame import event as Event
from pygame import Surface
from pygame.font import Font

from albow.References import AttrRef
from albow.References import ItemRef

from albow.themes.Theme import Theme

from albow.core.ui.Widget import Widget
from albow.core.ui.Screen import Screen

from albow.dialog.FileDialogUtilities import request_old_filename

from albow.core.ui.Shell import Shell
from albow.core.ui.AlbowEventLoop import AlbowEventLoop

from albow.menu.Menu import Menu
from albow.menu.MenuBar import MenuBar
from albow.menu.MenuItem import MenuItem

from albow.layout.Column import Column
from albow.layout.Row import Row

from albow.layout.Frame import Frame

from albow.widgets.Label import Label
from albow.widgets.ValueDisplay import ValueDisplay

from org.hasii.chip8.Chip8 import Chip8
from org.hasii.chip8.keyboard.Chip8KeyPadKeys import Chip8KeyPadKeys
from org.hasii.chip8.Chip8RegisterName import Chip8RegisterName
from org.hasii.chip8.Chip8Screen import Chip8Screen
from org.hasii.chip8.ui.Chip8UIStack import Chip8UIStack

from org.hasii.chip8.errors.InvalidIndexRegisterValue import InvalidIndexRegisterValue
from org.hasii.chip8.errors.UnknownInstructionError import UnknownInstructionError
from org.hasii.chip8.errors.UnKnownSpecialRegistersSubOpCode import UnKnownSpecialRegistersSubOpCode
from org.hasii.chip8.ui.Chip8Beep import Chip8Beep


class Chip8UIScreen(Screen):

    FONT_PKG:        str = 'org.hasii.chip8.resources'
    CPU_CYCLE_EVENT: int = AlbowEventLoop.MUSIC_END_EVENT + 1
    SIXTY_HERTZ:     int = 1000 // 60

    fileItems = [

        MenuItem(text="Load", command="processLoad"),
        MenuItem(text="Exit", command="processExit"),
    ]

    helpItems = [
        MenuItem(text="About", command="processAbout"),
        MenuItem(text="Help",  command="processHelp"),
    ]

    fileMenu: Menu = Menu(title="File", items=fileItems)
    helpMenu: Menu = Menu(title="Help", items=helpItems)

    def __init__(self, theShell: Shell, theSurface: Surface):
        """

        Args:
            theShell:  The shell that wraps this screen

            theSurface: The pygame surface to use to drawn on

        Returns:  An instance of itself

        """
        super().__init__(theShell)

        self.surface: Surface = theSurface
        self.logger:  Logger = getLogger(__name__)
        self.chip8:   Chip8 = Chip8()

        fullFileName:       str = self._findFont('MonoFonto.ttf')
        self.internalsFont: Font = Font(fullFileName, 13)

        self.note = Chip8Beep(440)

        self.labelAttrs = {
            'fg_color': Theme.WHITE,
            'bg_color': Theme.LAMAS_MEDIUM_BLUE,
            'font': self.internalsFont,
        }
        self.rowColumnAttrs = {
            'bg_color': Theme.LAMAS_MEDIUM_BLUE,
            'margin': 2,
            'spacing': 3,
        }

        menus = [
            Chip8UIScreen.fileMenu, Chip8UIScreen.helpMenu
        ]

        menuBar = MenuBar(menus=menus, width=self.shell.width)

        framedMenuBar: Frame       = Frame(client=menuBar, width=self.shell.width)
        chip8Screen:   Chip8Screen = Chip8Screen(self.chip8.virtualScreen)
        internalsDisp: Row         = self.makeCpuInternalsDisplay()
        registerDisp:  Row         = self.makeRegisterDisplay()
        stackDisp:     Column      = self.makeStackDisplay()

        registerStackDisp: Row = Row([registerDisp, stackDisp], align='b', **self.rowColumnAttrs)

        contentAttrs = {
            "align": "l",
            'expand': 0,
            'bg_color': Theme.LAMAS_MEDIUM_BLUE,
            'margin': 1,
            'spacing': 2,
        }
        contents = Column([framedMenuBar, chip8Screen, internalsDisp, registerStackDisp], **contentAttrs)

        self.logger.debug(f"Menu bar size: {framedMenuBar.size}, shell width: {self.shell.width}")
        self.add(contents)

    def timer_event(self, theEvent: Event):
        """
        The shell set this up to be called at the CHIP8 60Hz rate;
        So here we will
         * emulate a CPU cycle
         * decrement both the CHIP 8 delay timer and the sound timer

        Args:
            theEvent:

        """
        # clock          = Clock()
        # milliseconds   = clock.tick(1000)         # milliseconds passed since last frame; needs to agree witH Chip8UIShell value
        # self.logger.info(f"milliseconds: {milliseconds}")
        milliseconds: float = theEvent.dict['time']
        seconds:      float = milliseconds/1000
        self.logger.debug(f"seconds: {seconds:5.3f}")
        try:
            if self.chip8.romLoaded is True:
                if self.chip8.isCPUWaitingForKeyPress() is False:
                    self.chip8.emulateSingleCpuCycle()
                self.chip8.decrementDelayTimer()
                self.chip8.decrementSoundTimer()
                if self.chip8.soundTimer == 0:
                    self.note.stop()
        except (UnknownInstructionError, InvalidIndexRegisterValue, UnKnownSpecialRegistersSubOpCode) as e:
            self.logger.error(f"Chip 8 failure: {e}")
            self.logger.error(f"Chip Dump:\n {self.chip8}")
            self.chip8.debugPrintMemory = True
            self.logger.error(f'                        MEMORY DUMP')
            self.logger.error(f'____________________________________________________________________')
            self.chip8._debugPrintMemory(startByteNbr=0, nBytes=len(self.chip8.memory))

            self.shell.quit()

        return True

    def key_down(self, theKeyEvent: Event):
        """
        Seems like part of the Chip 8 emulator has to happen here:
        http://laurencescotford.co.uk/?p=347

        Args:
            theKeyEvent:  The PyGame key event
        """
        pressedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key down: {pressedKey.value:X}")
        if pressedKey != Chip8KeyPadKeys.UNSUPPORTED:
            self.chip8.keypad.keyDown(pressedKey)
            self.logger.debug(f"keypad: {self.chip8.keypad}")
            if self.chip8.keyPressData.waitingForKey is True:
                self.chip8.setKeyPressed(pressedKey)

            self.note.play(-1)

    def key_up(self, theKeyEvent: Event):

        releasedKey: Chip8KeyPadKeys = Chip8KeyPadKeys.toEnum(theKeyEvent.key)
        self.logger.debug(f"key up: {releasedKey.value:X}")
        if releasedKey != Chip8KeyPadKeys.UNSUPPORTED:
            self.chip8.keypad.keyUp(releasedKey)
            self.logger.debug(f"keypad: {self.chip8.keypad}")
            self.note.stop()

    def processLoad_cmd(self):

        cwd: str = getcwd() + '/org/hasii/chip8/roms'
        path = request_old_filename(directory=cwd)
        self.logger.info(f'path: {path}')
        self.chip8.resetCPU()
        fName: str = basename(path)
        self.chip8.loadROM(theFilename=fName)

    def processExit_cmd(self):
        self.logger.info("Executed exit item command")
        self.shell.quit()

    def processAbout_cmd(self):
        self.logger.info("Executed about item command")

    def processHelp_cmd(self):
        self.logger.info("Executed help item command")

    def makeCpuInternalsDisplay(self) -> Row:

        pcRow:        Row = self._makeLabelValueRow(refName='pc',               attrLabel='PC:',          attrFormat='0x%04X', valueWidth=50)
        idxRow:       Row = self._makeLabelValueRow(refName='indexRegister',    attrLabel='Idx:',         attrFormat='0x%04X', valueWidth=42)
        sndTimerRow:  Row = self._makeLabelValueRow(refName='soundTimer',       attrLabel='Sound Timer:', attrFormat='0x%04X', valueWidth=42)
        dlyTimerRow:  Row = self._makeLabelValueRow(refName='delayTimer',       attrLabel='Delay Timer:', attrFormat='0x%04X', valueWidth=42)
        instCountRow: Row = self._makeLabelValueRow(refName='instructionCount', attrLabel='Inst Cnt:',    valueWidth=50)

        retAttrs = {
            'bg_color': Theme.LAMAS_MEDIUM_BLUE,
            'fg_color': Theme.WHITE,
            'spacing': 2,
        }
        retContainer: Row = Row([pcRow, idxRow, sndTimerRow, dlyTimerRow, instCountRow], **retAttrs)

        return retContainer

    def makeRegisterDisplay(self) -> Row:

        leftList:  List[Widget] = []
        rightList: List[Widget] = []
        for regName in Chip8RegisterName:
            itemRef:  ItemRef      = ItemRef(base=self.chip8.registers, index=regName)
            regLabel: Label        = Label(regName.name + ':', **self.labelAttrs)
            regValue: ValueDisplay = ValueDisplay(ref=itemRef, width=42, **self.labelAttrs)
            regValue.format        = '0x%04X'

            pairRow: Row = Row([regLabel, regValue], **self.rowColumnAttrs)
            if regName.value % 2:
                rightList.append(pairRow)
            else:
                leftList.append(pairRow)

        leftColumn:  Column = Column(leftList, **self.rowColumnAttrs)
        rightColumn: Column = Column(rightList, **self.rowColumnAttrs)
        gridAttrs = {
            'bg_color': Theme.LAMAS_MEDIUM_BLUE,
            'margin': 2,
            'border_width': 1
        }
        retGrid: Row = Row([leftColumn, rightColumn], **gridAttrs)
        return retGrid

    def makeStackDisplay(self) -> Column:

        stackLabel: Label   = Label("Stack", **self.labelAttrs)
        stackBox:   Chip8UIStack = Chip8UIStack(theChipStack=self.chip8.stack)

        stackContainer: Column = Column([stackLabel, stackBox], **self.rowColumnAttrs)
        return stackContainer

    def _makeLabelValueRow(self, refName: str, attrLabel: str, attrFormat: str = None, valueWidth: int = 100) -> Row:

        attrRef:   AttrRef      = AttrRef(base=self.chip8, name=refName)
        attrLabel: Label        = Label(attrLabel, **self.labelAttrs)
        attrValue: ValueDisplay = ValueDisplay(ref=attrRef, width=valueWidth, **self.labelAttrs)
        if attrFormat is not None:
            attrValue.format = attrFormat

        retRow: Row = Row([attrLabel, attrValue], **self.rowColumnAttrs)

        return retRow

    def _findFont(self, theFileName: str):

        fileName = resource_filename(Chip8UIScreen.FONT_PKG, theFileName)

        self.logger.debug(f"The full file name: {fileName}")
        return fileName
