#basic test for showing x and y input

from dolphin import gui, event, memory, savestate

white = 0xffffffff
black = 0xff000000

def pointer_chase(address, *chase_offsets):
        val = memory.read_u32(address)
        for offset in chase_offsets[:-1]:
            val = memory.read_u32(val + offset)
        return val+chase_offsets[-1]

while True:
    await event.frameadvance()
    gui.draw_rect_filled((8, 10), (120, 40), black)

    x_input = memory.read_u8(pointer_chase(0x809BD730, 0xC, 0x0, 0x48, 0x38))
    gui.draw_text((10, 10), white, f"X Input: {x_input}")

    y_input = memory.read_u8(pointer_chase(0x809BD730, 0xC, 0x0, 0x48, 0x39))
    gui.draw_text((10, 20), white, f"Y Input: {y_input}")