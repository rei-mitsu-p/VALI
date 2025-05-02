<template>
  <div class="wrapper">
    <RightMenu>
      <BaseButton
        v-for="(_, level) in LEVEL_SETTINGS"
        :key="level"
        @clicked="
          selectedLevel = level;
          initialize();
        "
        :isSelected="selectedLevel == level"
        >{{ level }}</BaseButton
      >
    </RightMenu>
    <div class="grid">
      <div v-for="(row, rowIndex) in board" :key="rowIndex" class="row">
        <div
          v-for="(cell, colIndex) in row"
          :key="colIndex"
          class="cell"
          :class="{
            fixed: initial[rowIndex][colIndex] !== null,
            highlight: cell === selectedNumber,
          }"
          @click="inputSelectedNumber(rowIndex, colIndex)"
        >
          {{ cell ?? "" }}
        </div>
      </div>
    </div>
    <div class="number-pad">
      <BaseButton
        v-for="n in 9"
        :key="n"
        :isSelected="selectedNumber === n"
        @clicked="selectedNumber = n"
      >
        {{ n }}
      </BaseButton>
    </div>
    <h1 v-if="isSuccess">Success</h1>
  </div>
</template>

<script lang="ts" setup>
import BaseButton from "@/components/elements/BaseButton.vue";
import RightMenu from "@/components/layouts/RightMenu.vue";
import { onMounted, ref } from "vue";
type Board = (number | null)[][];

const LEVEL_SETTINGS = {
  Easy: { emptyCount: 32 },
  Normal: { emptyCount: 42 },
  Hard: { emptyCount: 52 },
} as const;

const selectedLevel = ref<keyof typeof LEVEL_SETTINGS>("Easy");
const selectedNumber = ref<number>(0);

const board = ref<Board>([]);
const solution = ref<Board>([]);
const initial = ref<Board>([]);

const isSuccess = ref(false);

const initialize = () => {
  const solved = generateSolution();
  solution.value = deepCopy(solved);
  const problem = generateProblem(
    solved,
    LEVEL_SETTINGS[selectedLevel.value].emptyCount
  );
  initial.value = deepCopy(problem);
  board.value = deepCopy(problem);
  selectedNumber.value = 0;
  isSuccess.value = false;
};

onMounted(initialize);

const generateSolution = (): Board => {
  const board = Array.from({ length: 9 }, () => Array(9).fill(null));
  fillBoard(board);
  return board;
};

const fillBoard = (board: Board): boolean => {
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      if (board[row][col] === null) {
        for (const num of shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])) {
          if (isSafe(board, row, col, num)) {
            board[row][col] = num;
            if (fillBoard(board)) {
              return true;
            }
            board[row][col] = null;
          }
        }
        return false;
      }
    }
  }
  return true;
};

const isSafe = (
  board: Board,
  row: number,
  col: number,
  num: number
): boolean => {
  for (let i = 0; i < 9; i++) {
    if (board[row][i] === num || board[i][col] === num) {
      return false;
    }
  }
  const startRow = Math.floor(row / 3) * 3;
  const startCol = Math.floor(col / 3) * 3;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[startRow + i][startCol + j] === num) {
        return false;
      }
    }
  }
  return true;
};

const shuffle = <T,>(array: T[]): T[] => {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
};

const generateProblem = (board: Board, emptyCount: number): Board => {
  const problem = deepCopy(board);
  const positions = shuffle(
    Array.from({ length: 81 }, (_, i) => [Math.floor(i / 9), i % 9])
  );

  let removed = 0;
  for (const [row, col] of positions) {
    const backup = problem[row][col];
    problem[row][col] = null;

    if (hasUniqueSolution(problem)) {
      removed++;
    } else {
      problem[row][col] = backup;
    }

    if (removed >= emptyCount) {
      break;
    }
  }
  return problem;
};

const hasUniqueSolution = (board: Board): boolean => {
  let count = 0;
  const copy = deepCopy(board);

  const solve = (b: Board): boolean => {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (b[row][col] === null) {
          for (let num = 1; num <= 9; num++) {
            if (isSafe(b, row, col, num)) {
              b[row][col] = num;
              if (solve(b)) {
                return true;
              }
              b[row][col] = null;
            }
          }
          return false;
        }
      }
    }
    count++;
    return count > 1;
  };

  solve(copy);
  return count === 1;
};

const deepCopy = (board: Board): Board => {
  return board.map((row) => [...row]);
};

const inputSelectedNumber = (row: number, col: number) => {
  if (
    !selectedNumber.value ||
    initial.value[row][col] !== null ||
    isSuccess.value
  ) {
    return;
  }
  board.value[row][col] =
    board.value[row][col] === selectedNumber.value
      ? null
      : selectedNumber.value;
  checkSuccess();
};

const checkSuccess = () => {
  isSuccess.value = board.value.every((row, r) =>
    row.every((cell, c) => cell === solution.value[r][c])
  );
};
</script>

<style scoped>
.wrapper {
  display: inline-block;
  margin: 10px auto;
}

.grid {
  display: grid;
  grid-template-rows: repeat(9, 40px);
  margin-bottom: 20px;
}
.row {
  display: grid;
  grid-template-columns: repeat(9, 40px);
}
.row:nth-child(3n + 4) {
  border-top: 2px solid black;
}
.cell:nth-child(3n + 4) {
  border-left: 2px solid black;
}
.cell {
  width: 40px;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  border: 1px solid gray;
  cursor: pointer;
  user-select: none;
  box-sizing: border-box;
}
.cell.fixed {
  background-color: lightcyan;
  font-weight: bold;
  cursor: default;
}
.cell.highlight {
  background-color: peachpuff;
}

.number-pad {
  display: flex;
  justify-content: center;
  gap: 5px;
}
.number-pad button {
  width: 35px;
  height: 35px;
}
</style>
