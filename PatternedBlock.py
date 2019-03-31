from mcpi.minecraft import Minecraft
import mcpi.block as Block

mc = Minecraft.create()

def patterned_block(pos, size, pattern, frequency):
    for x in range(1, size):
        for y in range(1, size):
            for z in range(1, size):
                id = pattern[round((x+y+z)/(size/frequency*4)%1*(len(pattern)-1))]
                mc.setBlock(pos.x+x, pos.y+y, pos.z+z, id)

patterned_block(mc.player.getPos(), 20, [Block.SNOW_BLOCK.id, Block.LAPIS_LAZULI_BLOCK.id], 8)
