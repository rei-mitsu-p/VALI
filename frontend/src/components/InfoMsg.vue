<script setup lang="ts">
import { ref, onMounted } from "vue";
import apiClient from "@/api/client";

defineProps<{ title: string }>();

const message = ref("");

onMounted(async () => {
  const response = await apiClient.get("/");
  message.value = response.data.message;
});
</script>

<template>
  <h1>{{ title }}</h1>
  <p>{{ message }}</p>
</template>
