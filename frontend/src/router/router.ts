import Chat from "@/components/pages/Chat.vue";
import Minesweeper from "@/components/pages/Minesweeper.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  { path: "/chat", component: Chat },
  { path: "/minesweeper", component: Minesweeper },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
