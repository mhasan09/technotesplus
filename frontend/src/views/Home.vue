<template>
  <div class="container">
    <div class="columns is-mobile">
      <div class="column is-half is-offset-one-quarter">
        <strong class="greetings">Hi,{{ state.user.username }}</strong>
        <p class="mb-4"></p>
      </div>
    </div>
    <Note
      v-for="note in state.notes"
      :key="note.id"
      :id="note.id"
      :note="note.CONTENT"
      @removeNote="handleRemoveNote"
    />
  </div>
</template>

<script>
import { reactive, onMounted } from "vue";
import axios from "axios";
import { ref } from "vue";
import Note from "../components/Note.vue";
import { backend } from "@/utils";
import router from "@/router";
import { useRouter } from "vue-router";
export default {
  components: {
    Note,
  },

  name: "Notes",
  setup(props) {
    const state = reactive({
      notes: [],
      user: [],
    });

    // We get all the notes for the user
    const getNotes = async (_) => {
      try {
        const response = await axios.get(`${backend}/api/user/notes`, {
          headers: {
            Authorization: `Bearer ${localStorage.accessToken}`,
          },
        });
        if (response.status === 200) {
          state.notes = response.data;
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
              state.notes = refreshResponse.data;
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
      getNotes();
    });

    const getUser = async (_) => {
      try {
        const response = await axios.get(`${backend}/api/get_user`, {
          headers: {
            Authorization: `Bearer ${localStorage.accessToken}`,
          },
        });
        if (response.status === 200) {
          state.user = response.data;
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
            const refreshResponse = await axios.get(`${backend}/api/get_user`, {
              headers: {
                Authorization: `Bearer ${refresh.data.access}`,
              },
            });
            if (refreshResponse.status === 200) {
              state.user = refreshResponse.data;
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
      getUser();
    });

    // Note component sends us the Id of the deleted note and we just remove
    // it from the list
    // const handleRemoveNote = childData => state.notes = state.notes.filter(note => note.id !== childData.id );
    const handleRemoveNote = (childData) => {
      state.notes = state.notes.filter((note) => note.id !== childData.id);
    };

    return {
      state,
      handleRemoveNote,
    };
  },
};
</script>

<style>
.greetings {
  font-size: 23px;
}
.is-right {
  margin-right: 5%;
}
@media screen and (device-width: 360px) and (device-height: 640px) and (orientation: portrait) {
  .columns.is-mobile > .column.is-offset-one-quarter {
    margin-left: 5%;
  }
  .columns.is-mobile > .column.is-half {
    flex: none;
    width: 90%;
  }
  i{
    display: inline-block;
  }
  .actions{
    margin-left: 54%;
    margin-bottom: 20%;
  }
  .greetings {
    margin-top: 5%;
}
}
</style>