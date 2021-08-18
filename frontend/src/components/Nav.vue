<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" @click="handlePushToHome">
        <strong class="logo">TechNotesPlus</strong>
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons" v-if="($route.name === 'Register') || ($route.name === 'Login')">
          <a class="button is-primary" @click="handlePushToRegister">
            <strong>Register</strong>
          </a>
          <a class="button is-light" @click="handlePushToLogin">
            Log in
          </a>
        </div>


        <div class="buttons" v-else>
          <a class="button is-info" @click="handlePushToCreateNote">
            Inscribe
          </a>
          <a class="button is-danger" @click="handleLogout">
            Log Out
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>

</template>

<script>
import router from "@/router";
import { useRoute } from 'vue-router';
import { reactive, watch, onMounted } from 'vue';
import { backend } from "@/utils";
import axios from "axios";


export default {
    name: 'Nav',

    setup(props) {
        const route = useRoute();
        const state = reactive({
          selected: null,
        });


        const handlePushToHome = _ => router.push({ name: 'Home' });
        const handlePushToRegister = _ => router.push({ name: 'Register' });
        const handlePushToLogin = _ => router.push({ name: 'Login' });
        const handlePushToShare = _ => router.push({ name: 'Share' });
        const handlePushToCreateNote = _ => router.push({ name: 'CreateNote' });
        const handleLogout = _ => {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            router.push({ name: 'Login' });
        }



        return {
            handlePushToRegister,
            handlePushToLogin,
            handleLogout,
            handlePushToHome,
            handlePushToCreateNote,
            handlePushToShare
        }
    }
}
</script>

<style>
.logo{
  font-size: 33px;
}
</style>


