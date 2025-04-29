<template>
  <RightMenu>
    <BaseButton
      v-for="(_, level) in LEVEL_SETTINGS"
      :key="level"
      :isSelected="selectedLevel == level"
      @clicked="
        selectedLevel = level;
        gridSize = LEVEL_SETTINGS[level].gridSize;
        initializePuzzle();
      "
      >{{ level }}</BaseButton
    >
  </RightMenu>
  <div class="puzzle-container" :style="{ '--repeat-size': gridSize }">
    <Tile
      v-for="(tile, index) in tiles"
      :key="index"
      :gridSize="gridSize"
      :tile="tile"
      @clicked="moveTile(index)"
    ></Tile>
  </div>
  <h1 v-if="isSuccess">Success</h1>
</template>

<script setup lang="ts">
import BaseButton from "@/components/elements/BaseButton.vue";
import Tile from "@/components/elements/slidepuzzle/Tile.vue";
import RightMenu from "@/components/layouts/RightMenu.vue";
import { computed, onMounted, ref } from "vue";

const LEVEL_SETTINGS = {
  Easy: { gridSize: 3 },
  Normal: { gridSize: 4 },
  Hard: { gridSize: 5 },
} as const;

const selectedLevel = ref<keyof typeof LEVEL_SETTINGS>("Easy");
const gridSize = ref(LEVEL_SETTINGS[selectedLevel.value].gridSize);
const tiles = ref<number[]>([]);

const isSuccess = computed(() => {
  return tiles.value.every(
    (tile, index) => tile === (index + 1) % gridSize.value ** 2
  );
});

onMounted(() => {
  initializePuzzle();
});

const initializePuzzle = () => {
  tiles.value = Array.from(
    { length: gridSize.value ** 2 },
    (_, i) => (i + 1) % gridSize.value ** 2
  );
  shufflePuzzle(tiles.value, 1000);
};

const shufflePuzzle = (tiles: number[], count: number) => {
  let emptyIndex = tiles.indexOf(0);

  for (let i = 0; i < count; i++) {
    const movableIndices = getMovableIndices(emptyIndex);
    const randomIndex =
      movableIndices[Math.floor(Math.random() * movableIndices.length)];
    swapTile(tiles, emptyIndex, randomIndex);
    emptyIndex = randomIndex;
  }
};

const getMovableIndices = (emptyIndex: number): number[] => {
  const row = Math.floor(emptyIndex / gridSize.value);
  const col = emptyIndex % gridSize.value;
  const movableIndices: number[] = [];

  if (row > 0) {
    movableIndices.push(emptyIndex - gridSize.value);
  }
  if (row < gridSize.value - 1) {
    movableIndices.push(emptyIndex + gridSize.value);
  }
  if (col > 0) {
    movableIndices.push(emptyIndex - 1);
  }
  if (col < gridSize.value - 1) {
    movableIndices.push(emptyIndex + 1);
  }
  return movableIndices;
};

const moveTile = (index: number) => {
  if (isSuccess.value) {
    return;
  }
  const emptyIndex = tiles.value.indexOf(0);
  if (getMovableIndices(emptyIndex).includes(index)) {
    swapTile(tiles.value, index, emptyIndex);
  }
};

const swapTile = (tiles: number[], index1: number, index2: number) => {
  [tiles[index1], tiles[index2]] = [tiles[index2], tiles[index1]];
};
</script>

<style scoped>
.puzzle-container {
  display: grid;
  grid-template-columns: repeat(var(--repeat-size), 100px);
  grid-template-rows: repeat(var(--repeat-size), 100px);
  gap: 3px;
  justify-content: center;
  align-items: center;
  margin-top: 5px;
}
</style>
