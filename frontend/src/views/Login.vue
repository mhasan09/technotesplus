<template>
   <section class="hero is-primary is-fullheight">
  <div class="hero-body">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">
          <form @submit.prevent="handleLogin" class="box">
            <div class="field">
              <label for="" class="label">Username</label>
              <div class="control has-icons-left">
                <input type="text" v-model="state.username" placeholder="e.g. azim001" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-user"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password" v-model="state.password" placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="checkbox">
                <input type="checkbox">
               Remember me
              </label>
            </div>
            <div class="field">
              <button class="button is-success">
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
  import { reactive, computed } from 'vue';
  import { backend } from '@/utils';
  import router from '@/router';
  export default {
    setup() {
      if(localStorage.getItem('accessToken') || localStorage.getItem('refreshToken')) {
        router.push({ name: 'Home' })
      }
      const state = reactive({
        username: null,
        password: null,
        
      });
      const handleLogin = async _ => {
          try {
            const response = await axios.post(`${backend}/api/token/`, {
              username: state.username,
              password: state.password
            });
            if (response.status === 200) {
              localStorage.setItem('accessToken', response.data.access);
              localStorage.setItem('refreshToken', response.data.refresh);
              await router.push({ name: 'Home' });
            }
          } catch(err) {
            if(err.status === 401) {
              alert('check your credentials')
            } else {
              alert('check if backend server is running')
            }
          } 
        
      }
  
      return {
        state,
        handleLogin,
      }
    }
  }
</script>

