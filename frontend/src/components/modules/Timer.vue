<template>
  <span>
    {{ secondsToHhmmss(timer) }}
  </span>
</template>

<script setup lang="ts">
import { secondsToHhmmss } from "@/utils/date-utils";
import { ref } from "vue";

const timer = ref(0);
const timerId = ref(0);

const start = () => {
  timerId.value = setInterval(() => {
    timer.value++;
  }, 1000);
};

const stop = () => {
  clearInterval(timerId.value);
};

const reset = () => {
  timer.value = 0;
};

defineExpose<{ start: () => void; stop: () => void; reset: () => void }>({
  start,
  stop,
  reset,
});
</script>
