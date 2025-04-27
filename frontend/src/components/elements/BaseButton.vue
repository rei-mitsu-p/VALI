<template>
  <button
    type="button"
    @click="$emit('clicked')"
    :style="style"
    :disabled="disabled"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
defineProps<{ style?: string; disabled?: boolean }>();
</script>

<style scoped>
button {
  background-color: royalblue;
  color: white;
  font-size: 16px;
  padding: 5px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

button:hover {
  background-color: navy;
}

button:focus {
  outline: navy solid 1px;
}
</style>
