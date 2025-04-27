<template>
  <input
    type="text"
    :value="modelValue"
    :placeholder="placeholder"
    :maxlength="maxlength"
    :disabled="disabled"
    :style="style"
    @input="
      $emit('update:modelValue', ($event.target as HTMLInputElement).value)
    "
  />
</template>

<script setup lang="ts">
defineProps<{
  modelValue: string;
  placeholder: string;
  maxlength: number;
  style?: string;
  disabled?: boolean;
}>();
</script>

<style scoped>
input {
  font-size: 16px;
  padding: 5px;
  border: 1px solid lightgray;
  border-radius: 3px;
}
</style>
