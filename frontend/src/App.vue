<script setup lang="ts">
import ninja from "@/assets/ninja.svg";
import InfoMsg from "@/components/InfoMsg.vue";
</script>

<template>
  <div class="center">
    <a href="/">
      <img src="/img/squid.svg" class="logo blue-shadow" />
    </a>
    <img :src="ninja" class="logo red-shadow" />
    <InfoMsg title="VALI TOP" />
  </div>
</template>

<style scoped>
.center {
  text-align: center;
}
.logo {
  height: 6em;
  padding: 1.5em;
  transition: filter 300ms;
}
.logo.blue-shadow:hover {
  filter: drop-shadow(0 0 2em blue);
}
.logo.red-shadow:hover {
  filter: drop-shadow(0 0 2em red);
}
</style>
