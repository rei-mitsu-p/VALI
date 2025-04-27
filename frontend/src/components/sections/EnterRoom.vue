<template>
  <Modal
    v-if="isError"
    title="Error"
    :messages="errorMessages"
    @close="
      isError = false;
      errorMessages = [];
    "
  />
  <div class="wrapper">
    <InputText v-model="name" placeholder="Enter your name" :maxlength="20" />
    <InputText
      v-model="roomName"
      placeholder="Enter room name"
      :maxlength="20"
    />
    <BaseButton @clicked="startIfValid">Start</BaseButton>
    <div class="room-list">
      <strong>Room List</strong>
      <CustomSlotTable
        v-if="roomnames.length"
        :columns="[
          { key: 'roomName', label: 'Room Name' },
          { key: 'setRoomName', label: '' },
        ]"
        :rows="roomnames.map((name) => ({ roomName: name }))"
      >
        <template #setRoomName="{ row }">
          <BaseButton @clicked="roomName = row.roomName">Set</BaseButton>
        </template>
      </CustomSlotTable>
    </div>
  </div>
</template>

<script setup lang="ts">
import apiClient from "@/api/client";
import BaseButton from "@/components/elements/BaseButton.vue";
import InputText from "@/components/elements/InputText.vue";
import CustomSlotTable from "@/components/modules/CustomSlotTable.vue";
import Modal from "@/components/modules/Modal.vue";
import { MESSAGE } from "@/constants/constants";
import { onMounted, ref } from "vue";

const emit = defineEmits<{
  (event: "start", name: string, roomName: string): void;
}>();

const isError = ref(false);
const errorMessages = ref<Array<string>>([]);

const name = ref("");
const roomName = ref("");

const roomnames = ref<Array<string>>([]);

onMounted(async () => {
  const response = await apiClient.get("/chat/roomnames");
  roomnames.value = response.data.result;
});

const startIfValid = () => {
  if (name.value.trim() === "") {
    errorMessages.value.push(MESSAGE.format(MESSAGE.REQUIRED, "Name"));
  }
  if (roomName.value.trim() === "") {
    errorMessages.value.push(MESSAGE.format(MESSAGE.REQUIRED, "Room Name"));
  }
  if (errorMessages.value.length) {
    isError.value = true;
    return;
  }
  emit("start", name.value, roomName.value);
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  overflow-y: auto;
}

input {
  width: 100%;
  height: 30px;
  margin-bottom: 10px;
  padding: 5px;
  font-size: 16px;
  box-sizing: border-box;
}

.room-list {
  margin-top: 10px;
}

.room-list > table {
  width: 100%;
  height: 100%;
}
</style>
