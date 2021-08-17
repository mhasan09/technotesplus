<template>
 <div class="columns is-mobile">
      <div class="column is-half is-offset-one-quarter">
        <div class="card">
          <div class="card-content">
            <div class="actions">
              <i class="fa fa-share-alt fa-lg" @click="getNote"></i>
              <i class="fa fa-edit fa-lg" @click="handleEditPanel"></i>
              <i class="fa fa-trash-alt fa-lg" @click="handleDelete"></i>
            </div>
            <!-- <p class="title">{{ state.id }}</p> -->
            <p class="title" v-if="state.showNote">{{ state.note }}</p>
            <div v-if="state.editClicked">
              <textarea class="textarea is-medium is-primary" type="text" v-model="state.note" placeholder="Primary input"></textarea>
              <p class="mt-4"></p>
              <div class="buttons">
                <button class="button is-primary" @click="handleSave">Save</button>
                <button class="button is-danger" @click="closeEditPanel">Cancel</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import {backend} from "@/utils";
export default {
    props: {
      id: {
        type: Number,
        required: true,
      },
      note: {
        type: String,
        required: true
      }
    },
    setup(props, { emit }) {
      const state = reactive({
        id: props.id,
        note: props.note,
        editClicked: false,
        showNote: true
      });

    // This function will save the edited data

     const handleSave = async _ => {
        try {
          const response = await axios.put(`${backend}/api/note/update/${props.id}`, {
            content: state.note
          }, {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`
            }
          });
          if(response.status === 200) {
            //Success
            state.editClicked = false;
            state.showNote = true
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
              onClick: function(){} // Callback after click
            }).showToast();
          }
        } catch(err) {
          const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });
          localStorage.setItem('accessToken', refresh.data.access);
          const refreshResponse = await axios.put(`${backend}/api/note/update/${props.id}`, {
            content: state.note
          }, {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`
            }
          });
          if(refreshResponse.status === 200) {
            //Success
            state.editClicked = false;
          }
        } 
      }


     const handleDelete = async _ => {
        try {
          const response = await axios.delete(`${backend}/api/note/delete/${props.id}`, {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`
            }
          });
          if(response.status === 200) {
            emit('removeNote', { id: props.id })
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
        } catch(err) {
          const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });
          localStorage.setItem('accessToken', refresh.data.access);
          const refreshResponse = await axios.delete(`${backend}/api/note/delete/${props.id}`, {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`
            }
          });
          if(refreshResponse.status === 200) {
            emit('removeNote', { id: props.id })
          }
        }
      }

      const handleEditPanel = () =>{
        state.editClicked = true
        state.showNote = false

      }

      const closeEditPanel = () =>{
        state.editClicked = false
      }


      const getNote = async _ => {
        const url = `${backend}/api/get_note/${props.id}`
        console.log(url);
        
      }


    return {
        state,
        handleDelete,
        handleSave,
        handleEditPanel,
        closeEditPanel,
        getNote
      }
    }
}
</script>

<style>
.actions{
  margin-left:77%
}
i{
   padding-left: 1em;
}

</style>