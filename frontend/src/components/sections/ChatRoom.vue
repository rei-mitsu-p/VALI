<template>
  <div class="chat-box">
    <strong>{{ roomName }}</strong>
    <div ref="messageArea" class="message-area">
      <div v-for="msg in messages" :key="msg">
        {{ msg }}
      </div>
    </div>
    <div class="chat-form">
      <BaseTextArea
        v-model="message"
        placeholder="Enter message"
        :maxlength="200"
      />
      <BaseButton @clicked="sendMessage">Send</BaseButton>
    </div>
  </div>
</template>

<script setup lang="ts">
import BaseButton from "@/components/elements/BaseButton.vue";
import BaseTextArea from "@/components/elements/BaseTextArea.vue";
import chatSocket from "@/socket/socket";
import { getCurrentHHmm } from "@/utils/date-utils";
import { nextTick, onMounted, onUnmounted, ref } from "vue";

const props = defineProps<{
  name: string;
  roomName: string;
}>();

const messageArea = ref<HTMLDivElement | null>(null);
const message = ref("");
const messages = ref<string[]>([]);

onMounted(() => {
  if (!chatSocket.connected) {
    chatSocket.connect();
  }
  chatSocket.emit("set_name", { name: props.name });
  chatSocket.emit("enter_room", { roomName: props.roomName });
  chatSocket.on("message", (data) => {
    messages.value.push(`${getCurrentHHmm()} ${data}`);
    nextTick(() => {
      if (messageArea.value) {
        messageArea.value.scrollTop = messageArea.value.scrollHeight;
      }
    });
  });
});

const sendMessage = () => {
  if (message.value.trim()) {
    chatSocket.emit("send_message", {
      message: message.value,
      roomName: props.roomName,
    });
    message.value = "";
  }
};

onUnmounted(() => {
  if (chatSocket.connected) {
    chatSocket.disconnect();
  }
});
</script>

<style scoped>
.chat-box {
  width: 100%;
  height: 100%;
  border-radius: 3px;
  box-shadow: 0 2px 5px lightgray;
  padding: 15px;
  text-align: left;
  box-sizing: border-box;
}

.message-area {
  width: 100%;
  height: 75%;
  overflow-y: auto;
  padding: 5px;
  background-color: whitesmoke;
  margin-bottom: 10px;
  border-radius: 3px;
  word-break: break-all;
  box-sizing: border-box;
}

.message-area > div {
  padding: 5px;
  border-bottom: silver solid 1px;
}

.chat-form {
  display: flex;
  height: 15%;
  gap: 5px;
}

textarea {
  padding: 5px;
  width: 100%;
}
</style>
