<template>
  <button
    type="button"
    @click="$emit('clicked')"
    :style="customStyle"
    :disabled="disabled"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
defineProps<{ customStyle?: string; disabled?: boolean }>();
</script>

<style scoped>
button {
  background-color: royalblue;
  color: white;
  font-size: 16px;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

button:hover {
  background-color: navy;
}

button:focus {
  outline: none;
}
</style>
