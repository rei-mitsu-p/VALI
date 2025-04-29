<template>
  <span>
    {{ secondsToHHmmss(seconds) }}
  </span>
</template>

<script setup lang="ts">
import { secondsToHHmmss } from "@/utils/date-utils";
import { ref } from "vue";

const seconds = ref(0);
const timerId = ref(0);

const start = () => {
  timerId.value = setInterval(() => {
    seconds.value++;
  }, 1000);
};

const stop = () => {
  clearInterval(timerId.value);
};

const reset = () => {
  seconds.value = 0;
};

defineExpose<{ start: () => void; stop: () => void; reset: () => void }>({
  start,
  stop,
  reset,
});
</script>
