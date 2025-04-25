<template>
  <textarea
    v-model="text"
    :placeholder="placeholder"
    :maxlength="maxlength"
    :disabled="disabled"
    :style="customStyle"
  ></textarea>
</template>

<script setup lang="ts">
import { computed } from "vue";

const emit = defineEmits(["update:modelValue"]);

const props = defineProps<{
  modelValue: string;
  placeholder: string;
  maxlength: number;
  customStyle?: string;
  disabled?: boolean;
}>();

const text = computed({
  get: () => props.modelValue,
  set: (val: string) => emit("update:modelValue", val),
});
</script>

<style scoped>
textarea {
  font-size: 16px;
  border: 1px solid lightgray;
  border-radius: 3px;
  resize: none;
}
</style>
