<template>
  <p class="mt-6"></p>
  <div class="columns is-mobile">
    <div class="column is-half is-offset-one-quarter">
      <article class="panel is-success">
        <p class="panel-tabs"></p>
        <div class="panel-block">
          <p class="control has-icons-left">
            <input class="input is-success" type="text" placeholder="Search" />
            <span class="icon is-left">
              <i class="fas fa-search" aria-hidden="true"></i>
            </span>
          </p>
        </div>
        <a
          class="panel-block is-active"
          v-for="user in state.users"
          :key="user.id"
          :id="user.id"
        >
          <span class="panel-icon">
            <i class="fas fa-user" aria-hidden="true"> </i>
          </span>
          <p class="mr-3"></p>
          <span>{{ user.username }}</span>
            <p class="ml-4"></p>
          <button class="button is-primary" style="margin-left:50%">Share</button>
        </a>
      </article>
    </div>
  </div>
</template>

<script>
import { reactive, onMounted } from "vue";
import axios from "axios";
import Note from "../components/Note.vue";
import { backend } from "@/utils";
import router from "@/router";
import { useRouter } from "vue-router";
export default {
  name: "Share",
  setup(props) {
    const state = reactive({
      users: [],
    });

    // this function will get all the user
    const getUsers = async (_) => {
      try {
        const response = await axios.get(`${backend}/api/users/all`, {
          headers: {
            Authorization: `Bearer ${localStorage.accessToken}`,
          },
        });
        if (response.status === 200) {
          state.users = response.data;
        }
      } catch (err) {
        if (err.status === 500) {
          //Throw error
        } else {
          try {
            const refresh = await axios.post(`${backend}/api/token/refresh/`, {
              refresh: localStorage.refreshToken,
            });
            localStorage.setItem("accessToken", refresh.data.access);
            const refreshResponse = await axios.get(
              `${backend}/api/user/notes`,
              {
                headers: {
                  Authorization: `Bearer ${refresh.data.access}`,
                },
              }
            );
            if (refreshResponse.status === 200) {
              state.users = refreshResponse.data;
            }
          } catch {
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            await router.push({ name: "Login" });
          }
        }
      }
    };
    onMounted(() => {
      getUsers();
    });


    return {
      state,
    };
  },
};
</script>

<style>
.button is-primary{
    float: right;
}
.gap{
    width:50%
}
</style>