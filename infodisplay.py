#To be used in Felk's Dolphin scripting branch.
#Currently, this program just displays inputs.

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
    gui.draw_rect_filled((8, 10), (120, 95), black)

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

    wheelieparam1 = memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x10, 0x2B6))
    wheelieparam2 = memory.read_u32(pointer_chase(0x809C18F8, 0xC, 0x10, 0x0, 0x10, 0x10, 0x2A8))
    gui.draw_text((10, 70), white, f'WP 1: {wheelieparam1}')
    gui.draw_text((10, 80), white, f'WP 2: {wheelieparam2}')