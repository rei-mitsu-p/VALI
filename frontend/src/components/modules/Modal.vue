<template>
  <div class="modal-overlay">
    <div class="modal">
      <div class="modal-header">
        <span v-if="title" class="modal-title">{{ title }}</span>
        <button class="modal-close" @click="$emit('close')">×</button>
      </div>
      <ul>
        <li v-for="message in messages" :key="message">
          {{ message }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title?: string;
  messages: Array<string>;
}>();
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal {
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 10px 150px black;
  width: 75%;
  max-width: 600px;
  position: relative;
  animation: fadeIn 0.3s ease-out;
  text-align: left;
  word-wrap: break-word;
}
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.modal-header {
  height: 15px;
}
.modal-title {
  font-size: 16px;
  font-weight: bold;
}
.modal-close {
  position: absolute;
  top: 5px;
  right: 5px;
  background: transparent;
  border: none;
  font-size: 30px;
  cursor: pointer;
  color: gray;
  transition: color 0.2s;
}
.modal-close:hover {
  color: crimson;
}

ul {
  max-height: 350px;
  overflow-y: auto;
  padding: 0;
}
ul::-webkit-scrollbar {
  width: 7px;
}
ul::-webkit-scrollbar-track {
  border-radius: 3px;
}
ul::-webkit-scrollbar-thumb {
  background: gray;
  border-radius: 3px;
}
ul::-webkit-scrollbar-thumb:hover {
  background: dimgray;
}
ul li {
  padding: 10px;
  border-bottom: 1px solid lightgray;
}
</style>
