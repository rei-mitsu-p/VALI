<template>
  <RightMenu>
    <span>{{ BOMB_SYMBOL }}: {{ bombCount - flagCount }}</span>
    <Timer ref="timer" />
    <BaseButton
      v-for="(_, level) in LEVEL_SETTINGS"
      :key="level"
      @clicked="selectLevel(level)"
      :isSelected="selectedLevel == level"
      >{{ level }}</BaseButton
    >
  </RightMenu>
  <div class="wrapper">
    <div
      class="grid-container"
      :style="{ '--grid-size': gridSize, '--grid-font-size': fontSize }"
    >
      <MCell
        v-for="(cell, index) in map.flat()"
        :key="index"
        :cell="cell"
        :isFailed="isFailed"
        :bombSymbol="BOMB_SYMBOL"
        @clicked="open(cell)"
        @rightClicked="toggleFlag(cell)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import BaseButton from "@/components/elements/BaseButton.vue";
import MCell from "@/components/elements/minesweeper/MCell.vue";
import RightMenu from "@/components/layouts/RightMenu.vue";
import Timer from "@/components/modules/Timer.vue";
import { Cell } from "@/types/minesweeper/cell";
import { onMounted, ref } from "vue";

const LEVEL_SETTINGS = {
  Easy: { gridSize: 10, bombCount: 10, fontSize: "30px" },
  Normal: { gridSize: 20, bombCount: 80, fontSize: "20px" },
  Hard: { gridSize: 30, bombCount: 225, fontSize: "13px" },
} as const;

const BOMB_SYMBOL = "💣";
const FLAG_SYMBOL = "🚩";

const selectedLevel = ref<keyof typeof LEVEL_SETTINGS>("Easy");
const bombCount = ref(LEVEL_SETTINGS[selectedLevel.value].bombCount);
const gridSize = ref(LEVEL_SETTINGS[selectedLevel.value].gridSize);
const fontSize = ref(LEVEL_SETTINGS[selectedLevel.value].fontSize);

const isStarted = ref(false);
const isFailed = ref(false);
const isSuccess = ref(false);

const map = ref<Cell[][]>([]);

const openedCount = ref(0);
const flagCount = ref(0);

const timer = ref(Timer);

const init = () => {
  timer.value?.stop();
  timer.value?.reset();
  map.value = Array.from({ length: gridSize.value }, (_, y) =>
    Array.from({ length: gridSize.value }, (_, x) => new Cell(x, y))
  );

  placeBombs(map.value.flat());

  openedCount.value = 0;
  flagCount.value = 0;
  isSuccess.value = false;
  isStarted.value = false;
  isFailed.value = false;
};

onMounted(init);

const placeBombs = (cells: Cell[]) => {
  for (let i = 0; i < bombCount.value; i++) {
    const index = Math.floor(Math.random() * cells.length);
    cells[index].hasBomb = true;
    cells.splice(index, 1);
  }
};

const selectLevel = (level: keyof typeof LEVEL_SETTINGS) => {
  selectedLevel.value = level;
  gridSize.value = LEVEL_SETTINGS[level].gridSize;
  bombCount.value = LEVEL_SETTINGS[level].bombCount;
  fontSize.value = LEVEL_SETTINGS[level].fontSize;
  init();
};

const getAdjacentCells = (cell: Cell): Cell[] => {
  const adjacentCells: Cell[] = [];
  for (let dy = -1; dy <= 1; dy++) {
    for (let dx = -1; dx <= 1; dx++) {
      if (dx !== 0 || dy !== 0) {
        const x = cell.x + dx;
        const y = cell.y + dy;
        if (map.value[y]?.[x]) {
          adjacentCells.push(map.value[y][x]);
        }
      }
    }
  }
  return adjacentCells;
};

const open = (cell: Cell) => {
  if (
    cell.isOpened ||
    cell.contents === FLAG_SYMBOL ||
    isFailed.value ||
    isSuccess.value
  ) {
    return;
  }

  if (cell.hasBomb) {
    if (!isStarted.value) {
      retry(cell.x, cell.y);
      return;
    }
    fail();
    return;
  }

  const adjacentCells = getAdjacentCells(cell);
  const adjacentBombCount = adjacentCells.filter((cell) => cell.hasBomb).length;

  if (!isStarted.value) {
    if (adjacentBombCount !== 0) {
      retry(cell.x, cell.y);
      return;
    }
    isStarted.value = true;
    timer.value?.start();
  }

  cell.isOpened = true;
  openedCount.value++;

  if (adjacentBombCount === 0) {
    adjacentCells.forEach((cell) => {
      if (!cell.isOpened) {
        open(cell);
      }
    });
  } else {
    cell.contents = adjacentBombCount.toString();
  }

  if (gridSize.value ** 2 === openedCount.value + bombCount.value) {
    success();
  }
};

const retry = (x: number, y: number) => {
  init();
  open(map.value[y][x]);
};

const toggleFlag = (cell: Cell) => {
  if (cell.isOpened || isFailed.value) {
    return;
  }

  if (cell.contents == FLAG_SYMBOL) {
    cell.contents = "";
    flagCount.value--;
  } else {
    cell.contents = FLAG_SYMBOL;
    flagCount.value++;
  }
};

const fail = () => {
  isFailed.value = true;
  timer.value?.stop();
};

const success = () => {
  isSuccess.value = true;
  timer.value?.stop();
};
</script>

<style scoped>
.wrapper {
  width: 600px;
  height: 600px;
  margin: 5px auto;
  box-shadow: 0 0px 0px 2px lightgray;
}

.grid-container {
  display: grid;
  width: 100%;
  height: 100%;
  grid-template-columns: repeat(var(--grid-size), 1fr);
  grid-template-rows: repeat(var(--grid-size), 1fr);
  font-size: var(--grid-font-size);
}
</style>
