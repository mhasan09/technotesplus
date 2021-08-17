<template>
  <div class="columns is-mobile">
    <div class="column is-half is-offset-one-quarter">
      <div class="field">
        <div class="control">
          <textarea
            class="textarea is-medium is-primary"
            placeholder="Let's list what to do !!!"
            id="note"
            v-model="state.note"
          ></textarea>
        </div>
      </div>
      <div class="buttons">
        <button class="button is-primary" @click="handleAddNote">
          Add Notes
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, computed } from "vue";
import axios from "axios";
import { backend } from "@/utils";
import router from "@/router";

export default {
  name: "CreateNote",
  setup() {
    const state = reactive({
      note: null,
    });
    const handleAddNote = async (_) => {
      try {
           // Let's get the initial response first
            // If it fails then I need to send the refresh token and try again
            // If it fails again then that means the refresh token expired and I can log out the user
        const response = await axios.post(
          `${backend}/api/note/create`,
          { content: state.note },
          {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          }
        );
        if (response.status === 200) {
          console.log("note is added");
          Toastify({
              text: "Note added",
              duration: 3000,
              destination: "https://github.com/apvarun/toastify-js",
              newWindow: true,
              close: true,
              gravity: "bottom", // `top` or `bottom`
              position: "right", // `left`, `center` or `right`
              backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
              stopOnFocus: true, // Prevents dismissing of toast on hover
              onClick: function(){} // Callback after click
            }).showToast();
          state.note = null;
          await router.push({ name: "Home" });
        }
      } catch (err) {
        if (err.status === 500) {
          console.log("Check your internet connection!");
        } else {
          try {
            const refresh = await axios.post(`${backend}/api/token/refresh/`, {
              refresh: localStorage.refreshToken,
            });
            await localStorage.setItem("accessToken", refresh.data.access);
            const refreshResponse = await axios.post(
              `${backend}/api/note/create`,{ content: state.note },
              {
                headers: {
                  Authorization: `Bearer ${localStorage.accessToken}`,
                },
              }
            );
            if (refreshResponse.status === 200) {
              state.note = null;
            }
          } catch (err) {
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");
            await router.push({ name: "Login" });
          }
        }
      }
    };
    return {
      state,
      handleAddNote,
    };
  },
};
</script>

<style>
</style>