<template>
  <header>
    <img
      src="@/assets/menu-button.svg"
      @click="isShowMenu = !isShowMenu"
      class="menu-button"
    />
    <Logo />
    <nav class="menu" v-if="isShowMenu">
      <RouterLink to="/chat">Chat</RouterLink>
    </nav>
  </header>
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
  border-bottom: silver 1px solid;
  height: 50px;
}

.menu-button {
  width: 20px;
  margin: 15px;
}

.menu {
  width: 150px;
  position: absolute;
  background-color: white;
  margin-top: 5px;
  padding: 10px;
  border-right: silver 1px solid;
}

.menu a {
  display: block;
  padding: 5px;
}

.contents {
  text-align: center;
}
</style>
