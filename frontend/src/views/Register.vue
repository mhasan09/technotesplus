<template>
   <section class="hero is-primary is-fullheight">
  <div class="hero-body">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">
          <form @submit.prevent="handleCreateUser" class="box">
            <div class="field">
              <label for="" class="label">Username</label>
              <div class="control has-icons-left">
                <input type="text" placeholder="e.g. azim001" v-model="state.username" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-user"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Email</label>
              <div class="control has-icons-left">
                <input type="email" placeholder="e.g. azimHasan@gmail.com" v-model="state.email" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password" placeholder="*******" v-model="state.password" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <button class="button is-success" type="submit">
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import axios from 'axios';
import { reactive } from 'vue';
import { backend } from '@/utils';
import router from '@/router';
export default {
  
  setup() {
      if(localStorage.getItem('accessToken') || localStorage.getItem('refreshToken')) 
      {
        router.push({ name: 'Home' })
      }
      const state = reactive({
        username: null,
        password: null,
        email: null
      })
        async function handleCreateUser() {
        
            try {
              const response = await axios.post(`${backend}/api/user/register`, {
                username: state.username,
                password: state.password,
                email: state.email
              });
              if (response.data === 200)
                await router.push({name: 'Login'})
            } catch(err) {
              console.log(err);
            } 
      }

      return {
        state,
        handleCreateUser
    }

  }
}
  

</script>

<style>

</style>