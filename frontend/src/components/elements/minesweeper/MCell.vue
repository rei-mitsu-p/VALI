<template>
  <div
    class="mcell"
    :class="{ opened: cell.isOpened }"
    @click="$emit('clicked')"
    @contextmenu.prevent="$emit('rightClicked')"
  >
    {{ isFailed && cell.hasBomb ? bombSymbol : cell.contents }}
  </div>
</template>

<script setup lang="ts">
import { Cell } from "@/types/minesweeper/cell";

defineProps<{
  bombSymbol: string;
  isFailed: boolean;
  cell: Cell;
}>();
</script>

<style scoped>
.mcell {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  box-shadow: 0 0 0 0.1px black;
  user-select: none;
  cursor: pointer;
}
.mcell:not(.opened):hover {
  background-color: whitesmoke;
}
.opened {
  background-color: lightgrey;
  cursor: default;
}
</style>
