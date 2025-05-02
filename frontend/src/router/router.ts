import Chat from "@/components/pages/Chat.vue";
import Minesweeper from "@/components/pages/Minesweeper.vue";
import NumberPlace from "@/components/pages/NumberPlace.vue";
import SlidePuzzle from "@/components/pages/SlidePuzzle.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  { path: "/chat", component: Chat },
  { path: "/minesweeper", component: Minesweeper },
  { path: "/slidepuzzle", component: SlidePuzzle },
  { path: "/numberplace", component: NumberPlace },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
