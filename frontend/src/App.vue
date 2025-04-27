<template>
  <header>
    <img
      src="@/assets/menu-button.svg"
      @click="isShowMenu = !isShowMenu"
      class="menu-button"
    />
    <Logo />
  </header>
  <nav class="menu" v-if="isShowMenu">
    <RouterLink to="/chat">Chat</RouterLink>
    <RouterLink to="/minesweeper">Minesweeper</RouterLink>
  </nav>
  <div class="contents">
    <RouterView />
  </div>
</template>

<script setup lang="ts">
import Logo from "@/components/modules/Logo.vue";
import { ref } from "vue";

const isShowMenu = ref(false);
</script>

<style>
body {
  font-size: 15px;
  font-family: Arial, Helvetica, sans-serif;
  color: black;
  background-color: white;
  line-height: 1.5;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

a {
  color: black;
  text-decoration: none;
}
</style>

<style scoped>
header {
  display: flex;
  align-items: center;
  border-bottom: silver 1px solid;
  height: 40px;
}

.menu-button {
  width: 20px;
  padding: 10px;
  cursor: pointer;
}

.menu {
  width: 150px;
  position: absolute;
  background-color: white;
  border-right: silver 1px solid;
  word-break: break-all;
}

.menu a {
  display: flex;
  padding: 10px;
}

.contents {
  text-align: center;
}
</style>
