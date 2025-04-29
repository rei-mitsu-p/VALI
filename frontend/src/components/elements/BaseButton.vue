<template>
  <button
    type="button"
    @click="$emit('clicked')"
    :style="style"
    :class="{ selected: isSelected }"
    :disabled="disabled"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
defineProps<{ style?: string; isSelected?: boolean; disabled?: boolean }>();
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

button.selected {
  background-color: navy;
}

button:hover {
  background-color: navy;
}

button:focus {
  outline: navy solid 1px;
}
</style>
