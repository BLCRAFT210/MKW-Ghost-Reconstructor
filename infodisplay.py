#To be used in Felk's Dolphin scripting branch.
#The two questionable params are likely not of utility for our purposes.

from dolphin import gui, event, memory, controller

white = 0xffffffff
black = 0xff000000

def pointer_chase(address, *chase_offsets):
        val = memory.read_u32(address)
        for offset in chase_offsets[:-1]:
            val = memory.read_u32(val + offset)
        return val+chase_offsets[-1]

while True:
    await event.frameadvance()
    currentInputs = controller.get_gc_buttons(0)
    gui.draw_rect_filled((8, 10), (180, 155), black)

    x_input = memory.read_u8(pointer_chase(0x809BD730, 0xC, 0x0, 0x48, 0x38))
    gui.draw_text((10, 10), white, f'X Input: {x_input}')

    y_input = memory.read_u8(pointer_chase(0x809BD730, 0xC, 0x0, 0x48, 0x39))
    gui.draw_text((10, 20), white, f'Y Input: {y_input}')

    if currentInputs['A']:
        gui.draw_text((10, 30), white, 'A')

    if currentInputs['B']:
        gui.draw_text((10, 40), white, 'B')

    if currentInputs['L']:
        gui.draw_text((10, 50), white, 'Shroom')
    
    dpad = []
    if currentInputs['Left']:
        dpad.append('Left')
    if currentInputs['Right']:
        dpad.append('Right')
    if currentInputs['Down']:
        dpad.append('Down')
    if currentInputs['Up']:
        dpad.append('Up')

    gui.draw_text((10, 60), white, ', '.join(dpad))

    questionableparam1 = memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x10, 0x2B6))
    questionableparam2 = memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x10, 0x2A8))
    gui.draw_text((10, 80), white, f'QP 2: {questionableparam2}')
    gui.draw_text((10, 70), white, f'QP 1: {questionableparam1}')

    trickable = bool(memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x1C, 0x8)) & 0x40000000)
    gui.draw_text((10, 90), white, f'Trickable: {trickable}')

    drifting = bool(memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x1C, 0x4)) & 0x8)
    gui.draw_text((10, 100), white, f'Drifting: {drifting}')

    grounded = bool(memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x1C, 0x4)) & 0x40000)
    gui.draw_text((10, 110), white, f'Grounded: {grounded}')

    inwheelie = bool(memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x1C, 0x4)) & 0x20000000)
    gui.draw_text((10, 120), white, f'In Wheelie: {inwheelie}')

    trickabletimer = memory.read_u16(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x1C, 0xA6))
    gui.draw_text((10, 130), white, f'Trickable timer: {trickabletimer}')

    speed = memory.read_f32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x10, 0x20))
    gui.draw_text((10, 140), white, f'Speed: {speed}')