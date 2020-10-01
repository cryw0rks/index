import Vue from "vue";
import VueRouter from "vue-router";

// View Declaration
import ViewHome from "../views/Home.vue";
import ViewService from "../views/Service.vue";
import ViewPortfolio from "../views/Portfolio.vue";
import ViewContact from "../views/Contact.vue";
import ViewProject from "../views/Project.vue";
import View404 from "../views/404.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "cryw0rks.exe",
    meta: {
      loginRequired: false,
      hideOnLogin: false
    },
    component: ViewHome
  },
  {
    path: "/service",
    name: "service.exe",
    component: ViewService
  },
  {
    path: "/portfolio",
    name: "portfolio.exe",
    component: ViewPortfolio
  },
  {
    path: "/project",
    name: "project.exe",
    component: ViewProject
  },
  {
    path: "/contact",
    name: "contact.exe",
    component: ViewContact
  },
  {
    path: "*",
    name: "404.exe",
    compenent: View404
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;