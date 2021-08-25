<template>
  <div class="columns is-mobile">
    <div class="column is-half is-offset-one-quarter">
      <div class="card">
        <div class="card-content">
          <div class="actions">
            <i class="fa fa-share-alt fa-lg" @click="toggleModal"></i>
            <i class="fa fa-edit fa-lg" @click="handleEditPanel"></i>
            <i class="fa fa-trash-alt fa-lg" @click="handleDelete"></i>
          </div>
          <!-- <p class="title">{{ state.id }}</p> -->
          <p class="title" v-if="state.showNote">{{ state.note }}</p>
          <div v-if="state.editClicked">
            <textarea
              class="textarea is-medium is-primary"
              type="text"
              v-model="state.note"
              placeholder="Primary input"
            ></textarea>
            <p class="mt-4"></p>
            <div class="buttons">
              <button class="button is-primary" @click="handleSave">
                Save
              </button>
              <button class="button is-danger" @click="closeEditPanel">
                Cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Modal @closeModal="toggleModal" :modalActive="modalActive">
    <div class="modal-content">
      <!-- <h1>{{ state.id }}</h1>
        <p>{{ state.url }}</p> -->
      <div class="panel-block">
        <p class="control has-icons-left">
          <input
            class="input is-success"
            type="text"
            placeholder="Search"
            v-model="state.search"
          />
          <span class="icon is-left">
            <i class="fas fa-search" aria-hidden="true"></i>
          </span>
        </p>
      </div>
      <table class="table">
        <thead>
          <tr>
            <!-- <p class="mt-4"></p> -->
          </tr>
        </thead>
      
        <tr>
          <td class="suggested">Suggested</td>
        </tr>
        <p class="mb-2"></p>
        <tbody v-for="user in searchFilter" :key="user.id" :userid="user.id">
          <tr>
            <th><i class="fas fa-user fa-lg" aria-hidden="true"></i></th>
            <td class="username">{{ user.username }}</td>
            <!-- <td class="email">{{ user.email }}</td> -->
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>
              <button class="button is-primary is-small" @click="sendNotification(user.id,user.email,user.username)">
                Share
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </Modal>
</template>

<script>
import { reactive, onMounted } from "vue";
import axios from "axios";
import { backend } from "@/utils";
import Modal from "@/components/Modal.vue";
import { ref,computed } from "vue";
export default {
  components: {
    Modal,
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
    note: {
      type: String,
      required: true,
    },
  },
  emits: ["removeNote"],
  setup(props, { emit }) {
    const state = reactive({
      id: props.id,
      note: props.note,
      editClicked: false,
      showNote: true,
      url: null,
      users: [],
      search: '',
    });

    // This function will save the edited data

    const handleSave = async (_) => {
      try {
        const response = await axios.put(
          `${backend}/api/note/update/${props.id}`,
          {
            content: state.note,
          },
          {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          }
        );
        if (response.status === 200) {
          //Success
          state.editClicked = false;
          state.showNote = true;
          Toastify({
            text: "Note edited",
            duration: 3000,
            destination: "https://github.com/apvarun/toastify-js",
            newWindow: true,
            close: true,
            gravity: "bottom", // `top` or `bottom`
            position: "right", // `left`, `center` or `right`
            backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
            stopOnFocus: true, // Prevents dismissing of toast on hover
            onClick: function () {}, // Callback after click
          }).showToast();
        }
      } catch (err) {
        const refresh = await axios.post(`${backend}/api/token/refresh/`, {
          refresh: localStorage.refreshToken,
        });
        localStorage.setItem("accessToken", refresh.data.access);
        const refreshResponse = await axios.put(
          `${backend}/api/note/update/${props.id}`,
          {
            content: state.note,
          },
          {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`,
            },
          }
        );
        if (refreshResponse.status === 200) {
          //Success
          state.editClicked = false;
        }
      }
    };

    const handleDelete = async (_) => {
      try {
        const response = await axios.delete(
          `${backend}/api/note/delete/${props.id}`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          }
        );
        if (response.status === 200) {
          emit("removeNote", { id: props.id });
          Toastify({
            text: "Note deleted",
            duration: 3000,
            destination: "https://github.com/apvarun/toastify-js",
            newWindow: true,
            close: true,
            gravity: "bottom", // `top` or `bottom`
            position: "right", // `left`, `center` or `right`
            backgroundColor: "linear-gradient(to right, #864ba2, #bf3a30)",
            stopOnFocus: true, // Prevents dismissing of toast on hover
          }).showToast();
        }
      } catch (err) {
        const refresh = await axios.post(`${backend}/api/token/refresh/`, {
          refresh: localStorage.refreshToken,
        });
        localStorage.setItem("accessToken", refresh.data.access);
        const refreshResponse = await axios.delete(
          `${backend}/api/note/delete/${props.id}`,
          {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`,
            },
          }
        );
        if (refreshResponse.status === 200) {
          emit("removeNote", { id: props.id });
        }
      }
    };

    const handleEditPanel = () => {
      state.editClicked = true;
      state.showNote = false;
    };

    const closeEditPanel = () => {
      state.editClicked = false;
      state.showNote = true;
    };

    const modalActive = ref(false);
    const toggleModal = () => {
      state.url = `${backend}/api/get_note/${props.id}`;
      modalActive.value = !modalActive.value;
    };

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


    const sendNotification = async (userid,email,username) => {

      state.url = `${backend}/api/get_note/${props.id}`;
     
      try {
          
        const response = await axios.post(`${backend}/api/email`,
          {
              'userid': userid,
              'username': username,
              'email': email,
              'url': state.url,
              'note': state.note
          },
          {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`,
            },
          }
        );
        if (response.status === 200) {
          Toastify({
              text: "Notification send",
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
          
        }
      }catch(err){
        console.log(err)
      } 
    };


    const searchFilter = computed(() => {
      return state.users.filter(user => user.username.toLowerCase().includes(state.search.toLowerCase()))

    });




 


    return {
      state,
      handleDelete,
      handleSave,
      handleEditPanel,
      closeEditPanel,
      toggleModal,
      getUsers,
      sendNotification,
      searchFilter,
      modalActive,
    };
  },
};
</script>

<style>
.actions {
  margin-left: 77%;
}
.title{
  white-space: pre-line;
}
i {
  padding-left: 1em;
}
.input {
  width: 85%;
}
.username{
  font-size: 19px;
}
.email{
  font-size: 19px;
}
.suggested{
  margin-left: 10%;
  font-size: 22px;
}
.fa-lg {
    font-size: 1.33333em;
    line-height: 1.50em;
    vertical-align: -.0667em;
}
.panel-block:not(:last-child), .panel-tabs:not(:last-child) {
    border-bottom: 1px solid #ffffff;
}
.table td, .table th {
    border: 1px solid #ffffff;
    
}

</style>