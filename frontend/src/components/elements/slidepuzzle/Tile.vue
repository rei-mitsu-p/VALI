<template>
  <div
    class="tile"
    :class="{ empty: tile === 0 }"
    :style="getImageSliceStyle(tile)"
    @click="$emit('clicked')"
  ></div>
</template>

<script setup lang="ts">
import okCat from "@/assets/ok-cat.svg";

const props = defineProps<{
  gridSize: number;
  tile: number;
}>();

const getImageSliceStyle = (tile: number): Record<string, string> => {
  if (tile === 0) {
    return {};
  }
  const row = Math.floor((tile - 1) / props.gridSize);
  const col = (tile - 1) % props.gridSize;

  return {
    backgroundImage: `url(${okCat})`,
    backgroundSize: `${props.gridSize * 100}%`,
    backgroundPosition: `${(col / (props.gridSize - 1)) * 100}% ${(row / (props.gridSize - 1)) * 100}%`,
  };
};
</script>

<style scoped>
.tile {
  background-color: whitesmoke;
  width: 100px;
  height: 100px;
  cursor: pointer;
  background-repeat: no-repeat;
}
.tile.empty {
  background-color: lightgray;
  cursor: default;
}
</style>
