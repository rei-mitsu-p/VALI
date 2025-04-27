<template>
  <h1>Chat</h1>
  <div v-if="!isStarted" class="enter-room">
    <EnterRoom
      @start="
        (name: string, roomName: string) => {
          dispName = name;
          dispRoomName = roomName;
          isStarted = true;
        }
      "
    />
  </div>
  <div v-if="isStarted" class="chat-room">
    <ChatRoom :name="dispName" :roomName="dispRoomName" />
  </div>
</template>

<script setup lang="ts">
import ChatRoom from "@/components/sections/ChatRoom.vue";
import EnterRoom from "@/components/sections/EnterRoom.vue";
import { ref } from "vue";

const isStarted = ref(false);
const dispName = ref("");
const dispRoomName = ref("");
</script>

<style scoped>
.enter-room {
  width: 300px;
  height: 500px;
  margin: auto;
}

.chat-room {
  width: 550px;
  height: 500px;
  margin: auto;
}
</style>
