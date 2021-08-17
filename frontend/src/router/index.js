import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Login from '../views/Login';
import Register from '../views/Register';
import CreateNote from "../components/CreateNote.vue";
import Share from "../components/Share.vue";
const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/create',
    name: 'CreateNote',
    component: CreateNote,
  },
  {
    path: '/share',
    name: 'Share',
    component: Share,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
