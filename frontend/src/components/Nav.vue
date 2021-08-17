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
          <!-- <a class="button is-info" @click="handlePushToCreateNote">
            Inscribe
          </a> -->
          <a class="button is-primary" @click="handlePushToRegister">
            <strong>Register</strong>
          </a>
          <a class="button is-light" @click="handlePushToLogin">
            Log in
          </a>
          <!-- <a class="button is-danger" @click="handleLogout">
            Log Out
          </a> -->
        </div>




        <div class="buttons" v-else>
          <a class="button is-info" @click="handlePushToCreateNote">
            Inscribe
          </a>
          <!-- <a class="button is-primary" @click="handlePushToRegister">
            <strong>Register</strong>
          </a>
          <a class="button is-light" @click="handlePushToLogin">
            Log in
          </a> -->
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
          // user: []
        });


      //   watch(() => route.name, () => {
      //   if(route.name === 'CreateNote' || route.name === 'Home') {
      //     state.selected = 0;
      //      console.log(route.name);
      //   } else if (route.name === 'Login' || route.name === 'Register')  {
      //     state.selected = 1;
      //     console.log(route.name);
      //   }
      // })

      // const showNavContent = () =>{
      //   const route_name = route.name
      //   console.log(route_name);
      //   return route_name
      // }





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


    //   const getUser = async (_) => {
    //   try {
    //     const response = await axios.get(`${backend}/api/get_user`, {
    //       headers: {
    //         Authorization: `Bearer ${localStorage.accessToken}`,
    //       },
    //     });
    //     if (response.status === 200) {
    //       state.user = response.data;
    //       console.log(state.user)
    //     }
    //   } catch (err) {
    //     if (err.status === 500) {
    //       //Throw error
    //     } else {
    //       try {
    //         const refresh = await axios.post(`${backend}/api/token/refresh/`, {
    //           refresh: localStorage.refreshToken,
    //         });
    //         localStorage.setItem("accessToken", refresh.data.access);
    //         const refreshResponse = await axios.get(`${backend}/api/get_user`, {
    //           headers: {
    //             Authorization: `Bearer ${refresh.data.access}`,
    //           },
    //         });
    //         if (refreshResponse.status === 200) {
    //           state.user = refreshResponse.data;
    //         }
    //       } catch {
    //         localStorage.removeItem("accessToken");
    //         localStorage.removeItem("refreshToken");
    //         await router.push({ name: "Login" });
    //       }
    //     }
    //   }
    // };
    // onMounted(() => {
    //   getUser();
    // });


        return {
            handlePushToRegister,
            handlePushToLogin,
            handleLogout,
            handlePushToHome,
            handlePushToCreateNote,
            handlePushToShare
            // showNavContent
        }
    }
}

</script>

<style>
.logo{
  font-size: 33px;
}
</style>


