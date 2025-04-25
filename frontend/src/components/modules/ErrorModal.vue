<template>
  <div v-if="isError" class="modal-overlay">
    <div class="modal">
      <div v-if="title" class="modal-header">
        <span class="modal-title">{{ title }}</span>
      </div>
      <button class="modal-close" @click="$emit('close')">×</button>
      <ul v-if="messages.length">
        <li v-for="message in messages" :key="message">
          {{ message }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  isError: boolean;
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
.modal-close {
  position: absolute;
  top: 3px;
  right: 10px;
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
.modal-header + .modal-close {
  top: 10px;
}
.modal-header {
  display: block;
  width: 95%;
}
.modal-title {
  font-size: 16px;
  font-weight: bold;
}

ul {
  max-height: 350px;
  overflow-y: scroll;
}
ul::-webkit-scrollbar {
  width: 10px;
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
