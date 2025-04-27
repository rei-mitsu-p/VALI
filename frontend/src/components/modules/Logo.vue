<template>
  <div class="logo">
    <a href="/">
      <img src="/img/squid.svg" class="blue-shadow" />
      <img src="@/assets/ninja.svg" class="red-shadow" />
      <img src="@/assets/shuriken.svg" class="shuriken" />
    </a>
  </div>
</template>

<style scoped>
.logo {
  position: relative;
}
.logo img {
  width: 25px;
  vertical-align: middle;
}
.logo .blue-shadow,
.logo .red-shadow {
  transition: filter 300ms;
}
.logo .blue-shadow:hover {
  filter: drop-shadow(0 0 15px blue);
}
.logo .red-shadow:hover {
  filter: drop-shadow(0 0 15px red);
}
.logo .shuriken {
  position: absolute;
  top: 50%;
  left: 75%;
  width: 20px;
  margin: 0;
  opacity: 0;
  pointer-events: none;
}
.logo:hover .shuriken {
  opacity: 1;
  animation: throwShuriken 0.5s linear infinite;
}

@keyframes throwShuriken {
  0% {
    transform: translate(-50%, -50%) scale(1) rotate(0deg);
  }
  100% {
    transform: translate(-200%, -50%) scale(0.5) rotate(360deg);
  }
}
</style>
