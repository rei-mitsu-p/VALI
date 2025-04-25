import Chat from "@/components/pages/Chat.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [{ path: "/chat", component: Chat }];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
