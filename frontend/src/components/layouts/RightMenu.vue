<template>
  <div class="menu">
    <slot></slot>
  </div>
</template>

<style scoped>
.menu {
  display: flex;
  flex-direction: column;
  position: absolute;
  right: 10px;
  gap: 5px;
}
</style>
